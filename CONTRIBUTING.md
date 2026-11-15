# Contributing to corneanotes

Thank you for helping improve these leaflets and protocols. Contributions from clinicians, allied health professionals, patients and carers are all welcome.

## The golden rules

1. **No patient-identifiable information, ever.** No names, dates of birth, hospital or NHS numbers, photographs, or case details that could identify someone. This repository is public and its history is permanent: anything pushed can be seen even after it is deleted.
   An automatic patient data check runs on every push and pull request and blocks merging if it finds anything that looks like patient data. It cannot catch everything, and it cannot un-publish something already pushed, so check before you commit. You can run the same check on your own computer: `python3 scripts/check_patient_data.py`.
2. **Every change is reviewed.** Nothing reaches the main branch without approval from a trusted reviewer (listed in `.github/CODEOWNERS`).
3. **Same information everywhere.** The clinical core of a document is shared by every service. Local details (phone numbers, urgent access, out-of-hours arrangements) go in placeholders filled from `sites/`, never in the shared text.
4. **National figures, kept in one place.** Never type a risk figure into a document. Add or update it in `evidence/uk/` with its national or published source, and refer to it by its key. See [evidence/README.md](evidence/README.md).
5. **Be honest about how it was produced.** Every document ends with a "Sources and how this document was produced" table showing, section by section, what it is based on: national data, a published guideline or research, clinical experience (expert opinion), another document it was adapted from, or an AI-drafted text that was then checked. Say who checked it and when. If you use AI help, say so and say what for. If you adapt someone else's document, name it and make sure its licence or the owner's permission allows it.
6. **Write it fresh.** Do not copy wording from another organisation's leaflets or guidance, including documents you wrote for your employer, unless the owner has agreed in writing to publication under this repository's licence. Use them as a checklist of what to cover, and write new text from the published sources.
7. **Write for the reader.** Leaflets are for patients: plain English, short sentences, and explain any medical term you have to use.

## How to suggest a change

### On the GitHub website (no coding needed)

1. Open the file you want to change, or `content/_template.md` to start a new one.
2. Click the pencil icon ("Edit this file"). GitHub will make your own copy (a "fork") automatically.
3. Make your changes and click **Commit changes**, then **Propose changes**.
4. Click **Create pull request** and fill in the checklist.

### With git

1. Fork the repository and create a branch.
2. Make your changes and push to your fork.
3. Open a pull request against `main`.

## What happens next

A reviewer will read your pull request. They may approve it, ask questions, or request changes. Once approved it is merged and becomes part of the published content. If you push further changes after approval, it will need approving again.

## Adding a new document

1. Copy `content/_template.md` into the right folder, for example `content/ophthalmology/cornea/conditions/keratoconus/`, or the `service/` folder if it belongs to no single condition.
2. Name it `<type>-<topic>.md` in lower case with hyphens, for example `leaflet-corneal-cross-linking.md`.
3. Fill in the details at the top of the file (the part between the `---` lines) and write the content underneath.
4. Leave `status` as `draft`. The reviewer changes it to `approved`.

## Adding your service

Copy the `_example.yaml` file at each level you need in `sites/` (usually a hospital file and a trust file), fill in your local details and open a pull request. See [sites/README.md](sites/README.md).

## Starting a new specialty or subspecialty

Open an issue first. A new area needs a lead reviewer, who is added to `.github/CODEOWNERS` for that area's folders.

## Licence

By contributing, you agree that your contribution is licensed under the same licences as the rest of the repository: content under [CC BY 4.0](LICENSE) and code under the [MIT License](LICENSE-CODE). This means anyone may reuse your contribution for any purpose, including commercial use such as a private practice website, as long as they credit the source. Only contribute material you have the right to license in this way.
