---
title: "Title of the document"
type: leaflet            # leaflet, consent, pifu, letter, video-script, protocol, guideline,
                         # referral, teaching, business-case, formulary-application, formulary-review
status: draft            # draft, approved (set by the reviewer) or withdrawn (state why at the top)
version: 0.1
authors:
  - "Your name"
approved_by:             # filled in by the reviewer
last_reviewed:           # YYYY-MM-DD, filled in by the reviewer
next_review_due:         # YYYY-MM-DD
risks_used:              # keys from evidence/ quoted in this document
  - risk.cornea.cxl.example_risk
production:              # how this document was produced; be honest, readers rely on it
  written_by: "Your name and role"
  ai_assistance: none    # none, or describe it, e.g. "First draft of sections 1 to 3 by an AI
                         # assistant, then checked line by line against the sources by the author"
  based_on_template: ""  # if adapted from another document, name it and its licence or permission
---

<!--
Shared core: everything below is the same for every service. Do not put local
details here. Use placeholders instead:
  {{site.name}}, {{site.contacts.main_phone}}, {{site.contacts.urgent_phone}},
  {{site.urgent_access}}, {{site.out_of_hours}}  (from sites/, hospital then trust,
  network and country)
  {{risk.<subspecialty>.<procedure>.<figure>}}   (from evidence/uk/)
Never type a risk figure directly into a document.
-->

## What is this about?

## What to expect

## What are the risks?

About {{risk.cornea.cxl.example_risk}} people ... (example of quoting a figure from evidence/)

## When to get urgent help

{{site.urgent_access}}

Telephone: {{site.contacts.urgent_phone}}

Out of hours: {{site.out_of_hours}}

## Contact us

{{site.name}}, {{site.contacts.main_phone}} ({{site.contacts.hours}})

## Sources and how this document was produced

<!--
Required in every document. One row per section (or per statement, where a
section mixes sources). "Based on" must be one of:
  National data (give the evidence key) | Published guideline | Published research |
  Clinical experience (expert opinion) | Adapted from another document |
  AI-drafted, then checked
Be specific and honest: if a statement rests on the author's own experience
rather than published evidence, say so.
-->

| Section | Based on | Source | Checked by | Date checked |
|---|---|---|---|---|
| What is this about? | | | | |
| What to expect | | | | |
| What are the risks? | National data | `risk.cornea.cxl.example_risk` (see `evidence/uk/`) | | |
| When to get urgent help | Local details | This service's file in `sites/` | | |

Written by: Your name and role. AI assistance: none. Reviewed and approved by: (reviewer, date).
