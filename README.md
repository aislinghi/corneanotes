# corneanotes

**Write it once, review it once, use it everywhere.**

## Why this exists

Every eye unit in the country writes its own patient leaflet for corneal cross-linking. And for corneal grafts, keratitis, dry eye, and every other common condition and operation. Each one is drafted, checked, approved by a committee, and then left to go out of date, separately, hundreds of times over.

The operation is the same everywhere. The condition is the same everywhere. The risks should be quoted from the same national data everywhere. What actually differs between hospitals is small: a phone number, how to get seen urgently, the trust logo, the house format.

This project stops us all doing the same work. The shared information is written once, reviewed by clinicians, kept current against national data, and then used by any service. Each service adds only its own local details.

It starts with corneal services in the UK. It is designed to grow across ophthalmology, then to other specialties, and internationally.

## How it works

**Shared core, local details.** Every document has a core (what the condition is, what the operation involves, what the risks are) that is reviewed centrally and is the same for everyone. Local details such as telephone numbers, urgent access instructions and out-of-hours arrangements go in placeholders, for example `{{site.urgent_phone}}`, which each service fills in from its own file in `sites/`. A service can update its phone numbers without touching, or re-reviewing, the clinical content.

**One national figure, used everywhere.** Risk figures are not typed into individual leaflets. Each figure lives once in `evidence/`, with its source in national data or the published literature, the date it was last checked and when it is next due. Documents refer to it, for example `{{risk.cornea.cxl.example_risk}}`, so updating one figure updates every document that quotes it.

**Kept current.** Every document and every figure has a review date. The plan is a scheduled check that flags anything overdue and lists new publications on each risk topic for a clinician to look at. Figures are only ever changed by a person, through a reviewed change, so there is a full record of who changed what, when, and on what evidence.

**Every change is reviewed.** Anyone can propose a change. Nothing is published until a trusted clinical reviewer for that area has approved it (see `.github/CODEOWNERS`).

> **Important:** this material supports, and does not replace, the judgement of the treating clinician. Check that any document fits your local policies before use.

## What is here

| Folder | Contents |
|---|---|
| `content/<specialty>/<subspecialty>/leaflets/` | Patient information leaflets |
| `content/<specialty>/<subspecialty>/protocols/` | Clinical protocols and pathways for staff |
| `content/<specialty>/<subspecialty>/referral/` | Referral guidance for optometrists, GPs and other units |
| `content/<specialty>/<subspecialty>/teaching/` | Training material |
| `content/_template.md` | Starting point for a new document |
| `evidence/` | Risk and outcome figures, each with its source and review date |
| `sites/` | Each service's local details (phones, urgent access, format) |
| `src/` | The website |

## Suggesting a change

See [CONTRIBUTING.md](CONTRIBUTING.md). You do not need to know how to code: you can edit files directly on the GitHub website.

## Licence

The content of this repository is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSE). You may share and adapt it for non-commercial purposes, as long as you give credit and share your adaptations under the same licence.

## Running the website locally

The site is a [Next.js](https://nextjs.org) app. It currently reads from Supabase and needs two environment variables in a `.env.local` file (never commit this file):

```
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
```

Then run `npm install` followed by `npm run dev`, and open <http://localhost:3000>.
