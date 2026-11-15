# Microbial keratitis

Guidelines here follow the shared-core, local-details model with one important difference: **antimicrobial drug choices are always local.**

## What is shared

- Clinical assessment and when to suspect infection
- Sampling and investigation (what to send, how, and when)
- Treatment principles, monitoring, and when to change or escalate treatment
- When to refer or seek specialist advice

## Shared list of eye preparations

`evidence/uk/ophthalmology/cornea/ophthalmic-antimicrobials.yaml` lists the antimicrobial eye preparations actually available (licensed, specially manufactured and unlicensed), each with its source and check date. It is used for two things:

1. **Lab testing.** A standard request to each local microbiology lab to test isolates against the agents available as eye preparations, so sensitivity results are useful for topical treatment, not only for the systemic panel.
2. **Local choice.** Each service picks its drugs from this list (each hospital's `formulary.stocked` list in `sites/hospitals/`), so local choices always map to something that exists.

## What is local

Drug choices, doses and regimens differ between areas because of local resistance patterns, sensitivities and formularies. They are set by each service with its own microbiology or antimicrobial stewardship team, and held under `formulary` in the `sites/` file for that area (usually a network or trust, since microbiology is often shared across trusts).

Guidelines refer to them with placeholders, for example:

- `{{site.formulary.bacterial_keratitis.first_line}}`
- `{{site.formulary.bacterial_keratitis.alternative}}`

A guideline produced for a service shows that service's drugs, with its local approver and review date. The shared text never names a specific first-line drug.

## Adding an indication

Add the indication to the guideline with its placeholders, and add a matching block to `sites/networks/_example.yaml` so areas know what to fill in. Each local block needs sign-off from its own microbiology lead before use.
