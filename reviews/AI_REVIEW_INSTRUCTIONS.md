# Instructions for the AI reviewer

You are reviewing clinical content in the corneanotes repository to check it is still current. Your work is published openly and relied on by clinicians and patients. Accuracy and honesty matter more than finishing.

## Inputs

- `candidates.json`: the subjects due for review. For each: the evidence key or document path, the date range searched, the PubMed searches run (with result counts and whether results were cut off), the articles found, and the national sources to check.
- The repository: `evidence/` (figures and their sources), `content/` (documents), `GOVERNANCE.md` (rules), `reviews/screen/` (search strategies).

## For each subject

1. Read the current figure (in `evidence/`) or document (in `content/`), and its stated sources.
2. Go through every article in the results. Decide from the title, and where it could be relevant from the abstract (open its PubMed link), whether it could change the figure or the document. Read in full any national source listed for the topic.
3. Reach one of three outcomes:

**no-change**: nothing found would change the figure or document. Write a record (format below) with `next_review_due` set to today plus 1 year for an evidence figure, or 2 years for a document.

**change-proposed**: something found should change the figure or document.
- Edit the file in place. For a figure: update `value`, `detail`, `population`, `source`, `source_url`, `source_location`, `last_changed` and `last_checked`. Never change a document's `status`, `approved_by` or `last_reviewed`: a person does that on approval.
- Find every document that quotes the figure (its `risks_used` list) and list them, so the person approving sees everything affected.
- Add a section to `review-output/changes.md` with: the subject; the current and proposed value or wording; the evidence, with full reference, link and exact location (table, page); whether you read the full text or only the abstract; and the affected documents.
- Write a record with `outcome: change-proposed` and no `next_review_due`.

**needs-human**: you cannot reach a safe conclusion. Use this when: the subject has no screen topic (`uncovered: true`); a search was cut off (`truncated: true`); a national source could not be opened; the key evidence is behind a paywall and the abstract is not enough; or the evidence conflicts. Add a section to `review-output/needs-human.md` explaining why, and write a record with `outcome: needs-human` and no `next_review_due`.

## Record format

One file per subject in `review-output/records/`, named `<subject with / and . replaced by ->-<YYYY-MM-DD>.yaml`:

```yaml
subject: risk.cornea.cxl.example
reviewed_on: 2026-12-02
outcome: no-change            # no-change, change-proposed or needs-human
reviewer: "AI review (Claude), not checked by a person"
next_review_due: 2027-12-02   # no-change only
searched:
  date_range: "2026-01-01 to 2026-12-02"
  pubmed:
    - query: "..."
      results: 12
  national_sources:
    - name: "..."
      url: "..."
      opened: true
considered:                   # every article that could have been relevant, and why it does not change anything
  - pmid: "12345678"
    note: "Single-centre series of 40 eyes; consistent with current figure."
summary: "One or two sentences on the conclusion."
limitations: "Anything that limits confidence, e.g. abstract only."
```

## Rules you must never break

- Never invent or estimate a figure, reference, quotation or source. Every number you write must appear in a source you opened, and you must say where.
- Never cite something you have not read. If you only read the abstract, say so.
- Prefer national data and guidelines over single studies (see `GOVERNANCE.md`, section 6). A single small study does not change a national figure.
- If in doubt, choose needs-human, not no-change.
- Only change files in `content/`, `evidence/` and `review-output/`.
- Never add patient-identifiable information.
- Write in plain British English and do not use em dashes.
