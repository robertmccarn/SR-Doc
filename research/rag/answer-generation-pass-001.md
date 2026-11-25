# RAG answer-generation and citation evaluation — pass 001

**Status:** Completed as a source-grounded manual evaluation pass; not a runtime test of generated answers from the retrieval CLI.  
**Date:** 2026-11-24  
**Branch:** `audit/continuity-research`  
**Baseline:** Maintainer-approved `evaluation-set-001.md` (20 cases, approved 2026-11-21).  
**Pinned Bronze archive SHA-256:** `d1af0775d69def6ef442b66393e3ad84db6cb6b9ecf9138170573fdfe0a02c8`.  
**Parent HEAD before this pass:** `c867876993903e988ff14ed0777967d9d66467ec`.

## 1. Executive result

Twenty answer outputs were drafted against the approved answer criteria and checked against the exact Bronze page records and registered character locators. All 20 cases meet their answer-key requirements, including the three required abstention/qualified-absence cases (Q18–Q20) and the contradiction-disclosure cases (Q09, Q15–Q17).

This is **not** an end-to-end evaluation of the committed retrieval application. The prior retrieval benchmark used a source-equivalent local reconstruction, not byte-identical committed scripts. For this pass, I used the benchmark's recorded retrieved page IDs, expanded the corresponding pinned Bronze page records, and reviewed the source locators directly. The archive bytes were available in the mounted ZIP; Windows-style archive paths were used to locate the records. I did not execute the CLI to generate evidence packets or have the application generate these answers.

### Manual scoring summary

| Measure | Result | Interpretation |
|---|---:|---|
| Answer-key criteria satisfied | 20/20 | Every case meets its registered expected answer and required qualification/abstention |
| Cases with source/evidence citations | 20/20 | Each answer identifies the supporting page/revision/path/character range or the exact-title/asset inventory evidence |
| Unsupported factual claims identified in review | 0 | Manual claim-to-locator review; not an independent scorer |
| Required contradiction disclosures | 4/4 | Q09, Q15, Q16, Q17 |
| Required abstentions / qualified absence | 3/3 | Q18, Q19, Q20 |
| Namespace leakage | 0 | Answers rely on main-namespace source pages; title/asset absence checks use audit/index evidence |
| Automated citation precision | NOT MEASURED | No answer-generation runtime or independent citation parser was exercised |
| Independent claim-support score | NOT MEASURED | The same evaluator authored and reviewed the outputs |

Do not combine these results into a single reliability percentage. The 20/20 result is a manually reviewed answer-key compliance score for this bounded set, not a statistical estimate of production accuracy.

## 2. Method and evidence boundary

1. Re-verified branch `audit/continuity-research` at parent HEAD `c867876993903e988ff14ed0777967d9d66467ec`.
2. Read the normative `RESEARCH-ASSISTANT-PROTOCOL.md`, the approved 20-case answer key, the retrieval benchmark report, and documentation governance.
3. Confirmed the pinned ZIP's SHA-256 is the archive snapshot identifier recorded in the evaluation baseline. Read the ten registered Bronze page records directly from the ZIP and checked their expected IDs, titles, revisions, and character locators against the approved evaluation set.
4. Used the benchmark's retrieved page IDs and full-page expansion results as the retrieval handoff. Where first-stage passages missed registered locators, full-page expansion was used only for pages already discovered by retrieval.
5. Drafted each answer using only the captured main-namespace page content and documented archive/index metadata for absence checks. Each answer includes page ID, revision, repository-relative Bronze path, and character range.
6. Scored against the answer criteria and pitfalls already approved in `evaluation-set-001.md`.

**Important distinction:** This pass verifies that source-grounded answers can be composed from the retrieved page set plus full-page expansion. It does not show that the currently committed search CLI automatically returns all the evidence needed, nor that a model can reliably generate these answers from machine evidence packets without human expansion/review.

## 3. Answer outputs

### Q01 — Capital of the United Federation of China

**Answer:** Beijing.

