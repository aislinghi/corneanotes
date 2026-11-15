#!/usr/bin/env python3
"""Patient data check: fail if anything in the repository looks like patient data.

Runs on every push and pull request (see .github/workflows/patient-data-check.yml)
and can be run locally before committing:

    python3 scripts/check_patient_data.py

What it looks for in every tracked file:
  - NHS, CHI or Health and Care numbers (10 digits with a valid check digit)
  - dates of birth (a "DOB" or "date of birth" label followed by a date)
  - hospital or record numbers (an "MRN", "hospital number" or similar label followed by a number)
  - patient name labels ("Patient name: Smith") and letters addressed to a named person
  - UK mobile phone numbers
  - email addresses and postcodes in content/ and evidence/ (sites/ may hold department ones)
  - files that cannot be scanned and may hold patient data: images, scans, video,
    PDFs and Office documents

Findings are reported by type, file and line only. The matched text is never
printed, because logs on a public repository are public.

False positives:
  - a single line can be excluded by adding the marker "pii-check: ignore" to it,
    e.g. <!-- pii-check: ignore --> in Markdown or # pii-check: ignore in YAML;
  - a file that cannot be scanned (e.g. a reviewed image) can be listed in
    .pii-allowlist.
Both are protected by CODEOWNERS, so the reviewer sees every exception.

This check reduces risk; it cannot catch everything (for example free-text
case descriptions). Contributors and reviewers remain responsible for never
adding patient-identifiable information.
"""
import fnmatch
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
IGNORE_MARKER = "pii-check: ignore"
ALLOWLIST = ROOT / ".pii-allowlist"

# Never scanned: generated or third-party files with no patient content.
SKIP_FILES = {"package-lock.json", "LICENSE", "LICENSE-CODE", "scripts/check_patient_data.py"}

# Files that cannot be scanned as text and could contain patient data.
UNSCANNABLE = {
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".heic", ".heif",
    ".dcm", ".dicom", ".mp4", ".mov", ".avi", ".mkv", ".m4v", ".wav", ".mp3", ".m4a",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".odt", ".ods", ".rtf",
    ".zip", ".7z", ".rar",
}
BINARY_OK = {".ico", ".woff", ".woff2", ".ttf", ".otf"}

TEN_DIGITS = re.compile(r"(?<![\d.,-])(\d{3})[ -]?(\d{3})[ -]?(\d{4})(?![\d.,])")

PATTERNS_EVERYWHERE = [
    ("Date of birth",
     re.compile(r"\b(d\.?\s?o\.?\s?b\.?|date of birth|born on)\s*[:\-]?\s*\d", re.I)),
    ("Hospital or record number",
     re.compile(r"\b(mrn|hospital\s*(no|number|num)|hosp\.?\s*no|unit\s*(no|number)|"
                r"patient\s*(id|no|number)|case\s*(no|number)|record\s*(no|number))\b"
                r"\s*[:#.]?\s*[A-Z]{0,3}\d{4,}", re.I)),
    ("Patient name",
     re.compile(r"\bpatient(\s+name)?\s*:\s*(?!\{\{)[A-Z][a-z]+", re.I)),
    ("Letter addressed to a named person",
     re.compile(r"\bDear\s+(Mr|Mrs|Ms|Miss|Mx|Dr|Prof)\.?\s+(?!\{\{)[A-Z][a-z]+")),
    ("UK mobile number",
     re.compile(r"(?<!\d)(07\d{3}|\+44\s?\(?0?\)?\s?7\d{3})\s?\d{3}\s?\d{3}(?!\d)")),
]

PATTERNS_CONTENT = [
    ("Email address", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")),
    ("Postcode", re.compile(r"\b[A-Z]{1,2}\d[A-Z\d]?\s*\d[ABD-HJLNP-UW-Z]{2}\b")),
]
CONTENT_DIRS = ("content/", "evidence/")


def nhs_check_digit_ok(digits):
    """NHS numbers (and CHI and Health and Care numbers) use a modulus 11 check digit."""
    total = sum(int(d) * w for d, w in zip(digits[:9], range(10, 1, -1)))
    check = 11 - (total % 11)
    if check == 11:
        check = 0
    return check != 10 and check == int(digits[9])


def tracked_files():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True)
    return [p for p in out.stdout.decode().split("\0") if p]


def load_allowlist():
    if not ALLOWLIST.exists():
        return []
    lines = ALLOWLIST.read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in lines if l.strip() and not l.strip().startswith("#")]


def main():
    allow = load_allowlist()
    findings = []

    for rel in tracked_files():
        path = ROOT / rel
        if rel in SKIP_FILES or rel.startswith("node_modules/") or not path.is_file():
            continue
        suffix = path.suffix.lower()
        allowed = any(fnmatch.fnmatch(rel, pat) for pat in allow)
        if suffix in UNSCANNABLE:
            if not allowed:
                findings.append((rel, 0, "File type cannot be checked for patient data "
                                         "(add to .pii-allowlist only after review)"))
            continue
        if suffix in BINARY_OK or allowed:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append((rel, 0, "Binary file cannot be checked for patient data "
                                     "(add to .pii-allowlist only after review)"))
            continue

        in_content = rel.startswith(CONTENT_DIRS)
        for n, line in enumerate(text.splitlines(), start=1):
            if IGNORE_MARKER in line:
                continue
            for m in TEN_DIGITS.finditer(line):
                digits = "".join(m.groups())
                if nhs_check_digit_ok(digits):
                    findings.append((rel, n, "Possible NHS, CHI or Health and Care number"))
            checks = PATTERNS_EVERYWHERE + (PATTERNS_CONTENT if in_content else [])
            for label, pattern in checks:
                if pattern.search(line):
                    findings.append((rel, n, label))

    if not findings:
        print("Patient data check passed: nothing that looks like patient data was found.")
        return 0

    print(f"Patient data check FAILED: {len(findings)} possible item(s) found.\n")
    for rel, n, label in findings:
        where = f"{rel}:{n}" if n else rel
        print(f"  {where}  {label}")
        # GitHub annotation (shown on the pull request); never includes the matched text.
        loc = f"file={rel},line={n}" if n else f"file={rel}"
        print(f"::error {loc}::{label}")
    print("\nRemove the data, then commit again. If it is a false positive, add the marker "
          f"'{IGNORE_MARKER}' to that line, or list a reviewed file in .pii-allowlist.")
    print("If real patient data was pushed, removing it in a new commit is not enough: "
          "it stays in the history. Tell the maintainer straight away.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
