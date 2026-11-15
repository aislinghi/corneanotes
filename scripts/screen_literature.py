#!/usr/bin/env python3
"""Literature screen for AI reviews.

Two modes:

  search  For each subject due for review, run the PubMed searches of every
          screen topic that covers it, limited to items published since the
          subject was last reviewed. Writes the results (and exactly what was
          searched) to a JSON file for the AI reviewer.

            python3 scripts/screen_literature.py search --due due.json --out candidates.json \\
                [--records DIR]

  test    Check that every item ever reported as missed (reviews/missed/) is now
          found by the screen: PubMed items must be returned by the topic's
          searches, and web sources must be listed in its national_sources.
          Fails if any is not. Runs on every pull request that changes the screen.

            python3 scripts/screen_literature.py test

Uses the NCBI E-utilities API. No personal details are sent.
"""
import argparse
import datetime as dt
import fnmatch
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
DEFAULT_LOOKBACK_YEARS = 5
MAX_PER_QUERY = 1000

sys.path.insert(0, str(ROOT / "scripts"))
from check_currency import as_date, front_matter, load_evidence, load_records  # noqa: E402


def eutils(endpoint, **params):
    params.update({"retmode": "json", "tool": "corneanotes"})
    url = EUTILS + endpoint + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = json.load(resp)
            time.sleep(0.4)  # stay under NCBI's limit of 3 requests a second
            return data
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def search(query, mindate=None, maxdate=None):
    params = {"db": "pubmed", "term": query, "retmax": MAX_PER_QUERY}
    if mindate:
        params.update({"datetype": "edat", "mindate": mindate, "maxdate": maxdate})
    res = eutils("esearch.fcgi", **params)["esearchresult"]
    return int(res["count"]), res["idlist"]


def summaries(pmids):
    out = []
    for i in range(0, len(pmids), 100):
        chunk = pmids[i:i + 100]
        res = eutils("esummary.fcgi", db="pubmed", id=",".join(chunk))["result"]
        for pmid in chunk:
            item = res.get(pmid, {})
            out.append({
                "pmid": pmid,
                "title": item.get("title", ""),
                "journal": item.get("fulljournalname", ""),
                "pubdate": item.get("pubdate", ""),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            })
    return out


def load_topics():
    topics = {}
    for f in sorted((ROOT / "reviews" / "screen").glob("*.yaml")):
        if f.name.startswith("_"):
            continue
        t = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        topics[t.get("topic", f.stem)] = t
    return topics


def covers(topic, subject):
    pats = (topic.get("covers") or {})
    return any(fnmatch.fnmatch(subject, p) for p in (pats.get("evidence") or []) + (pats.get("documents") or []))


def last_reviewed(subject, evidence, records):
    rec = records.get(subject)
    dates = [as_date(rec.get("reviewed_on"))] if rec else []
    if subject in evidence:
        dates.append(as_date(evidence[subject]["entry"].get("last_checked")))
    else:
        path = ROOT / subject
        if path.exists():
            dates.append(as_date((front_matter(path) or {}).get("last_reviewed")))
    dates = [d for d in dates if d]
    return max(dates) if dates else None


def cmd_search(args):
    due = json.loads(pathlib.Path(args.due).read_text(encoding="utf-8"))
    topics, evidence, records = load_topics(), load_evidence(), load_records(args.records)
    today = dt.date.today()
    out = {"generated_on": str(today), "subjects": []}
    cache = {}
    for item in due:
        subject = item["subject"]
        since = last_reviewed(subject, evidence, records) or today.replace(year=today.year - DEFAULT_LOOKBACK_YEARS)
        entry = {"subject": subject, "due": item["due"], "searched_from": str(since),
                 "searched_to": str(today), "topics": [], "uncovered": False}
        matched = [(name, t) for name, t in topics.items() if covers(t, subject)]
        if not matched:
            entry["uncovered"] = True  # no screen topic: the AI must report this, not pass it
        for name, t in matched:
            results = []
            for q in t.get("pubmed") or []:
                key = (q, str(since))
                if key not in cache:
                    count, ids = search(q, since.strftime("%Y/%m/%d"), today.strftime("%Y/%m/%d"))
                    cache[key] = {"query": q, "count": count, "pmids": ids}
                results.append(cache[key])
            pmids = sorted({p for r in results for p in r["pmids"]})
            entry["topics"].append({
                "topic": name,
                "searches": [{"query": r["query"], "count": r["count"],
                              "truncated": r["count"] > len(r["pmids"])} for r in results],
                "articles": summaries(pmids) if pmids else [],
                "national_sources": t.get("national_sources") or [],
            })
        out["subjects"].append(entry)
    pathlib.Path(args.out).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Screened {len(out['subjects'])} subject(s); results in {args.out}")
    return 0


def cmd_test(_args):
    topics = load_topics()
    failures, checked = [], 0
    for f in sorted((ROOT / "reviews" / "missed").glob("*.yaml")):
        if f.name.startswith("_"):
            continue
        m = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        t = topics.get(m.get("topic"))
        name = f.relative_to(ROOT)
        checked += 1
        if not t:
            failures.append(f"{name}: topic '{m.get('topic')}' not found in reviews/screen/")
            continue
        pmid = str(m.get("pmid") or "").strip()
        if pmid:
            found = any(search(f"({q}) AND {pmid}[uid]")[0] > 0 for q in t.get("pubmed") or [])
            if not found:
                failures.append(f"{name}: PubMed {pmid} is not found by the searches for topic '{m['topic']}'")
        url = (m.get("url") or "").strip()
        if url and not pmid:
            listed = [s.get("url", "") for s in t.get("national_sources") or []]
            if not any(url.startswith(u) or u.startswith(url) for u in listed if u):
                failures.append(f"{name}: {url} is not listed in national_sources for topic '{m['topic']}'")
    if failures:
        print("Screen test FAILED. These reported misses would still be missed:")
        print("\n".join(f"  {x}" for x in failures))
        return 1
    print(f"Screen test passed: all {checked} reported miss(es) are now found by the screen.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("--due", required=True)
    s.add_argument("--out", required=True)
    s.add_argument("--records")
    sub.add_parser("test")
    args = ap.parse_args()
    return cmd_search(args) if args.cmd == "search" else cmd_test(args)


if __name__ == "__main__":
    sys.exit(main())