**Evidence:** Direct infobox field `capital = Beijing`; page 655, revision 10838, `bronze/pages/655/10838.wikitext`, chars 1428–1445. Main namespace.

**Score:** PASS — direct fact and locator match.

### Q02 — United Federation of China existence dates

**Answer:** The United Federation of China is dated 2058–2108 in its infobox.

**Evidence:** `year_start=2058` and `year_end=2108`; page 655, revision 10838, `bronze/pages/655/10838.wikitext`, chars 213–244. Main namespace.

**Score:** PASS — both endpoints preserved as infobox values.

### Q03 — Third Chinese Civil War dates

**Answer:** The Third Chinese Civil War's overall infobox date range is 2105–2126.

**Evidence:** `date= 2105-2126`; page 1408, revision 11531, `bronze/pages/1408/11531.wikitext`, chars 120–137. Main namespace.

**Score:** PASS — overall date distinguished from combatant phase labels.

### Q04 — Association of East-Asia president

**Answer:** The Association of East-Asia page lists Raku Li Kim as President.

**Evidence:** `leader_title1 = President` and `leader_name1 = Raku Li Kim`; page 1927, revision 11231, `bronze/pages/1927/11231.wikitext`, chars 409–462. Main namespace.

**Score:** PASS — name and office both cited.

### Q05 — Lost Decade (China) overview

**Answer:** The page describes the Lost Decade as the period following the collapse of China's commodities bubble. It says the term originally referred to 2018–2027, before being overtaken by the more severe Market Crash of 2027. Its account describes economic stagnation and reform pressures, political purges, rising sea levels and displacement, rebellion in frontier provinces and Tibet, and a return to regionalism and civil strife.

**Evidence:** Page 1319, revision 9584, `bronze/pages/1319/9584.wikitext`, lead and Causes section, chars 0–2050. Main namespace.

**Score:** PASS — summary is attributed to the page and does not import external history. The answer is a concise synthesis of the cited passage, not a claim that each causal statement has independent corroboration.

### Q06 — Whether “UFC” is a formal alias or redirect

**Answer:** The United Federation of China page uses “UFC” contextually in its prose after naming the United Federation of China. The captured title/redirect index does not establish a separate exact-title page or formal redirect/alias named “UFC.” The abbreviation should therefore be treated as contextual shorthand, not a verified alias-index mapping.

**Evidence:** Page 655, revision 10838, `bronze/pages/655/10838.wikitext`, prose chars 2550–2900; exact-title/redirect inventory and approved evaluation case Q06. Main namespace for the prose; derived title inventory for the lookup result.

**Score:** PASS — distinguishes a contextual abbreviation from a formal resolver mapping.

### Q07 — Main Page redirect target

**Answer:** Captured page 84, “Main Page,” redirects to page 2, “Second Renaissance Wikia.” The redirect source identity remains page 84; it is not the same record as the target page.

**Evidence:** Page 84, revision 87, `bronze/pages/84/87.wikitext`, chars 0–38; target page 2, revision 11916, `bronze/pages/2/11916.wikitext`. Main namespace.

**Score:** PASS — target and redirect-source provenance preserved.

### Q08 — PRC and UFC identity

**Answer:** They are distinct captured page identities. The People's Republic of China page describes the PRC as a communist country in East Asia; the United Federation of China infobox separately lists the People's Republic of China as predecessor `p1`. The predecessor relationship does not establish that the two page identities are the same entity.

**Evidence:** PRC page 2418, revision 11711, `bronze/pages/2418/11711.wikitext`, lead chars 0–80; UFC page 655, revision 10838, `bronze/pages/655/10838.wikitext`, predecessor field chars 246–278. Main namespace.

**Score:** PASS — distinguishes page identity from a stated succession relationship.

### Q09 — Second Chinese Civil War infobox date and date-like combatant value

**Answer:** The Second Chinese Civil War infobox gives 2027–2048 as its `date` value. Separately, its `combatant1` block contains the date-like label 2105–2111. These are different source fields and must not be collapsed into a single war range.

