#!/usr/bin/env python3
"""Check every document renders: all evidence and site placeholders resolve
against the example hospital, and the evidence and site files are valid.
Runs on every push and pull request."""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
failed = 0
docs = [p for p in sorted((ROOT / "content").rglob("*.md"))
        if not p.name.startswith("_") and p.name.lower() != "readme.md"]
for doc in docs:
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "render.py"), str(doc),
                        "--site", str(ROOT / "sites" / "hospitals" / "_example.yaml"), "--out", "/dev/null"],
                       capture_output=True, text=True)
    rel = doc.relative_to(ROOT)
    if r.returncode != 0:
        failed += 1
        msg = (r.stderr.strip().splitlines() or ["unknown error"])[-1]
        print(f"FAIL {rel}: {msg}")
        print(f"::error file={rel}::{msg}")
    else:
        print(f"ok   {rel}")
print(f"\n{len(docs) - failed} of {len(docs)} documents render.")
sys.exit(1 if failed else 0)
