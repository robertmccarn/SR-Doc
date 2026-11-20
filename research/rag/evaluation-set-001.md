# Initial RAG evaluation set — authoring template

**Status:** Seed question set; not yet scored. Expected evidence page IDs and answer keys must be completed from source review before evaluation.

| ID | Category | Question | Expected behavior / pitfall |
|---|---|---|---|
| Q01 | Direct fact | What is the stated capital of the People's Republic of China? | Retrieve exact page passage and cite it; do not use real-world knowledge. |
| Q02 | Direct fact | What dates does the United Federation of China page give for its existence? | Quote the page's stated dates; distinguish page claim from historical consistency. |
| Q03 | Direct fact | What is the stated duration of the Third Chinese Civil War? | Retrieve the conflict page and cite its dates. |
| Q04 | Direct fact | Who is listed as the head of state of [choose a documented country]? | Resolve the exact page and relevant infobox field. |
| Q05 | Direct fact | What does the Lost Decade (China) page say happened to China? | Summarize only supported text; avoid filling its narrative gaps. |
| Q06 | Entity resolution | Is "UFC" an alias for the United Federation of China in the captured corpus? | Distinguish an explicit alias from a contextual abbreviation. |
| Q07 | Entity resolution | Which page does the redirect [choose verified redirect] resolve to? | Follow captured redirect evidence; do not infer identity from similar titles. |
| Q08 | Entity resolution | Are [two similar named entities] the same entity? | Require explicit identity evidence; otherwise retain ambiguity. |
| Q09 | Timeline | When did the Second Chinese Civil War occur according to its infobox? | Report 2027–2048 and separately surface the incompatible combatant dates. |
| Q10 | Timeline | What dates are given for the Third Chinese Civil War? | Report source dates and distinguish phases if stated. |
| Q11 | Timeline | What is the documented relationship between the UFC and Federal Republic of China periods? | Surface the 2108 overlap and missing transition explanation; no invented succession. |
| Q12 | Relationship | Which entities are listed as combatants in [choose conflict page]? | Use source infobox fields; label structured extraction as derived and cite source. |
| Q13 | Relationship | Which office does [choose officeholder] hold, and in which entity? | Require exact linked infobox fields and source text. |
| Q14 | Relationship | What predecessor/successor relationships are explicitly documented for [choose entity]? | Preserve predicate direction and verify each edge against source passage. |
| Q15 | Contradiction | Why does the Second Chinese Civil War page include 2105–2111 among combatant dates despite its 2027–2048 infobox dates? | Present both claims; do not resolve without evidence. |
| Q16 | Contradiction | How do the UFC and Federal Republic of China pages describe the 2108 transition? | Report the overlapping dates and absence of a documented transition; no invented explanation. |
| Q17 | Contradiction | What historical dates appear in the modern Chinese-state infoboxes? | Identify stale 1911–1949 event data and explain source-level inconsistency. |
| Q18 | Abstention | What was the exact territorial boundary of the Federal Republic of China in 2120? | Abstain unless a captured map or passage establishes it; missing map is not a boundary. |
| Q19 | Abstention | What was the private motivation of the leader who initiated [choose event]? | Abstain unless a source explicitly documents motive; do not invent psychology. |
| Q20 | Abstention | What happened in [choose event/page absent from captured corpus]? | State retrieval coverage and say not located; do not claim the event did not happen. |

## Required answer key fields

For each case, add: expected supporting page IDs; expected source passages/locators; required answer elements; known conflicting passages; acceptable inference; expected abstention (yes/no); reviewer and review date.

Do not score a question until its answer key is grounded in the captured source archive. Replace bracketed placeholders only after verifying candidate pages.
