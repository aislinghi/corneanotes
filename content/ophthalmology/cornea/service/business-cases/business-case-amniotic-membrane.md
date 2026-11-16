---
title: "Business case: amniotic membrane service for the ocular surface"
type: business-case
status: draft
version: 0.1
authors:
  - "corneanotes maintainer"
approved_by:
last_reviewed:
next_review_due:
risks_used:
  - cost.cornea.amniotic_membrane.dehydrated_application
  - cost.cornea.amniotic_membrane.ped_standard_care_cost
  - cost.cornea.amniotic_membrane.ped_dehydrated_pathway_cost
  - cost.cornea.amniotic_membrane.theatre_cost_per_minute
  - risk.cornea.amniotic_membrane.ped_standard_care_healed
  - risk.cornea.amniotic_membrane.ped_dehydrated_healed
production:
  written_by: "corneanotes maintainer"
  ai_assistance: "Drafted by an AI assistant from the published sources listed, after each quoted figure and statement was checked against the original. To be reviewed line by line by the maintainer before approval."
  based_on_template: "Structure follows HM Treasury's Five Case Model. No wording copied from other organisations' business cases."
---

This is a template business case for setting up, or extending, an amniotic membrane service in a hospital eye department. The national sections (evidence, regulation, supply and published costs) are shared. The local sections are filled in from each unit's file in `sites/`, and each unit should add its own activity data and price quotes before submitting it. It follows HM Treasury's Five Case Model, the standard framework for public sector business cases [1]. Keep it in proportion: a small service change needs a short case [1].

## 1. Summary

{{site.business_cases.amniotic_membrane.proposal}}

{{site.business_cases.amniotic_membrane.expected_activity}}

**Clinical lead:** {{site.business_cases.amniotic_membrane.clinical_lead}}

## 2. Strategic case

### 2.1 What amniotic membrane is used for

Amniotic membrane is a thin tissue from the placenta, donated after planned caesarean births [2]. In eye care it is placed on the surface of the eye to protect it and help it heal. Common uses include:

- persistent epithelial defects (surface wounds that will not heal) and surface inflammation [3]
- chemical injuries to the eye [4]
- severe infections of the cornea, alongside antimicrobial treatment [5]
- neurotrophic keratitis (loss of feeling in the cornea) [6]
- as a graft after removing a pterygium, although a graft of the patient's own conjunctiva gives fewer recurrences [7]

### 2.2 What the evidence shows

The evidence is mixed and mostly of low certainty. A business case should not overstate it.

- **Chemical injuries:** there is uncertain evidence of benefit in moderate burns, and no clear benefit has been shown in severe burns [4].
- **Infectious keratitis:** adding amniotic membrane shortened the time to healing, but the evidence was of low quality [5].
- **Neurotrophic keratitis:** amniotic membrane may make little or no difference to healing compared with eyelid closure or a bandage contact lens (very low-certainty evidence) [6].
- **Pterygium:** a conjunctival graft is associated with a lower risk of recurrence at six months than amniotic membrane [7].
- **Persistent epithelial defects:** in a UK study, standard care fully healed about {{risk.cornea.amniotic_membrane.ped_standard_care_healed}} patients, with long treatment, many clinic visits and an average cost of about {{cost.cornea.amniotic_membrane.ped_standard_care_cost}} per patient. Clinic-applied dehydrated amniotic membrane was associated with a higher healing rate (about {{risk.cornea.amniotic_membrane.ped_dehydrated_healed}}) and fewer visits. This study compared against earlier data, and its authors were funded by the manufacturer [3].

### 2.3 Current service

{{site.business_cases.amniotic_membrane.current_service}}

Conventional amniotic membrane grafting needs operating theatre time and surgical costs, which can delay early treatment [3].

### 2.4 Case for change and objectives

Suggested objectives (make them specific, measurable and time-limited for your unit [1]):

- reduce the time from decision to amniotic membrane treatment
- move suitable cases from theatre to clinic
- reduce clinic visits and theatre use for persistent epithelial defects
- meet Human Tissue Authority (HTA) requirements for storage and traceability

## 3. Economic case

### 3.1 Options

| Option | Description |
|---|---|
| 1. Do nothing | Keep the current service. |
| 2. Theatre only, frozen membrane | Frozen amniotic membrane from NHS Blood and Transplant, stitched or glued in theatre. |
| 3. Clinic only, dehydrated membrane | A dehydrated amniotic membrane applied in clinic under a carrier lens or ring. |
| 4. Both (usually preferred) | Clinic-applied membrane for suitable cases, keeping theatre-based frozen membrane for cases that need it. |

### 3.2 Two types of product

- **Frozen amniotic membrane (NHS Blood and Transplant).** Supplied frozen in glycerol, in 2 x 2 cm, 3 x 3 cm and 5 x 5 cm sizes [2]. It must be kept in a dedicated, alarmed freezer, and NHSBT sets its expiry date according to the freezer temperature [8].
- **Dehydrated amniotic membrane.** For example, Omnigen is shipped and stored between 2°C and 25°C [9], and can be stored for up to 60 weeks [10]. It is applied in clinic under a carrier lens. The lens (OmniLenz) is CE marked [11]. Clinic application is recorded with two NHS procedure codes: C46.6 (amniotic membrane graft to cornea) and C51.5 (placement of a therapeutic contact lens) [11].

