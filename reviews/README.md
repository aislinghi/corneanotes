# Reviews: keeping content current

Every evidence figure and approved document has a review date. When one is due, it is reviewed by AI. If nothing has changed, the AI review alone renews it. If something has changed, the AI proposes the change and a person approves it.

## How a review runs

Monthly, the **AI review** workflow (`.github/workflows/ai-review.yml`):

1. Finds everything due for review (`scripts/check_currency.py`).
2. Runs the **screen** for each one (`scripts/screen_literature.py`): the PubMed searches and national sources for its topic in `reviews/screen/`, limited to what has appeared since it was last reviewed.
3. Asks the AI reviewer to assess the results, following [AI_REVIEW_INSTRUCTIONS.md](AI_REVIEW_INSTRUCTIONS.md). Each subject gets one of three outcomes:

| Outcome | What happens |
|---|---|
| **No change** | A review record is saved and the next review date moves on. No person checks it. Displayed as "Reviewed by AI on [date], no change found, not checked by a person". |
| **Change proposed** | The AI edits the figure or document and a pull request is opened, listing the evidence and every document affected. A person must approve it. |
| **Needs a person** | The AI could not reach a safe conclusion (no screen topic, results cut off, a source could not be opened, conflicting evidence). An issue is opened. |

The AI never approves a change to clinical content. It can only renew a review date when it finds no change, and every such renewal is recorded with exactly what was searched.

## Where review records are kept

Review records are kept on a separate branch, `review-records`, in `reviews/records/`. This lets "no change" reviews be saved without a pull request, while every change to clinical content on `main` still needs approval. The currency check and the website read the latest record for each subject.

## Reporting something the review missed

Anyone can report a paper, dataset or guideline the review should have found, using the **Something the review missed** issue form. When confirmed:

1. It is added to `reviews/missed/` as a permanent test case (copy `_example.yaml`).
2. The topic's searches or national sources in `reviews/screen/` are changed so it is found.
3. The **screen test** (`python3 scripts/screen_literature.py test`) must pass: every item ever reported as missed must be found by the current screen. It runs on every pull request that changes the screen, so a later change can never quietly reintroduce an old miss.
4. If the missed item changes a figure or document, that change goes through a pull request in the usual way.

Over time this makes the screen more complete. It cannot guarantee that nothing is ever missed, which is why reporting misses matters.

## Screen topics

Each file in `reviews/screen/` is one topic: which evidence keys and documents it covers, its PubMed searches, and the national sources to check. Copy `_example.yaml` to add a topic. A subject due for review with no topic is never passed as "no change": it goes to a person.
