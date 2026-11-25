# Flood claim reconciliation — pass 001

**Date:** 2026-11-25  
**Branch:** `experiment/corrected-realism`  
**Status:** Non-canon editorial analysis; no accepted lore or source files changed.  
**Authority:** `realism-first-timeline-2024-2040.md`, especially its binding realism rule and section 4 retcon matrix.  
**Source archive:** `SR-Doc-Audit.zip`, SHA-256 `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`.

## 1. Scope and method

This is the first bounded claim-reconciliation tranche: every one of the **58 Main-namespace pages** returned by the pass-001 exact phrase search for `The Flood`, `Flood of 2026`, or `Flood refugees`.

- Read page identity, revision and raw SHA-256 from `bronze/manifests/pages.json`.
- Searched each corresponding raw Bronze Wikitext file; the page-level phrase-hit count is recorded in the companion CSV.
- Compared Silver `parsed_links` against the canonical target `The Flood` (including anchor links). The 58 phrase-hit pages contain **35 canonical direct-link edges across 29 pages**; the remaining 29 pages have no parsed direct link to that target. This is a phrase-hit subset, not the full Flood graph count from dependency discovery.
- Reviewed source context around matches and cross-checked the detailed source claims already documented for page 637 and timeline page 88.
- Classified each page by semantic dependency, not merely by whether a wikilink exists.

**Review limitation:** this is a focused context-window reconciliation of the phrase hits, not a complete line-by-line semantic review of every sentence in all 58 pages. Classifications marked indirect/ambiguous are review judgments and should be revisited during the later page-by-page proposal. The CSV records the exact source revision and hash so the review is reproducible.

## 2. Results

| Exclusive review class | Pages | Interpretation |
|---|---:|---|
| Primary source / chronology authority | 2 | The Flood article and master timeline establish the retired event and its chronology |
| Direct causal or structural dependency | 37 | Page content attributes a political, economic, demographic, technical, military or regional outcome to the Flood |
| Indirect / downstream dependency | 11 | Cohort labels, later wars, ideology, later economic events or biographical context inherit the Flood premise |
| Cultural / summary reference | 4 | Century overview or fictional books/texts refer to the Flood without being direct event mechanisms |
| Incidental / poll artifact | 3 | A poll option or passing media reference; no meaningful lore dependency established |
| Regional climate mention to decouple | 1 | Mexico explicitly says it was not severely affected; retain independently plausible local hazards, not the global event |
| **Total** | **58** | All exact-phrase Main-namespace hits in this tranche |

The 35 direct-link edges are a structural observation. They do not imply 35 causal dependencies. Conversely, text-only pages can carry major causal dependencies: for example, the Earth Working Group and several country histories discuss Flood effects without a parsed link to the canonical Flood page.

## 3. Page-by-page disposition

The companion `flood-claim-reconciliation-001.csv` is the row-level record. It includes page ID, title, revision, source SHA-256, phrase-hit count, parsed direct-link count, dependency class, evidence summary, proposed disposition and confidence.

### Primary source and chronology

- **Page 637 — The Flood:** primary retired-claim source. Preserve the distinction between 300m deaths in the lead and 300m people without reliable food, shelter or water in China in the 2039 passage. They are not the same measure. The article also states 2.4bn displaced and 11m initial-event deaths, a gradual rise toward 7m, and a near-30m 2041 peak.
- **Page 88 — Timeline of major events:** central chronology dependency. It puts the 7m rise in 2026, the famine/revolution/Chinese war chain in 2024–2032, and the later near-30m sea-level claim in 2039–2043. These entries must be replaced together rather than edited independently.

### Direct causal or structural dependents (37)

