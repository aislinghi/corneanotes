# Sites: local details

Local details are set at four levels. Each level inherits from the one above it, and a lower level overrides a higher one, so each file only holds what is genuinely different at that level.

| Level | Folder | Typically holds |
|---|---|---|
| Country | `sites/countries/` | Which national evidence set to use (`evidence/<country>/`), nation within the UK |
| Network | `sites/networks/` | Shared arrangements across trusts, e.g. regional cornea network, shared microbiology lab and antimicrobial formulary |
| Trust | `sites/trusts/` | House document format, consent policy, trust formulary, governance contacts |
| Hospital or clinic | `sites/hospitals/` | Phone numbers, urgent access, out of hours, PIFU line, which eye drops are stocked, video links |

Each file names its parent(s): a hospital names its trust, a trust names its country and any networks it belongs to. A trust can belong to more than one network (for example a cornea network and a different microbiology network). Where two networks set the same detail, the trust file must say which applies.

When a document is produced for a hospital, every `{{site.*}}` placeholder is filled from the hospital file, then its trust, then its networks, then its country, using the first value found.

## Adding your service

Copy the `_example.yaml` file at each level you need (most services need a hospital file and a trust file; the network and country files may already exist), rename it (lower case, hyphens) and open a pull request.

## Rules

- Only information that is already public: published department numbers, not personal mobiles.
- Nothing about patients.
- No commercially confidential information, such as local contract prices or supplier quotes. This repository is public.
