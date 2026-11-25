# Retired-claim dependency discovery — pass 001

**Date:** 2026-11-25  
**Branch:** `experiment/corrected-realism`  
**Scope:** Read-only dependency discovery and claim inventory for section 4 of `realism-first-timeline-2024-2040.md`. This note and its CSV ledger are research artifacts, not canon edits.

## 1. Executive result

The scan covered the pinned Bronze Wikitext and Silver metadata in `SR-Doc-Audit.zip`, plus the repository's page ledger and available RAG assets.

- **Bronze corpus:** 3,579 page records, including 507 Main-namespace pages. The archive SHA-256 is `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`. All 3,579 raw Wikitext files were SHA-256 checked against `bronze/manifests/pages.json`; **3,579/3,579 matched**.
- **Page ledger:** key source records were cross-checked against `research/page-ledger.csv` for page ID, title, revision, raw path and SHA-256. The ledger itself is an index, not a substitute for the captured source bytes.
- **Silver metadata:** 3,579 page rows, 11,462 parsed `wiki_link` relation records, and 4,447 year-mention records.
- **Exact-phrase corpus scan:** 107 unique Main-namespace pages contain at least one scoped event/entity phrase. The group counts overlap; they must not be summed.
- **Direct relationship graph:** 148 Silver `wiki_link` edges point to the scoped canonical target titles, originating from 73 unique source pages: 145 edges from Main pages, two from User pages, and one from a Template page.
- **Claim ledger:** `claim-ledger-001.csv` contains 243 grouped source observations with page/revision/hash, location, old value/evidence, proposed disposition, confidence, and dependent-page list. Row counts are grouped observations, not unique pages or graph edges.

No accepted canon, Bronze/Silver source data, manifests, or RAG implementation files were changed.

## 2. Method and evidence classes

### Inputs

1. `bronze/manifests/pages.json` and the referenced raw Wikitext files in the supplied ZIP.
2. `silver/pages.jsonl`, `silver/relations.jsonl`, and `silver/timeline.jsonl` in the same ZIP.
3. Current repository `research/page-ledger.csv`.
4. Current `research/rag/` code, README and validation/build reports; recursive Git tree inventory at the branch HEAD.

### Search procedure

- Scanned all 3,579 captured Wikitext records. Main namespace (namespace 0) is the canon/dependency result set; Talk, Thread, User, File and Template namespaces are context only and reported separately.
- Searched exact titles and scoped aliases: The Flood / Flood of 2026 / Flood refugees; Great Famine / American Famine; Market Crash of 2027; Revolutions of 2027; Second Chinese Civil War; White Tide; Alexandria Ocasio-Cortez; Great Reset; Mars Corporation; Meridian Base; American colonization of Mars; Dissolution of the Russian Federation / Russian Republic / Treaty of Odessa; Arctic-to-Bosporus pipeline / Bosporus pipeline / occupation of Arabia / Rise of Turkey; Galileo II.
- Searched relevant numeric and date claims, including 7 m and 30 m sea level, 300m deaths and 300m without basic needs (kept distinct), 2.4bn displaced, 11m deaths, 100m–500m and 40m famine mortality, 70%/22% fishery reductions, halved rice output, 100m Chinese displacement, White Tide force/casualty figures, 90m displacement, 39 states, 400m U.S. population, the 100-person/27-day Mars mission, and the 2029/2030/2033/2038 program milestones.
- Classified parsed links from Silver relations separately from text-only mentions. Redirect directives, category membership, and template/module invocations were inspected as distinct structures. Page transclusion syntax `{{:Page title}}` was searched separately from normal template calls.
- Recomputed each raw Wikitext SHA-256 from bytes (not decoded/re-encoded text) and compared it with the Bronze page manifest. Key page-ledger records were also compared to the archive identity.

### Evidence labels

- **Observed:** literal source text, a parsed relation, redirect directive, category membership, or template invocation.
- **Computed:** counts, unique-page totals, SHA-256 comparisons, and reverse-link lists derived from the captured records.
- **Inferred:** editorial review candidates identified from the timeline's existing dependency checklist or from a clearly related downstream premise; they are not counted as literal hits.
- **Hypothesis:** a proposed causal explanation that is not established by this corpus scan.
- **Unresolved:** missing target article, ambiguous scope, conflicting source values, or unverified rendering behavior.

## 3. Dependency counts

### 3.1 Exact-phrase Main-namespace pages

