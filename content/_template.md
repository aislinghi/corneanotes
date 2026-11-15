---
title: "Title of the document"
type: leaflet            # leaflet, consent, pifu, letter, video-script, protocol, guideline,
                         # referral, teaching, business-case, formulary-application, formulary-review
status: draft            # draft or approved (set by the reviewer)
version: 0.1
authors:
  - "Your name"
approved_by:             # filled in by the reviewer
last_reviewed:           # YYYY-MM-DD, filled in by the reviewer
next_review_due:         # YYYY-MM-DD
risks_used:              # keys from evidence/ quoted in this document
  - risk.cornea.cxl.example_risk
sources:
  - "Reference for any clinical statement not covered by evidence/"
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
