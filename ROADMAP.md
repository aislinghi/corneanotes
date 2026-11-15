# Roadmap

Documents planned so far, starting with cornea. Each is split into a shared core (the same for every service) and local details (filled from that service's file in `sites/`). Figures and national prices come from `evidence/`.

## Patient information

| Document | Shared core | Local details |
|---|---|---|
| Patient leaflets (per condition and procedure) | Condition, procedure, risks from `evidence/` | Contacts, urgent access, out of hours |
| Consent content (per procedure) | Procedure, risks from `evidence/` (same keys as the leaflet), alternatives | Trust consent form and sign-off stay with the trust |
| Patient-initiated follow-up (PIFU) information | What PIFU is, symptoms that mean getting in touch, when to seek urgent help instead | PIFU line, how to get in touch, response time, time on PIFU |
| Patient letters | Standard wording | Service details; patient details filled only in the patient record, never here |
| Video scripts | Approved script, captions and transcript | Recorded by the service's own clinicians; links in `sites/` |

## Clinical

| Document | Shared core | Local details |
|---|---|---|
| Keratoconus management protocol | Assessment, monitoring, treatment thresholds and pathway | Referral routes, clinic arrangements |
| Microbiology guidelines (e.g. microbial keratitis) | Sampling, investigation, evidence-based treatment principles | Antimicrobial choices must follow the local formulary and resistance data agreed with local microbiology (see `formulary` in `sites/`) |
| Shared list of antimicrobial eye preparations | Every available eye preparation (licensed, special, unlicensed) with source and check date; standard lab testing request | Which ones the service stocks |
| Referral guidance | When and how urgently to refer | Referral routes and contacts |

## Training

| Document | Shared core | Local details |
|---|---|---|
| Eye casualty training in cornea | Recognition and initial management of corneal presentations, when to escalate | Local escalation routes and on-call arrangements |

## Medicines

| Document | Shared core | Local details |
|---|---|---|
| Formulary applications for new medicines | Evidence review, national guidance status, licensing, place in pathway, national list price from `evidence/` | Committee format, local patient numbers, budget impact, supply arrangements |
| Formulary reviews | Standard review checklist: new evidence, safety alerts, guidance and price changes | Local usage, outcome and decision |

## Business cases

| Document | Shared core | Local details |
|---|---|---|
| Graft tissue | Clinical need, evidence, national tissue prices from `evidence/` | Local activity, current spend, service model |
| Amniotic membrane | Clinical indications, evidence, national prices from `evidence/` | Local activity, current spend |
| New equipment | Clinical rationale, evidence, equipment options | Local activity, quotes, estates and staffing |
| New training | Training need, curriculum, expected outcomes | Local staffing, backfill, costs |

## Supporting work

- Automated checks on every change (placeholders, evidence keys, no typed-in figures, no patient data, readability, review dates)
- Scheduled check for overdue reviews and new publications on each risk topic
- Word and PDF output in each trust's own template
- Version control for consent (permanent document IDs and tagged releases)
