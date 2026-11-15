# corneanotes

**Write it once, review it once, use it everywhere.**

## Why this exists

Every eye unit in the country writes its own patient leaflet for corneal cross-linking. And for corneal grafts, keratitis, dry eye, and every other common condition and operation. Each one is drafted, checked, approved by a committee, and then left to go out of date, separately, hundreds of times over.

The operation is the same everywhere. The condition is the same everywhere. The risks should be quoted from the same national data everywhere. What actually differs between hospitals is small: a phone number, how to get seen urgently, the trust logo, the house format.

This project stops us all doing the same work. The shared information is written once, reviewed by clinicians, kept current against national data, and then used by any service. Each service adds only its own local details.

It starts with corneal services in the UK, drawing on experience of setting up a cornea service. It is designed to grow across ophthalmology, then to other specialties, and internationally.

At this early stage it is maintained by a single clinician. Others are welcome to read it and suggest changes.

## How it works

**Shared core, local details.** Every document has a core (what the condition is, what the operation involves, what the risks are) that is reviewed centrally and is the same for everyone. Local details such as telephone numbers, urgent access instructions and out-of-hours arrangements go in placeholders, for example `{{site.contacts.urgent_phone}}`. These are filled from `sites/`, which holds local details at four levels (country, network, trust and hospital), each inheriting from the level above. A service can update its phone numbers without touching, or re-reviewing, the clinical content.

**One national figure, used everywhere.** Risk figures are not typed into individual leaflets. Each figure lives once in `evidence/` (for now `evidence/uk/`), with its source in national data or the published literature, the date it was last checked and when it is next due. Documents refer to it, for example `{{risk.cornea.cxl.example_risk}}`, so updating one figure updates every document that quotes it.

**Kept current.** Every document, figure and local formulary has a review date. A monthly check (`scripts/check_currency.py`, run by GitHub Actions) opens an issue listing anything overdue or due soon, any document quoting a figure that has changed since the document was last reviewed, and any reference to a figure that does not exist. A planned addition will also list new publications on each risk topic for a clinician to look at. Figures are only ever changed by a person, through a reviewed change, so there is a full record of who changed what, when, and on what evidence.

**Honest about where it came from.** Every document ends with a table showing, section by section, what it is based on (national data, published guidance or research, clinical experience, an adapted document, or AI-drafted text that was then checked), who checked it and when. Readers can see exactly how much weight each part will bear.

**Every change is reviewed.** Anyone can propose a change. Nothing is published until a trusted clinical reviewer for that area has approved it (see `.github/CODEOWNERS`).

> **Important:** this material supports, and does not replace, the judgement of the treating clinician. Check that any document fits your local policies before use.

See [ROADMAP.md](ROADMAP.md) for the documents planned so far, and [content/ophthalmology/cornea/README.md](content/ophthalmology/cornea/README.md) for how content is organised.

## What is here

| Folder | Contents |
|---|---|
| `content/<specialty>/<subspecialty>/conditions/<condition>/` | Everything for one condition or procedure: leaflet, consent, PIFU, video script, protocol, business case |
| `content/<specialty>/<subspecialty>/service/` | Things for the whole service: general patient information, training, business cases, medicines |
| `content/_template.md` | Starting point for a new document |
| `evidence/<country>/` | Risk and outcome figures, national prices, and the list of available eye preparations, each with its source and review date |
| `sites/` | Local details at four levels: country, network, trust, hospital |
| `src/` | The website |

## Suggesting a change

See [CONTRIBUTING.md](CONTRIBUTING.md). You do not need to know how to code: you can edit files directly on the GitHub website.

## How this repository was produced

The structure, governance files, templates and scripts in this repository were drafted with the help of an AI assistant (Claude, made by Anthropic), working to the maintainer's direction, and reviewed by the maintainer. Clinical content is labelled document by document in its own sources table.

## Licence

The content of this repository is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSE). You may share and adapt it for non-commercial purposes, as long as you give credit and share your adaptations under the same licence.

## Running the website locally

The site is a [Next.js](https://nextjs.org) app. It currently reads from Supabase and needs two environment variables in a `.env.local` file (never commit this file):

```
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
```

Then run `npm install` followed by `npm run dev`, and open <http://localhost:3000>.
