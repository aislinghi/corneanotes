#!/usr/bin/env python3
"""Render a document for one hospital: fill {{site.*}} and {{risk.*}} placeholders.

    python3 scripts/render.py <document.md> --site sites/hospitals/<hospital>.yaml [--out file.md]

Site details are merged from the hospital file, then its trust, the trust's
networks and the country, with lower levels taking priority. Figures come from
evidence/<country>/. Fails if any placeholder cannot be filled, so nothing is
ever published with a gap.
"""
import argparse
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_currency import load_evidence  # noqa: E402

PLACEHOLDER = re.compile(r"\{\{\s*([a-z_]+(?:\.[A-Za-z0-9_]+)+)\s*\}\}")


def load_level(folder, name, example=False):
    base = ROOT / "sites" / folder
    for candidate in [base / f"{name}.yaml"] + ([base / "_example.yaml"] if example else []):
        if candidate.exists():
            return yaml.safe_load(candidate.read_text(encoding="utf-8")) or {}
    raise SystemExit(f"Site file not found: sites/{folder}/{name}.yaml")


def merge(low, high):
    """Merge dicts; values in `low` (the more local level) win."""
    out = dict(high)
    for k, v in low.items():
        out[k] = merge(v, out[k]) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def site_chain(path):
    hospital = yaml.safe_load(pathlib.Path(path).read_text(encoding="utf-8")) or {}
    example = pathlib.Path(path).name.startswith("_")
    trust = load_level("trusts", hospital["trust"], example) if hospital.get("trust") else {}
    merged = merge(hospital, trust)
    for net in trust.get("networks") or []:
        merged = merge(merged, load_level("networks", net, example))
    country = merged.get("country") or trust.get("country")
    if country:
        merged = merge(merged, load_level("countries", country, example))
    return merged


def lookup(data, dotted):
    for part in dotted.split("."):
        if not isinstance(data, dict) or part not in data:
            return None
        data = data[part]
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("document")
    ap.add_argument("--site", required=True)
    ap.add_argument("--out")
    args = ap.parse_args()

    site = site_chain(args.site)
    evidence = load_evidence()
    text = pathlib.Path(args.document).read_text(encoding="utf-8")
    body = text.split("---", 2)[2] if text.startswith("---") else text
    body = re.sub(r"(?s)<!--.*?-->\n?", "", body)

    missing = []

    def fill(m):
        key = m.group(1)
        if key.startswith("site."):
            value = lookup(site, key[5:])
        elif key in evidence:
            value = evidence[key]["entry"].get("value")
        else:
            value = None
        if value in (None, ""):
            missing.append(key)
            return m.group(0)
        return str(value).strip()

    out = PLACEHOLDER.sub(fill, body).lstrip()
    if missing:
        print("Cannot render: no value for " + ", ".join(sorted(set(missing))), file=sys.stderr)
        return 1
    if args.out:
        pathlib.Path(args.out).write_text(out, encoding="utf-8")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
