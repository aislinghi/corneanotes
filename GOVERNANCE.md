# Governance

This document sets out how corneanotes is run: who decides what, how content is approved and kept current, and what users of the material are responsible for.

**Status: draft.** Items marked **[To confirm]** are proposals awaiting the maintainer's decision.

## 1. Purpose

corneanotes exists to stop clinical services repeating the same work. Standard information about a condition or operation is written once, reviewed once, kept current against national data, and shared openly for anyone to use. Services add only their own local details.

## 2. Scope

**In scope:** patient information leaflets, consent content, patient-initiated follow-up (PIFU) information, letter templates, video scripts, clinical protocols and guidelines, referral guidance, training material, business case templates, formulary application and review templates, and the evidence and national figures these rely on.

**Out of scope:**

- Any information about individual patients.
- Advice for an individual patient. The material is general information, not a substitute for assessment by a clinician.
- Tools that take information about a patient and produce a recommendation for that patient. Such tools may fall within medical device regulation and would need a separate, deliberate decision before being added.
- Commercially confidential information, such as local contract prices or supplier quotes.

## 3. Status and maintainership

corneanotes is currently maintained by a single clinician, drawing on their experience of setting up a corneal service. It is produced in a personal capacity and does not represent the views or policies of any employer or organisation. **[To confirm wording]**

The long-term aim is for ownership to pass to, or be shared with, a professional body or clinical network. Material already published remains available under its licence whatever happens to ownership.

## 4. Roles

| Role | Who | Responsibilities |
|---|---|---|
| Maintainer | The repository owner | Overall direction, governance, final say on disputes, approving changes to governance files |
| Area reviewer | Named in `.github/CODEOWNERS` for each area (currently the maintainer for all areas) | Reviewing and approving changes to content and evidence in their area |
| Contributor | Anyone | Proposing changes through pull requests, following [CONTRIBUTING.md](CONTRIBUTING.md) |
| Adopting service | Any service using the material | Local approval, local details, and use in their own setting (see section 10) |

New area reviewers are appointed by the maintainer. A reviewer should be a clinician with relevant expertise who has made a declaration of interests (section 8).

## 5. How content is approved

1. Every change is made through a pull request. Nothing reaches the main branch without approval from the area reviewer.
2. A reviewer must not approve their own change. While there is a single maintainer, the maintainer's own changes are merged without a second reviewer, and this is recorded in the document's sources table ("Reviewed and approved by"). **[To confirm: seek an independent clinical reviewer for patient-facing documents as soon as one is available]**
3. A document has one of three statuses:
   - `draft`: not yet approved; must not be used with patients.
   - `approved`: reviewed and approved for use.
   - `withdrawn`: no longer to be used, with the reason stated at the top of the document.
4. Every approved document records its version, who approved it, when, and when it is next due for review.

## 6. Evidence standards

Clinical statements are based on the best available evidence, in this order of preference:

1. National data (national registries, audits and published national statistics)
2. National or professional body guidelines
3. Systematic reviews and large published studies
4. Other published research
5. Clinical experience (expert opinion), clearly labelled as such

Risk figures, outcome figures and national prices are held once in `evidence/`, with their source, the exact location in the source, and the dates they were last changed and checked. Documents refer to them and never type them in. Local unit figures are not used in shared content.

Antimicrobial drug choices are the exception to "the same everywhere": they are set locally with each area's microbiology team, because resistance patterns and formularies differ. The shared content covers principles, and the shared list of available eye preparations.

## 7. Transparency about how content is produced

1. Every document ends with a "Sources and how this document was produced" table, showing for each section what it is based on, who checked it and when.
2. **Use of AI.** AI tools may be used to help draft or edit content. Where they are:
   - this is stated in the document's sources table, with what the AI was used for;
   - every statement is checked by a named person against its source before approval;
   - AI is never treated as a source in its own right.
3. Material adapted from another document is credited, and is only included if its licence or the owner's permission allows reuse under this repository's licences.

## 8. Conflicts of interest

Reviewers, and contributors making substantial clinical contributions, declare any interest that a reasonable person might think could influence their judgement, such as payments, grants, shares or advisory roles with companies making devices, drugs or tissue products relevant to the content, or with organisations that might use or sell the material. Declarations are recorded in [DECLARATIONS.md](DECLARATIONS.md) and updated at least annually. A reviewer with a relevant interest does not approve changes it affects.

## 9. Keeping content current

1. Every approved document, evidence figure and local formulary has a next review date. **[To confirm default intervals. Proposal: documents every 2 years; risk figures and national prices every year; local formularies as set by local microbiology]**
2. A monthly automated check opens an issue listing anything overdue or due soon, any document quoting a figure that has changed since the document was last reviewed, and any missing review dates or sources tables.
3. Automated checks never change content. Changes are made by people, through reviewed pull requests.
4. A document that is overdue for review by more than **[To confirm: 6 months]** is marked as overdue wherever it is displayed.

## 10. Responsibilities of adopting services

Anyone may use this material, including commercially, as long as they credit the source (see the licence). When a service adopts it, that service:

- is responsible for checking the material is appropriate for its patients and setting;
- obtains any local approval it needs (for example a patient information panel, consent policy, or medicines committee);
- is responsible for the accuracy of its own local details;
- is responsible for keeping its copy current, or for using a version that updates automatically;
- must not suggest that the maintainer or reviewers endorse its service.

The material is provided as is, without warranty, as set out in the licence.

## 11. Corrections and safety concerns

- **Errors and suggestions:** open an issue or a pull request.
- **Safety concerns** (something that could harm a patient if followed): open an issue with "Safety" at the start of the title. Safety issues are looked at before any other work. If confirmed, the document is corrected or marked `withdrawn` straight away, and the change is recorded. **[To confirm target response time, e.g. 7 days]**
- If a concern cannot be raised publicly, contact the maintainer through their GitHub profile.

## 12. Personal data

The repository holds no patient data. An automatic check runs on every push and pull request and blocks merging if anything looks like patient data (NHS, CHI or Health and Care numbers, dates of birth, hospital numbers, patient names, mobile numbers, and files that cannot be scanned such as images and PDFs). Exceptions for false positives must be marked in the file and are visible to the reviewer. If patient data is ever pushed, the maintainer is told at once, the data is removed from the repository history, and GitHub is asked to purge cached copies. The only personal data held is the names, roles and declarations that contributors and reviewers choose to provide. Site files contain only information that services already publish, such as department phone numbers.

## 13. Accessibility and inclusion

Patient-facing material is written in plain English, and alternative formats (easy read, large print, translations) are produced where possible. Translations are credited and checked like any other content.

## 14. Licences

Content is licensed under [CC BY 4.0](LICENSE) and code under the [MIT License](LICENSE-CODE). Licences already granted cannot be withdrawn.

## 15. Changing this document

Changes to this governance document are made by pull request and approved by the maintainer. Significant changes are noted in the pull request description.
