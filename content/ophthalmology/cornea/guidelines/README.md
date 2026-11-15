# Cornea guidelines

Guidelines here, for example on microbial keratitis, follow the shared-core, local-details model with one important difference: **antimicrobial drug choices are always local.**

## What is shared

- Clinical assessment and when to suspect infection
- Sampling and investigation (what to send, how, and when)
- Treatment principles, monitoring, and when to change or escalate treatment
- When to refer or seek specialist advice

## What is local

Drug choices, doses and regimens differ between areas because of local resistance patterns, sensitivities and formularies. They are set by each service with its own microbiology or antimicrobial stewardship team, and held in that service's `sites/` file under `formulary`.

Guidelines refer to them with placeholders, for example:

- `{{site.formulary.bacterial_keratitis.first_line}}`
- `{{site.formulary.bacterial_keratitis.alternative}}`

A guideline produced for a service shows that service's drugs, with its local approver and review date. The shared text never names a specific first-line drug.

## Adding an indication

Add the indication to the guideline with its placeholders, and add a matching block to `sites/_example.yaml` so services know what to fill in. Each service's local block needs sign-off from its own microbiology lead before use.