| Claim / entity | Main pages with scoped phrase hit |
|---|---:|
| The Flood | 58 |
| Great Famine | 10 |
| Market Crash of 2027 | 13 |
| Revolutions of 2027 | 13 |
| Second Chinese Civil War | 7 |
| White Tide | 21 |
| Alexandria Ocasio-Cortez | 17 |
| Great Reset | 17 |
| Mars Corporation | 16 |
| Meridian Base | 5 |
| American colonization of Mars | 4 |
| Russian dissolution / Russian Republic / Treaty of Odessa | 8 |
| Turkey Arabia / pipeline | 2 |
| Galileo II | 2 |

These are overlapping phrase-hit groups. Their union is **107 unique Main-namespace pages**. The full page IDs/titles are carried in the ledger's `dependent_pages` column.

### 3.2 Parsed direct wikilinks

Counts below are Silver `relations.jsonl` graph edges, followed by unique source pages. They are not the same denominator as grouped rows in the CSV.

| Target title | Edges | Unique source pages |
|---|---:|---:|
| The Flood | 36 | 30 |
| Great Famine | 10 | 9 |
| Market Crash of 2027 | 13 | 12 |
| Revolutions of 2027 | 13 | 10 |
| Second Chinese Civil War | 7 | 7 |
| White Tide | 18 | 16 |
| Alexandria Ocasio-Cortez | 20 | 15 |
| Great Reset | 14 | 13 |
| Mars Corporation | 7 | 7 |
| Meridian Base | 0 | 0 |
| American colonization of Mars | 4 | 4 |
| Dissolution of the Russian Federation | 5 | 5 |
| Galileo II | 0 | 0 |
| Russian Republic | 0 | 0 |
| Treaty of Odessa | 1 | 1 |
| **Total** | **148** | **73 across all targets** |

Namespace breakdown of those 148 edges: 145 from Main pages, two from User pages, and one from a Template page. The 73 source pages comprise 70 Main, two User, and one Template page. Several sources link to more than one target.

### 3.3 CSV dependency-type counts

The 243 ledger rows are grouped source observations:

| Ledger dependency type | Rows |
|---|---:|
| Direct wikilink observation | 127 |
| Text-only mention | 66 |
| Numeric claim / value | 31 |
| Timeline field | 4 |
| Redirect | 3 |
| Template / infobox use | 6 |
| Category membership | 6 |
| **Total** | **243** |

The 127 direct-link rows group page/claim observations; the authoritative graph-edge count is the separate 148 figure above. Do not equate rows, edges, and unique pages.

### 3.4 Redirects, categories, templates and transclusions

- **Redirects (3 observed):** page 1310 `Frontier Program` → `American colonization of Mars`; page 1577 `Dissolution of the Eurasian Union` → `Dissolution of the Russian Federation`; page 1728 `The Great Reset` → `Great Reset`. The Russian dissolution redirect points to a target for which no dedicated Main-namespace article was found.
- **Category:** `Category:The Flood` has three captured page memberships: page 637 `The Flood`, plus File pages 639 `File:FloodMap.png` and 2049 `File:North America Flood.png`. This is classification/asset association, not three dependent lore articles. No equivalent retired-event category was found for the other targets.
- **Template/infobox use:** six source pages have 21 template/module invocations recorded in the Bronze manifest: Mars Corporation (638), American colonization of Mars (1139), Second Chinese Civil War (1413), Great Reset (1670), Alexandria Ocasio-Cortez (3592), and White Tide (3593). These are formatting/metadata dependencies, not evidence that those pages are transcluded into other articles.
- **Template link:** `Template:Periods in US history` links to `Great Reset`; it is transcluded on page 1670. This is a navigation/template link chain, not transclusion of the Great Reset article.
- **Page transclusion:** no explicit `{{:Target page}}` transclusion of the scoped event/entity pages was found in Main-namespace Wikitext. Dynamic rendering through modules, parser functions, or external gadgets is not proven absent.

## 4. Retired-claim findings and disposition

### Flood and food crisis

- **The Flood, page 637:** the article states 300m deaths worldwide (lead, line 2); 2.4bn displaced and 11m deaths in the initial 2026 flooding (line 14); sea levels reaching 7m in the same passage; and a near-30m 2041 peak (lines 2 and 19). It separately states that 300m people in China were left without a reliable source of food, shelter or clean water in 2039 (line 51). The latter is not a death count and must not be conflated with the lead's 300m deaths. Timeline page 88 gives the 7m event in 2026.
- **Great Famine, page 2027:** lead says 2024–2033 and 100m to half a billion deaths; it separately states 40m deaths in the 2024 episode. Page 3 describes a 70% North Atlantic fishery reduction and a 22% Asian reduction; it also describes rice production loss. Page 12 retrospectively identifies three episodes: Famine of 2024, Great Famine of 2027, and American Famine of 2029–2031. Preserve the timeline/article endpoint discrepancy (2032 vs 2033) and the three-episode distinction until explicitly reconciled.
- **Disposition:** remove the global famine framing and extreme totals. Retain only separately evidenced, regional food crises with proximate causes, bounded geography, duration, production/import effects, and clearly defined mortality/displacement categories.