| Page ID | Page | Reconciliation finding |
|---:|---|---|
| 107 | World War III | Ecological damage and mass British relocation shape the postwar settlement; rebuild migration and political effects independently. |
| 217 | United States of America | Major dependency: Flood section links disaster to labor shortage, crash, federal power, migration and population geography. |
| 642 | Market Crash of 2027 | Flood evacuation, recovery and insurance losses contribute to the crash; any retained crash needs an independent financial trigger. |
| 655 | United Federation of China | Flood worsens instability and drives inland migration/cultural change; decouple the Chinese transition. |
| 820 | Revolutions of 2027 | Famine, displacement and instability are part of a synchronized global revolutionary wave; replace with separate regional processes. |
| 911 | First Nations War | Infobox and EWG conflict inherit the Flood/Climate Wars framework; post-2041 conflict may remain only with a new causal chain. |
| 949 | Japan | Flood pressure is used to explain constitutional/military change and territorial expansion; re-ground in domestic politics and regional security. |
| 1085 | Genetic Engineering | Crop engineering and public acceptance are tied to Flood/Famine pressures; retain only plausible technology with independent drivers. |
| 1106 | Earth Working Group | Global restoration, New Tokyo, dredging and polar interventions are Flood responses; replace with bounded feasible projects. |
| 1162 | Israel | Jordan Valley flooding changes agricultural and foreign-policy priorities; retain water stress only with independent regional causes. |
| 1255 | European Union | Flood is credited with EU support resurgence; separate political/economic trends from the global shock. |
| 1260 | United Nations | North Korean collapse and UN stabilization are attributed to Flood-related internal strife; supply a distinct Korean trigger if retained. |
| 1351 | Seventh Party System | Party realignment, immigration and foreign policy depend on the Flood/labor-crisis chain; rebuild from elections, institutions and demographic/economic factors. |
| 1366 | Caribbean annexation | Total evacuations and refugee flows are linked to calving and rising seas; replace with bounded hurricane/storm-surge/migration cases. |
| 1413 | Second Chinese Civil War | Flood background, mass displacement, food pressure and Three Gorges Dam failure drive the war; remove the pre-2041 civil-war chain. |
| 1420 | Argentina | Río de la Plata damage is credited with severe contraction; use Argentina-specific fiscal, trade, commodity and hydrological drivers. |
| 1474 | India | Flood famine triggers Pakistan civil war, refugee flows, Kashmir uprising and Indian intervention; remove this causal chain. |
| 1551 | Quebec | Greenland event and Laurentian flooding drive economic damage and independence referendum; use credible constitutional/fiscal/linguistic causes if separatism remains. |
| 1637 | The Refreeze | 2045 geoengineering is explicitly a response to Flood effects; later divergence is allowed, but global sea-level reversal is not a credible mechanism. |
| 1670 | Great Reset | Flood intensifies refugee politics, labor shortages, unrest and famine; retain independent structural pressures, not a master catalyst. |
| 1811 | Arctic states | Refugee displacement and later geoengineering conflict underpin Arctic polities; rebuild any post-2041 formation from regional agency and feasible migration. |
| 1896 | Canada | Refugee inflow is described as Canada's main economic strain; replace mass-migration premise with plausible domestic and regional pressures. |
| 1913 | British Republic | Flood and Revolutions are cited as causes of constitutional transition and US-administered resettlement; rebuild independently. |
| 1927 | Association of East-Asia | Hundreds of millions displaced by Flood are used to explain the regional order; remove unsupported scale and re-ground East Asian developments. |
| 1937 | Australia | Flood is said to make the interior virtually uninhabitable; retain only defensible drought, heat, water and coastal hazards. |
| 2027 | Great Famine | 2027 famine is explicitly attributed to Flood, desalination, land loss and port destruction; remove global famine and extraordinary totals. |
| 2311 | Third Agricultural Revolution | Agricultural technology transfer is framed as a Flood response; potentially retain the transition with independent food-security and R&D drivers. |
| 2418 | People's Republic of China | Civil-war narrative ties coastal loss, 100m+ displacement, famine and dam failure to rebellion; remove the chain. |
| 2718 | Sovereign Citizen's Alliance | Infobox era marker and secessionist timeline overlap the Flood crisis; remove Flood marker and reassess scale under bounded-extremism rule. |
| 2775 | Brazil | Flood/Famine intensify opposition and precede rebellion/coup; re-ground in Brazilian institutions, land conflict, elections and military incentives. |
| 2801 | Europans | Lunar settlement is motivated by water demand during Flood; remove this rationale unless a separate credible space-economy case is built. |
| 3112 | Venezuela | Sea-level displacement and famine drive refugee camps and regime-changing revolution; remove the extreme chain and retain independent local pressures. |
| 3592 | Alexandria Ocasio-Cortez | Future presidency and Renewal narrative center on Flood crisis; preserve observed biography, but future presidency is optional fiction, not required canon. |
| 3593 | White Tide | Flood diverts federal resources and shapes political cooperation; apply the bounded-extremism retcon and remove mass-displacement dependence. |
| 3607 | Latvia | European collapse and Polish annexation are linked to Flood and retreating seas; remove this chain and independently ground any later Baltic realignment. |
| 3622 | Prime Minister of Canada | Flood-related problems are cited as cause of Canada's emergency government and 2029 republic transition; re-ground constitutional change independently. |
| 3670 | American Redoubt | Infobox labels the entity's era as the Flood; remove the era marker and reconcile its timeline with the bounded White Tide scale. |

### Indirect / downstream dependencies (11)

