# Cornea

Content is grouped in two ways.

## `conditions/`

One folder per condition or procedure. Everything about it sits together, so documents that must agree are reviewed together:

```
conditions/keratoconus/
  leaflet-corneal-cross-linking.md
  consent-corneal-cross-linking.md
  pifu.md
  video-script-corneal-cross-linking.md
  protocol-keratoconus-management.md
  business-case-corneal-cross-linking.md
```

When a risk figure in `evidence/` changes, every document in the folder that quotes it is updated and checked in the same change.

## `service/`

Things for the whole cornea service that belong to no single condition:

| Folder | Contents |
|---|---|
| `service/patient-information/` | General patient information, e.g. what patient-initiated follow-up (PIFU) is |
| `service/training/` | e.g. eye casualty training in cornea |
| `service/business-cases/` | e.g. new equipment, graft tissue, amniotic membrane, new training |
| `service/medicines/` | Formulary applications and reviews for medicines |

## Document types

Every file states its type at the top, so the website can list all documents of one type across conditions:

`leaflet`, `consent`, `pifu`, `letter`, `video-script`, `protocol`, `guideline`, `referral`, `teaching`, `business-case`, `formulary-application`, `formulary-review`

Name files `<type>-<topic>.md` in lower case with hyphens, for example `leaflet-corneal-cross-linking.md`.