### Economic and political upheaval

- **Market Crash of 2027, page 642:** lead fixes the crash at 24 October 2027. The article attributes it to multiple interacting factors, including labor shortage, housing-market stress, supply/energy constraints, speculative expansion, and a reported 36.6% increase in financial-services profits in H1 2027. Do not silently collapse these into a single demographic cause.
- **Revolutions of 2027, page 820:** lead describes a global revolutionary wave affecting more than 50 countries; page 3 says the wave began in China in February and spread across Eurasia and parts of Africa. The page explicitly connects food shortages, refugee politics, class demands, nationalism, and dissatisfaction with leadership.
- **Great Reset, page 1670:** describes a broad 2010s/2020s socioeconomic transition, with competing proposed start dates and multiple economic, demographic, political, labor and automation mechanisms. The realism-first disposition is not to erase all structural change; it is to remove a deterministic, singular “reset” whose endpoint is made inevitable by the implausible global Flood/revolution chain. Validate the causal claims individually.
- **Disposition:** the Market Crash may remain only as a contingent crisis with a credible financial trigger and transmission model. Replace the synchronized global revolution with region-specific political processes. Retain plausible institutional/economic pressures under the Great Reset label only where supported.

### China

- **Second Chinese Civil War, page 1413:** infobox dates the war 2027–2048; its narrative includes the Three Gorges Dam catastrophe and over 100m people forced inland. Page 1413 also contains a later 2105–2111 combatant-period field. Page 1408 `Third Chinese Civil War` is a separate later chronology and must not be silently merged with the pre-2041 war.
- **Disposition:** remove the 2027–2048 civil-war chronology, dam catastrophe trigger and 100m displacement. Retain the 2105–2111 / page-1408 conflict as a separately unresolved later-source issue; it must not depend on the removed 2027 war.

### United States, White Tide and AOC

- **White Tide, page 3593:** infobox dates 2028–2035; lists force strengths of 8.9m and 8.1m and casualties of 8.55m and 4.45m. Narrative describes attacks on 18 state capitols, five captured capitols, and three state governments voting to secede. The article is marked WIP.
- **Alexandria Ocasio-Cortez, page 3592:** future narrative makes her the 2028 election winner and president from 2029; says nearly 90m Americans remain displaced and 39 states face domestic terrorism/armed insurrection by 30 November 2029. Timeline page 88 also projects 400m U.S. population by 2035.
- **Disposition:** preserve AOC as a real-world person and preserve observed biography through the historical cutoff. Her future election/presidency is not a required event; if retained, it is one contingent fictional political outcome. Remove White Tide civil-war/secession/mass-casualty/mass-displacement scale; at most retain bounded extremist violence. Remove the 90m displacement and 400m population assumptions unless a new, defensible demographic model supports them. American Renewal may remain a policy label, with ordinary legal, fiscal, construction and demographic timescales.

### Russia and Turkey

- **Russian dissolution:** timeline page 88 schedules dissolution in 2029–2038 and a NATO/UN nuclear-stockpile operation. Page 1683 `Russia` describes a Russian Republic successor, with an infobox end-year 2139 and prose end-year 2138. Page 1729 `Treaty of Odessa` describes a 2034 Poland–Turkey agreement, assented to by Japan and the United States, over territories of the former Russian Federation. Page 1577 is a redirect to the absent `Dissolution of the Russian Federation` target.
- **Turkey Arabia/pipeline:** the explicit Arabia occupation and Arctic–Bosporus pipeline are timeline-only claims in this exact search; page 1438 `Eurasian Coalition` is the other exact-phrase hit. The existing timeline dependency checklist separately identifies page 1423 `Turkey` for review, but it did not produce an exact pipeline/occupation phrase hit in this scan.
- **Disposition:** keep the Russian Federation intact through 2040; remove pre-2041 dissolution and foreign nuclear-stockpile seizure. Preserve the 2138/2139 discrepancy as a separate later-chronology source conflict. Remove Arabia occupation and the mega-pipeline; retain plausible Turkish influence through diplomacy, defense, trade corridors and bounded regional operations. Page 1423 is an **inferred review candidate**, not an observed exact-match hit.

### Mars and outer-planet program

