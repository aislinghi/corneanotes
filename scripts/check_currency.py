#!/usr/bin/env python3
"""Currency check: report what is overdue, due soon, or affected by a changed figure.

Reads:
  content/**/*.md       front matter: status, last_reviewed, next_review_due, risks_used;
                        and the "Sources and how this document was produced" table
  evidence/**/*.yaml    any entry with next_check_due (and last_changed, last_checked)
  sites/**/*.yaml       any block with next_review_due (e.g. local formularies)

Writes a Markdown report to stdout. Files and keys starting with "_" or
"example" are templates and are skipped.

An AI review that finds no change is stored as a review record (see
reviews/README.md). If --records points at a folder of records, a record's
next_review_due replaces the file's own date when it is later.

Usage: python3 scripts/check_currency.py [--today YYYY-MM-DD] [--soon-days N]
                                         [--records DIR] [--json FILE]
"""
import argparse
import datetime as dt
import json
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREFIX = {"risks": "risk", "costs": "cost"}


def as_date(value):
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str) and value.strip():
        try:
            return dt.date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def skip(path):
    return path.name.startswith("_") or path.name.lower() == "readme.md"


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return yaml.safe_load(parts[1]) or {}


def walk(node, path=()):
    """Yield (key_path, dict) for every dict that carries a review date."""
    if isinstance(node, dict):
        if "next_check_due" in node or "next_review_due" in node:
            yield path, node
        for key, value in node.items():
            if str(key).lower().startswith("example"):
                continue
            yield from walk(value, path + (str(key),))


def load_evidence():
    """Return {key: entry} for every evidence entry, e.g. risk.cornea.cxl.haze."""
    index = {}
    for f in sorted((ROOT / "evidence").rglob("*.yaml")):
        if skip(f):
            continue
        rel = f.relative_to(ROOT / "evidence").parts  # country, specialty, subspecialty, file
        subspecialty = rel[-2] if len(rel) >= 2 else "general"
        prefix = PREFIX.get(f.stem, f.stem)
        data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        if f.stem not in PREFIX:
            data = data.get("agents", data)
        for key_path, entry in walk(data):
            if not key_path:
                continue
            key = ".".join((prefix, subspecialty) + key_path)
            index[key] = {"entry": entry, "file": f.relative_to(ROOT)}
    return index


def load_records(folder):
    """Return {subject: latest record} from AI review records."""
    latest = {}
    if not folder:
        return latest
    for f in sorted(pathlib.Path(folder).rglob("*.yaml")):
        rec = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        subject, on = rec.get("subject"), as_date(rec.get("reviewed_on"))
        if subject and on and (subject not in latest or on > as_date(latest[subject]["reviewed_on"])):
            latest[subject] = rec
    return latest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--soon-days", type=int, default=60)
    ap.add_argument("--records", help="folder of AI review records")
    ap.add_argument("--json", help="also write the items due for review to this file")
    args = ap.parse_args()
    today, soon = args.today, args.today + dt.timedelta(days=args.soon_days)
    records = load_records(args.records)

    overdue, due_soon, missing, stale_docs, broken, no_sources = [], [], [], [], [], []
    due_subjects = []

    def effective(subject, due):
        rec = records.get(subject)
        rec_due = as_date(rec.get("next_review_due")) if rec else None
        if rec_due and (due is None or rec_due > due):
            return rec_due
        return due

    def check(label, due, subject=None):
        if subject:
            due = effective(subject, due)
        if due is None:
            missing.append(label)
        elif due < today:
            overdue.append(f"{label}: due {due}")
        elif due <= soon:
            due_soon.append(f"{label}: due {due}")
        if subject and due is not None and due <= soon:
            due_subjects.append({"subject": subject, "due": str(due)})

    evidence = load_evidence()
    for key, item in evidence.items():
        check(f"`{key}` ({item['file']})", as_date(item["entry"].get("next_check_due")), key)

    for f in sorted((ROOT / "sites").rglob("*.yaml")):
        if skip(f):
            continue
        data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        for key_path, block in walk(data):
            name = ".".join(key_path) or "file"
            check(f"`{f.relative_to(ROOT)}` {name}", as_date(block.get("next_review_due")))

    for f in sorted((ROOT / "content").rglob("*.md")):
        if skip(f):
            continue
        meta = front_matter(f)
        if meta is None:
            continue
        rel = f.relative_to(ROOT)
        if "## Sources and how this document was produced" not in f.read_text(encoding="utf-8"):
            no_sources.append(f"`{rel}`")
        if meta.get("status") == "approved":
            check(f"`{rel}`", as_date(meta.get("next_review_due")), str(rel))
        reviewed = as_date(meta.get("last_reviewed"))
        for key in meta.get("risks_used") or []:
            if key not in evidence:
                broken.append(f"`{rel}` quotes `{key}`, which is not in `evidence/`")
                continue
            changed = as_date(evidence[key]["entry"].get("last_changed"))
            if changed and (reviewed is None or changed > reviewed):
                stale_docs.append(
                    f"`{rel}`: `{key}` changed {changed}, document last reviewed {reviewed or 'never'}"
                )

    out = [f"# Currency check, {today}", ""]
    sections = [
        ("Overdue", overdue),
        (f"Due in the next {args.soon_days} days", due_soon),
        ("Documents quoting a figure that changed after they were last reviewed", stale_docs),
        ("Documents quoting a figure that does not exist", broken),
        ("Missing a review date", missing),
        ("Missing the sources and production table", no_sources),
    ]
    total = 0
    for title, items in sections:
        out += [f"## {title} ({len(items)})", ""]
        out += [f"- [ ] {i}" for i in items] or ["None."]
        out.append("")
        total += len(items)
    out.append("Generated by `scripts/check_currency.py`. Items due are reviewed by the AI review (see `reviews/README.md`). Any change to a figure or document goes through a pull request approved by a person.")
    print("\n".join(out))
    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(due_subjects, indent=2), encoding="utf-8")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