**Evidence:** Page 1413, revision 11017, `bronze/pages/1413/11017.wikitext`, `date` value chars 114–125 and `combatant1` chars 198–554. Main namespace.

**Score:** PASS — both observations are disclosed with field distinction.

### Q10 — Third Chinese Civil War phases

**Answer:** The overall infobox range is 2105–2126. The combatant blocks separately label phases 2105–2111 and 2117–2126 under `combatant1`, and 2105–2108 and 2117–2126 under `combatant2`. These field labels do not establish that every listed participant fought throughout the entire overall period.

**Evidence:** Page 1408, revision 11531, `bronze/pages/1408/11531.wikitext`, overall date chars 120–137; `combatant1` phase/participant block chars 209–~930; `combatant2` phase/participant block chars 931–~1832. Main namespace.

**Score:** PASS — overall range and side-specific phase labels remain distinct.

### Q11 — UFC / Federal Republic of China transition

**Answer:** The UFC infobox ends in 2108. The Federal Republic of China infobox begins in 2108 and lists the UFC as its predecessor. The shared boundary year is documented, but the transition mechanism is not explained by these fields.

**Evidence:** UFC page 655, revision 10838, `bronze/pages/655/10838.wikitext`, `year_end` chars 239–244; FRoC page 649, revision 10840, `bronze/pages/649/10840.wikitext`, `year_start` chars 212–228 and `p1` chars 246–278. Main namespace.

**Score:** PASS — no unsupported overlap or transfer narrative.

### Q12 — Second Chinese Civil War combatants

**Answer:** The `combatant1` block lists the People's Republic of China and Shanghai. The `combatant2` block lists Tibet, East Turkestan, Manchuria, Hainan, Macau, and Hong Kong.

**Evidence:** Page 1413, revision 11017, `bronze/pages/1413/11017.wikitext`, `combatant1` chars 198–554 and `combatant2` chars 566–1137. Main namespace.

**Score:** PASS — the two sides are preserved as the infobox lists them; no additional alliance or command claim is inferred.

### Q13 — Joseph Loveridge's Chairman role

**Answer:** Joseph Loveridge is listed as Chairman of the Joint Chiefs of Staff, with Chet Singh as predecessor and Rohan Mustafa as successor. The listed term is January 25, 2141 through July 15, 2149.

**Evidence:** Page 1343, revision 8656, `bronze/pages/1343/8656.wikitext`, `office` chars 161–207; `predecessor` chars 207–231; `successor` chars 231–260; `term_start` chars 260–291; `term_end` chars 291–317. Main namespace.

**Score:** PASS — fields are associated with the Chairman role and not the separate second office.

### Q14 — UFC predecessors and successors

**Answer:** The UFC infobox lists two predecessors: People's Republic of China and Republic of China. It lists twelve successors: Federal Republic of China, Guangdong, Fujian, Wuyue, Jiangxi, Hunan, Zhuang, Yunnan, Manchuria, Hainan, Taiwan, and Federated Provinces of the Yangtze. These are the infobox's explicit parameter values, not an independently adjudicated political succession graph.

**Evidence:** Page 655, revision 10838, `bronze/pages/655/10838.wikitext`, predecessor/successor fields `p1`–`p2` and `s1`–`s12`, chars 246–~1110. Main namespace.

**Score:** PASS — all listed values preserved and correctly qualified.

### Q15 — Why the Second Chinese Civil War page contains 2105–2111

**Answer:** The captured page does not explain why 2105–2111 appears in the Second Chinese Civil War's `combatant1` block alongside its 2027–2048 infobox date. The Third Chinese Civil War page independently uses 2105–2111 as a `combatant1` phase label. The sources establish the observations, not their cause.

**Evidence:** Second Chinese Civil War page 1413, revision 11017, `bronze/pages/1413/11017.wikitext`, chars 114–125 and 198–554; Third Chinese Civil War page 1408, revision 11531, `bronze/pages/1408/11531.wikitext`, chars 324–333. Main namespace.

