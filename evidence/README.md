# Evidence: risk, outcome and cost figures

Every risk or outcome figure, and every national cost or price (for example tissue prices or national tariffs used in business cases), quoted in a document lives here, once. Documents refer to a figure by its key, for example `{{risk.cornea.cxl.example_risk}}`, and never type the number in directly. Update the figure here and every document that quotes it updates too.

## Rules

1. **National data first.** Use national registry or audit data where it exists. Otherwise use high-quality published literature (systematic reviews, large series). Local unit figures are not used: the same operation should be described with the same numbers everywhere.
2. **Every figure has a source.** Give a full reference and a link, and say exactly where in the source the figure appears (table, page, section).
3. **Every figure has a review date.** `last_checked` is when someone last confirmed the figure against its source and looked for newer data. `next_check_due` is when it must be looked at again.
4. **Only people change figures.** Any change goes through a pull request and is approved by a reviewer for that area. Automated checks may flag figures for review, but never change them.

Costs follow the same rules. Use the national published price (with its source and the date it applies from), not a figure from one unit's invoice. Local costs that genuinely differ, such as staffing or estates, belong in that service's `sites/` file.

## File format

Evidence is held per country, because national data differs between countries. For now only the UK is covered: `evidence/uk/`. One YAML file per subspecialty, for example `evidence/uk/ophthalmology/cornea/risks.yaml`:

```yaml
cxl:                                   # procedure or condition
  example_risk:                        # figure name; key becomes risk.cornea.cxl.example_risk
    description: "Plain-English description of the outcome"
    value: "1 in N"                    # as it should read in a patient leaflet
    detail: "Underlying figure, e.g. x% (95% CI a to b), n = ..."
    population: "Who the figure applies to"
    source: "Full reference"
    source_url: "https://..."
    source_location: "Table 2, page 5"
    last_checked: 2026-01-01
    checked_by: "Name"
    next_check_due: 2027-01-01
```
