# Formulary applications

Applications to add a new medicine to a local formulary, and the periodic reviews of medicines already on it. Every service applying for the same medicine needs the same evidence, so the evidence review is written once here and reused.

## What is shared

- The medicine, its indication and its proposed place in the treatment pathway
- Evidence review: efficacy, safety, comparators, with every source cited
- National guidance status (for example NICE technology appraisals or guidelines), with the date it was checked
- Licensing status, including whether use is off-label or unlicensed (for example specially manufactured eye drops)
- National list price, held in `evidence/` with its source and date
- Monitoring requirements and review criteria
- For reviews: a standard checklist of what has changed since the last review (new evidence, safety alerts, guidance, price)

## What is local

- Which committee the application goes to, and its own form or format
- Expected local patient numbers and the budget impact
- Local prescribing and supply arrangements (who prescribes, hospital-only or shared care, pharmacy supply route)
- Local approval decision and review date

Local details come from the service's `sites/` file or are added by the service in its own copy. Commercially confidential pricing (for example local contract prices) must never be added to this public repository.