**Score:** PASS — explanation abstained; no copying error, retcon, or shared-event theory invented.

### Q16 — UFC, FRoC, and Association chronology

**Answer:** The UFC is dated through 2108. The FRoC is dated 2108–2139, lists the UFC as predecessor, and lists the Association of East-Asia as successor. The FRoC's Foundation section says “TBA.” The Association page gives its establishment date as January 1, 2140. The captured pages do not provide the missing transition narrative.

**Evidence:** UFC page 655, revision 10838, `bronze/pages/655/10838.wikitext`, chars 239–244 and 403–432; FRoC page 649, revision 10840, chars 212–243, 246–278, 321–349, and 1906–1940; Association page 1927, revision 11231, `bronze/pages/1927/11231.wikitext`, chars 635–670. Main namespace.

**Score:** PASS — dates, predecessor/successor fields, TBA stub, and establishment date disclosed without inventing the 2108–2140 history.

### Q17 — Historical dates in modern Chinese-state infoboxes

**Answer:** The UFC infobox labels its era “20th century” while listing historical events including the Xinhai Revolution (1911), Nationalist rule from Nanking (1927), the Second Sino-Japanese War (1937), the Constitution (1947), and the Battle of Huaihai (1948). The FRoC infobox labels its era “22nd century” but repeats those historical event dates; it also lists first/last leader years 1912 and 1949 and statistics for 1912. These are literal captured values and appear inconsistent with the stated modern eras; the source does not explain them.

**Evidence:** UFC page 655, revision 10838, `bronze/pages/655/10838.wikitext`, era/events chars 1904–2450; FRoC page 649, revision 10840, `bronze/pages/649/10840.wikitext`, leader years chars 938–1027, era/events chars 1111–1605, and statistics chars 1670–1686. Main namespace.

**Score:** PASS — literal values retained; “carryover” is not asserted as a proven cause.

### Q18 — Exact Federal Republic territorial boundary in 2120

**Answer:** Abstain. The Federal Republic of China page references a historical orthographic-projection map, but the map binary is absent from this archive snapshot. The captured text and caption do not establish the exact territorial boundary in 2120.

**Evidence:** FRoC page 649, revision 10840, `bronze/pages/649/10840.wikitext`, `image_map` chars 666–726 and caption chars 727–835; UFC page 655, revision 10838, `image_map` chars 1232–1292. The referenced filename appears in the raw page references and page-manifest image metadata but has no asset-manifest row or physical binary in this archive snapshot; see `evaluation-set-001.md` and locator-validation report.

**Score:** PASS — correct abstention; does not infer territory from other fields or maps.

### Q19 — Private motivation of the Second Chinese Civil War initiator

**Answer:** Abstain. The captured Second Chinese Civil War page does not establish a named initiator's private motivation. It describes the conflict and background conditions, but those descriptions do not prove an individual's private intent.

**Evidence:** Page 1413, revision 11017, `bronze/pages/1413/11017.wikitext`, full article body chars 1388–2743 and infobox chars 0–1388. Main namespace.

**Score:** PASS — no psychology or unsupported motive inferred.

### Q20 — Exact title “Association of East Asia”

**Answer:** No exact captured page titled “Association of East Asia” was found in the approved title/redirect inventory. A distinct near-title, “Association of East-Asia” (page 1927), exists. Do not treat the hyphenated page as the exact requested title without an approved alias/identity rule.

**Evidence:** Exact-title/redirect lookup result and approved evaluation inventory; near-title page 1927, revision 11231, `bronze/pages/1927/11231.wikitext`. See `evaluation-set-001.md` Q20 and `retrieval-benchmark-pass-001.json` Q20. Main namespace for the near-title.

**Score:** PASS — exact-title absence is distinguished from entity nonexistence; no fuzzy merge.

## 4. Per-case scoring