- **Mars Corporation, page 638:** describes the company as founded 31 December 2023 and a 100-person crewed Mars landing at Meridian Base after a 27-day voyage. The timeline page 88 separately calls 2026 the first crewed Mars mission. These are contradictory source claims; do not choose one as the “correct” mission date.
- **American colonization of Mars, page 1139:** describes a 50-year Frontier Program and 2029 magnetoshield, 2030 asteroid redirection, genetic terraforming and 2033 solar-mirror/biosphere milestones. Redirect page 1310 points to this article.
- **Meridian Base:** no dedicated Main-namespace article and no parsed direct wikilinks; five Main pages contain the phrase (timeline 88, Mars 318, Mars Corporation 638, colonization 1139, Bradbury 2150).
- **Galileo II:** no dedicated Main-namespace article and no parsed direct wikilinks; exact phrase appears on timeline 88 and Adrian Hayer 1589. Timeline associates it with 2030–2038 outer-planet exploration/resource-economy claims.
- **Disposition:** remove the 2023/2026 crewed landing and permanent base assumptions through 2040; recast Mars Corporation as a terrestrial aerospace/robotics venture or later mission contractor if retained. Remove the 2029–2033 terraforming, magnetoshield, asteroid-redirection and solar-mirror sequence. Keep Galileo II only as a plausible robotic science/technology demonstration; remove industrial extraction, crewed Titan settlement and routine resource deliveries.

## 5. Context namespaces — not canon dependency counts

The exact-phrase scan found 27 non-Main pages:

- **Talk (namespace 1): 8** — page IDs 1287, 1409, 1784, 2644, 3163, 3239, 3398, 3512.
- **Thread (namespace 1201): 12** — page IDs 1289, 1301, 1449, 1490, 1501, 2327, 2999, 3230, 3246, 3346, 3513, 3557.
- **User (namespace 2): 3** — page IDs 2331, 2355, 3727.
- **File (namespace 6): 3** — page IDs 639, 2049, 3571.
- **Template (namespace 10): 1** — page ID 2583.

These records can preserve creator discussion, personal drafts, or asset metadata. They are context only and must not be silently promoted into canon. The two User-namespace direct-link edges and the single Template-namespace Great Reset edge are already separated in the graph counts above.

## 6. RAG/index availability

The supplied ZIP contains Silver `pages.jsonl`, `relations.jsonl`, and `timeline.jsonl`; these were scanned. The repository tree contains RAG source code, schemas, tests, and validation/benchmark reports. It does **not** contain the built SQLite FTS database, chunk JSONL, or the separately described `SR-Doc-RAG-Index-001.zip` artifact. Therefore:

- Silver parsed-link and year-mention data were available and used.
- No live RAG retrieval query was run for this pass.
- No claim is made that RAG search independently found or missed any item.
- The RAG README's previously reported 7,598-chunk build is historical evidence of a local artifact, not proof that that artifact was present in this working environment.

## 7. Limitations and unresolved items

1. Phrase matching is deliberately conservative and can miss synonyms, paraphrases, misspellings, or indirect causal dependencies. It can also return incidental mentions; every row retains its source locator and snippet for review.
2. The acronym `AOC` was not used as a standalone phrase query because it is ambiguous; the full name Alexandria Ocasio-Cortez was searched.
3. Silver `wiki_link` records are parsed source links, not proof of rendered display, reader navigation, semantic dependence, or canon importance.
4. The category and template inventories are source metadata. No full MediaWiki renderer, Lua execution, gadget execution, or browser-rendered page inspection was run.
5. The transclusion search detects explicit page transclusion syntax in raw Wikitext. Dynamic transclusion via modules, parser functions, or extension behavior remains unverified.
6. Page 1423 `Turkey` is an editorially identified review candidate from the existing dependency checklist, not an exact phrase hit for the occupation/pipeline claims.
7. The target `Dissolution of the Russian Federation` has a redirect but no dedicated Main-namespace page. Meridian Base and Galileo II also have no dedicated Main-namespace pages.
8. The Great Famine's 2032/2033 endpoint, the Flood's 300m deaths versus 300m without basic needs, the 2023/2026 Mars first-crew claims, and the Russian 2138/2139 successor-state end year are distinct source conflicts. Preserve them; do not normalize them during discovery.
9. The Market Crash's 2027 date and mechanisms, Great Reset's periodization/causality, and AOC's hypothetical future presidency are not resolved by link counts. They require claim-level editorial review.
10. No canon edits, tests, builds, RAG CLI executions, PRs, merges, or branch promotions were performed.

## 8. Next step

Use this ledger as the dependency baseline for a **separate claim-reconciliation review**. Before any canon edit, review the 107 Main-namespace pages and all direct-link targets together, identify which references are causal versus incidental, reconcile each source conflict, and prepare a page-by-page change proposal. The user must separately authorize canon edits.