- **101 Dylan J. Price:** California disaster and failed relief are given as the reason for a 2026 gubernatorial run.
- **902 Carla Anderson:** Commonwealth resettlement in North America is biographical background; causal weight is limited.
- **1074 Augment Rights Movement:** “Flood Generation” is a cohort label and climate experience is used to explain naturalist attitudes.
- **1139 American colonization of Mars:** Flood-triggered Luddite politics affect public support for terraforming; the Mars program is independently retired.
- **1215 Postnaturalism:** Flood is the ideological pivot toward geoengineering.
- **1408 Third Chinese Civil War:** later narrative inherits Flood-driven inland migration and the Refreeze; preserve as a separate later continuity issue.
- **1580 List of recessions in the United States:** 2043 Summer of Storms is linked to the Flood; post-2041 event may be retained only with independent cause.
- **1919 Republic of Sahtu:** only a temporal comparison to life before the Flood was found; causal dependence is unresolved and must not be assumed.
- **2137 Generational Chaos:** Flood is listed as a Fourth Turning crisis.
- **2813 Neo-Jeffersonianism:** “Flood Generation” is used to explain postwar labor-market resentment.
- **3610 2060s:** decade's recovery is attributed to global cooling and sea-level reversal; remove the global Refreeze mechanism or explicitly define a later divergence.

### Cultural, summary, incidental and regional references (8)

- **94 21st Century:** summary list only; update after the timeline is reconciled.
- **2122 Notable Literature:** named works and literary eras refer to the Flood; review the premises of individual works.
- **2449 American Empire:** the book's thesis depends on the Flood making the US an “unintentional empire”; reframe if retained.
- **2452 The Great Deluge:** book about the Flood and claimed influence on EWG; remove or reframe.
- **2 Second Renaissance Wikia** and **1355 Poll archive:** the term appears only as a poll option; exclude as lore dependencies.
- **961 Trump-Russia scandal:** passing media-history reference only; no causal dependency established.
- **1391 Mexico:** explicit exception: the page says Mexico was not severely affected by the Flood. Retain only independently plausible northern drought and Mexico City flood risk; remove the global event label.

## 4. Cross-page causal clusters requiring separate reconciliation

1. **Physical event → famine → revolution → Chinese conflict:** pages 637, 88, 2027, 820, 1413 and 2418. This is a linked chain, not six independent events. Retiring the physical Flood removes the stated proximate cause for much of the chain.
2. **United States political/economic transition:** pages 217, 642, 1351, 3592, 3593, 2718 and 3670. The Flood currently explains labor, insurance, federal capacity, immigration, political realignment and extremist opportunity. Rebuild these as interacting but distinct pressures; do not substitute another single master cause.
3. **Regional state histories:** pages 949, 1162, 1255, 1260, 1366, 1391, 1420, 1474, 1551, 1811, 1896, 1913, 1927, 1937 and 3112. Remove the common global event and preserve only locally supported hazards, institutions and agency.
4. **Geoengineering and recovery:** pages 1106, 1215, 1637, 1811 and 3610. The current source architecture assumes a global disaster followed by planetary-scale reversal. Any retained environmental response must be bounded by feasible engineering, energy, finance, governance and timescales.
5. **Cultural memory and generations:** pages 1074, 2122, 2137, 2449 and 2813. Reassess the cohort label, literary works and ideology if the event is removed.

## 5. Findings and open questions

- The exact-phrase scan is not a complete synonym/semantic dependency search. Pages without a phrase hit may still depend on Flood assumptions through indirect causal claims.
- A parsed wikilink is not proof of causal dependence; text-only references can be more consequential than direct links.
- The 2041+ material is outside the no-divergence-before-2041 constraint, but it still cannot inherit physically impossible pre-2041 conditions without an explicit, dated divergence mechanism.
- Do not conflate the 300m death estimate with the separate 300m Chinese population lacking basic needs.
- Do not treat the 2.4bn displacement claim as “immediate”; the source says it followed the initial flooding, while describing meltwater rise as gradual.
- Page 1919 is unresolved; no retcon recommendation should be made on the phrase alone.
- Page 1391 is a regional-climate exception, not evidence that the global Flood is plausible.
- The existing ledger's `dependent_pages` field is a union-level discovery list, not a page-specific causal edge list. This reconciliation provides page-local classifications for this Flood tranche only.

## 6. Next tranche

Proceed to the Great Famine / Market Crash / Revolutions / Great Reset cluster. Reconcile the cross-links and shared causal claims together before reviewing the China, U.S., Mars, Russia and Turkey clusters. No canon edits, Bronze/Silver changes, manifest changes, PRs, merges or branch promotions are authorized.