### 3.3 Costs

NHS Blood and Transplant does not publish its tissue prices online; ask Tissue and Eye Services for a current price list [2].

Published UK figures, from one cost study [3]:

| Item | Figure |
|---|---|
| One clinic application of dehydrated membrane with its lens, including postage | {{cost.cornea.amniotic_membrane.dehydrated_application}} |
| Average cost per patient of standard care for a persistent epithelial defect | {{cost.cornea.amniotic_membrane.ped_standard_care_cost}} |
| Modelled average cost per patient with clinic-applied dehydrated membrane, including follow-up | {{cost.cornea.amniotic_membrane.ped_dehydrated_pathway_cost}} |
| Theatre time used in the model, per minute | {{cost.cornea.amniotic_membrane.theatre_cost_per_minute}} |

**Cautions about these figures.** They come from one study at two UK centres. Its authors were funded by the manufacturer. Costs for clinic-applied membrane were modelled against earlier data rather than measured side by side, and unit costs were based on 2017 NHS Reference Costs [3]. Replace them with your own unit's costs where you can.

{{site.business_cases.amniotic_membrane.product_price}}

### 3.4 Benefits

- Earlier treatment without waiting for theatre [3].
- Fewer clinic visits and shorter treatment for persistent epithelial defects, if the published results apply to your patients [3].
- Theatre time released for other operations.

## 4. Commercial case

- **NHS Blood and Transplant.** Tissue is supplied only to UK hospitals, and only to a named registered healthcare professional [12]. Supply needs a signed service level agreement and an order number, and NHSBT charges on a cost-recovery basis [12]. One agreement can cover several departments [12].
- **Commercial products.** Agree supply, delivery and storage terms with the supplier. A supplier of tissue must have agreements with end users about traceability and reporting of serious adverse events and reactions [13].

## 5. Financial case

{{site.business_cases.amniotic_membrane.funding}}

Include in your finance appendix: tissue and lens costs per case, delivery charges, any freezer or storage costs, staff time, and the expected savings in theatre time and clinic visits.

## 6. Management case

### 6.1 Regulation: Human Tissue Authority

- Amniotic membrane is human tissue. Storing tissue for human use for **more than 48 hours** needs a licence under the Human Tissue (Quality and Safety for Human Application) Regulations 2007 [14, 15]. Storage for less than 48 hours, for use in transplantation, is exempt [16].
- This applies to dehydrated products too. The HTA found that several unlicensed hospitals had stored Omnigen for longer than 48 hours [10]. Tissue products are not covered by the UK medical devices regulations [17].
- Many hospitals use their blood transfusion laboratory, which may already hold a licence and suitable freezers [8, 18].

{{site.business_cases.amniotic_membrane.storage}}

### 6.2 Traceability and safety reporting

- Hospitals must complete the audit trail for each piece of tissue, from receipt to use or disposal [18].
- Record the donation or batch number and product code in the patient's notes [18].
- Traceability data must be kept for at least 30 years after use [13].
- End users must report any serious adverse reaction or event to the supplying tissue establishment within 24 hours [13].

### 6.3 Staffing and training

{{site.business_cases.amniotic_membrane.staffing}}

Agree training and competency sign-off before staff apply amniotic membrane in clinic.

### 6.4 Patient information

Use the amniotic membrane patient leaflet in `conditions/ocular-surface-disease/`.

### 6.5 Audit and benefits tracking

Record for each case: indication, product, setting (clinic or theatre), time from decision to treatment, healing, number of applications, clinic visits, complications and costs. Report after 12 months.

### 6.6 Risks

| Risk | Mitigation |
|---|---|
| Storing tissue for more than 48 hours without an HTA licence | Store under an existing licence (for example the transfusion laboratory), or order for use within 48 hours [10, 14] |
| Loss of traceability | Use a tissue register, and record batch numbers in the notes [18] |
| Freezer failure | Use a dedicated alarmed freezer monitored 24 hours a day [8] |
| Benefits smaller than predicted | Audit outcomes and costs, and review after 12 months |
| Infection after application | Follow-up arrangements and patient information on warning signs |

## Sources and how this document was produced