| Case | Answer criteria | Citation/provenance | Contradiction / abstention behavior | Result |
|---|---|---|---|---|
| Q01 | Complete | Direct field | Not required | PASS |
| Q02 | Complete | Both date fields | Not required | PASS |
| Q03 | Complete | Overall date field | Phase distinction retained | PASS |
| Q04 | Complete | Name and title fields | Not required | PASS |
| Q05 | Complete | Lead and Causes passage | Attributed summary | PASS |
| Q06 | Complete | Prose + title inventory | Abbreviation not promoted to alias | PASS |
| Q07 | Complete | Redirect source + target | Source identity retained | PASS |
| Q08 | Complete | Both page identities + predecessor | Identity not conflated | PASS |
| Q09 | Complete | Two separate fields | Both date signals disclosed | PASS |
| Q10 | Complete | Overall + phase fields | Side-specific phases retained | PASS |
| Q11 | Complete | Both country infoboxes | Transition not invented | PASS |
| Q12 | Complete | Both combatant blocks | No extra relationships inferred | PASS |
| Q13 | Complete | Office and term fields | Separate office not conflated | PASS |
| Q14 | Complete | All predecessor/successor fields | Infobox not treated as adjudicated graph | PASS |
| Q15 | Complete | Both conflict pages | Cause left unresolved | PASS |
| Q16 | Complete | Three page identities | Chronology gap disclosed | PASS |
| Q17 | Complete | Both infoboxes | Apparent carryover not explained away | PASS |
| Q18 | Correct abstention | Map reference + missing-asset inventory | Abstain | PASS |
| Q19 | Correct abstention | Full page review | Abstain | PASS |
| Q20 | Qualified exact-title absence | Title inventory + near-title source | No fuzzy merge | PASS |

## 5. Findings and implications

### What this pass establishes

- The approved answer key is sufficiently specific to support a repeatable manual answer review.
- All 20 questions can be answered or appropriately qualified using the registered source pages and the documented full-page expansion step.
- The answer contract's contradiction and abstention rules are actionable: Q09/Q15–Q17 can disclose conflicting or incomplete source data without inventing explanations; Q18/Q19 abstain; Q20 reports a search-boundary result without asserting nonexistence.
- Character-range citations can be expressed consistently using page ID, revision, source path, field/section, and offsets.

### What this pass does not establish

- It does not establish that the committed retrieval CLI returns the same evidence packets used here.
- It does not establish autonomous answer-generation quality; the answers were manually composed from source pages.
- It does not establish independent citation precision, independent claim-support rate, semantic contradiction precision, or statistically meaningful abstention quality.
- It does not remove the source-equivalent reconstruction caveat from retrieval benchmark pass 001.
- It does not validate the corpus beyond the approved 20-case set.

## 6. Recommended next work

1. **Close the retrieval reproducibility gap:** run the exact committed `build_index.py`, `build_alias_index.py`, and `search.py` Git blobs against the pinned archive, verify blob hashes before execution, and regenerate the 20 evidence packets.
2. **Automate packet-to-answer fixtures:** store the 20 source-grounded answer outputs and expected claim/citation elements in a machine-readable evaluation format. Validate citation references and answer-key coverage mechanically where possible.
3. **Separate generation from scoring:** use an independent evaluator or blind second pass for claim support, citation precision, contradiction disclosure, and abstention. Do not score model self-review as independent.
4. **Measure first-stage locator recall:** address the eight missed passage ranges before treating full-page expansion as an acceptable default cost.
5. Keep the approved evaluation baseline unchanged unless the maintainer explicitly approves a versioned revision.

## 7. Files and change control

This pass adds one bounded research artifact. It does not modify Bronze/Silver source bytes, manifests, lore canon, retrieval code, schemas, or the approved evaluation questions. No merge, pull request, or branch promotion was performed.

**Evaluation integrity note:** This is a manual answer-generation and scoring pass by the same agent. Its value is a source-grounded reference answer set and explicit score rubric, not independent validation. A future independent evaluator should score the answer outputs without using this pass's pass/fail labels as hints.