| Section | Based on | References | Checked by | Date checked |
|---|---|---|---|---|
| Structure | HM Treasury guidance | [1] | AI assistant, quotes checked against source | 2026-11-16 |
| Uses and evidence | Cochrane reviews; systematic review; UK published research | [3, 4, 5, 6, 7] | AI assistant, quotes checked against source | 2026-11-16 |
| Products and supply | NHS Blood and Transplant; manufacturer information; HTA inspection report | [2, 8, 9, 10, 11, 12] | AI assistant, quotes checked against source | 2026-11-16 |
| Costs | UK published cost study (manufacturer-funded) | [3] | AI assistant, quotes checked against source | 2026-11-16 |
| Regulation, traceability, reporting | Legislation; Human Tissue Authority guidance; NHS Blood and Transplant | [13, 14, 15, 16, 17, 18] | AI assistant, quotes checked against source | 2026-11-16 |
| Local service, activity, storage, staffing, funding, prices | Local details | This service's file in `sites/` (`business_cases.amniotic_membrane`) | | |

All national cost figures are held in `evidence/uk/ophthalmology/cornea/costs.yaml`, and outcome figures in `evidence/uk/ophthalmology/cornea/risks.yaml`, with the exact quotation and location in each source.

Written by: corneanotes maintainer. AI assistance: drafted by an AI assistant from the sources listed, with every figure checked against the original source. Reviewed and approved by: not yet reviewed.
Latest routine review: shown automatically from the review records.

## References

1. HM Treasury. Guidance on developing business cases for projects and programmes (Five Case Model). Updated June 2026. [Link](https://www.gov.uk/government/publications/guidance-on-developing-business-cases)
2. NHS Blood and Transplant, Tissue and Eye Services. Amniotic membrane. [Link](https://www.nhsbt.nhs.uk/tissue-and-eye-services/products/eyes/amniotic-membrane/)
3. Maqsood SE, Posnett JW, Elalfy M. Management of ocular surface disease involving inflammation and persistent epithelial defects utilising various treatment modalities in the UK NHS. Eye (Lond). 2026;40(11):1627-1636. Funded by a NuVision fellowship grant. [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC13415519/)
4. Clare G, Bunce C, Tuft S. Amniotic membrane transplantation for acute ocular burns. Cochrane Database Syst Rev. 2022;CD009379. [Link](https://pubmed.ncbi.nlm.nih.gov/36047788/)
5. Ting DSJ, Henein C, Said DG, Dua HS. Amniotic membrane transplantation for infectious keratitis: a systematic review and meta-analysis. Sci Rep. 2021;11:13007. [Link](https://pubmed.ncbi.nlm.nih.gov/34155280/)
6. Kruoch Z, Choo AY, Kemp A, Gonzales M, et al. Medical and surgical interventions for neurotrophic keratopathy. Cochrane Database Syst Rev. 2025;12:CD015723. [Link](https://pubmed.ncbi.nlm.nih.gov/41347649/)
7. Clearfield E, Muthappan V, Wang X, Kuo IC. Conjunctival autograft for pterygium. Cochrane Database Syst Rev. 2016;(2):CD011349. [Link](https://pubmed.ncbi.nlm.nih.gov/26867004/)
8. NHS Blood and Transplant, Tissue and Eye Services. Storing tissue safely. [Link](https://www.nhsbt.nhs.uk/tissue-and-eye-services/support/storing-tissue-safely/)
9. NuVision Biotherapies. Omnigen (manufacturer information). [Link](https://www.nu-vision.co.uk/omnigen/)
10. Human Tissue Authority. Inspection report: NuVision Biotherapies Ltd (licence 22656), inspected 11 January 2023, final report 24 February 2023. Published on the HTA website (direct link not stable; search HTA inspection reports for licence 22656). [Link](https://www.hta.gov.uk/guidance-professionals/regulated-sectors/human-application)
11. NuVision Biotherapies. OmniLenz (manufacturer information). [Link](https://www.nu-vision.co.uk/omnilenz/)
12. NHS Blood and Transplant, Tissue and Eye Services. New customers. [Link](https://www.nhsbt.nhs.uk/tissue-and-eye-services/support/new-customers/)
13. Human Tissue Authority. Guide to quality and safety assurance for human tissues and cells for patient treatment. January 2021. [Link](https://www.hta.gov.uk/sites/default/files/2021-06/HTA%20guide%20to%20Quality%20and%20Safety%20Assurance%20for%20Human%20Tissue%20and%20Cells%20for%20Patient%20Treatment%20-%20Jan%202021.pdf)
14. The Human Tissue (Quality and Safety for Human Application) Regulations 2007 (SI 2007/1523), regulation 7. [Link](https://www.legislation.gov.uk/uksi/2007/1523/regulation/7)
15. The Human Tissue (Quality and Safety for Human Application) Regulations 2007 (SI 2007/1523), regulation 5 (definition of storage). [Link](https://www.legislation.gov.uk/uksi/2007/1523/regulation/5)
16. Human Tissue Authority. Licensing exemptions. [Link](https://www.hta.gov.uk/guidance-professionals/licensing/licensing-exemptions)
17. The Medical Devices Regulations 2002 (SI 2002/618), regulation 3(d). [Link](https://www.legislation.gov.uk/uksi/2002/618/regulation/3)
18. NHS Blood and Transplant, Tissue and Eye Services. Tissue tracking. [Link](https://www.nhsbt.nhs.uk/tissue-and-eye-services/support/tissue-tracking/)
