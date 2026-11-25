# Narrative audit — validation tranche 001

**Status:** Partial validation and first substantive review; not a completed corpus audit  
**Repository:** robertmccarn/SR-Doc  
**Branch:** experiment/corrected-realism  
**Audited branch HEAD:** fdec89ff1221a36fa360630b0d7607b7c7d2f95d  
**Audit date:** 2026-11-25

## 1. Scope and method

This tranche validates Claude's read-only handoff, reads the uncovered pages and recursively discovered dependencies, checks source provenance against the Bronze manifest, and performs targeted external checks.

The governing records reviewed were agents.md, .ai/swap.md, research/continuity/DOCUMENTATION-GOVERNANCE.md, research/continuity/MASTER-RESEARCH-REGISTER.md, research/README.md, research/session-log.md, and research/continuity/realism-first-timeline-2024-2040.md.

The audit remains on experiment/corrected-realism. No accepted canon, Bronze or Silver source data, manifests, or RAG implementation was modified. No tests, builds, or RAG CLI runs were performed.

### Page scope and integrity

Twenty-eight Bronze pages were examined at varying depth: 19 full semantic reads and 9 partial reads. All 28 raw Wikitext SHA-256 values matched the corresponding raw_sha256 values in bronze/manifests/pages.json.

The 28 pages comprise:
- The 14 exact-year pages identified by Claude as absent from claim-ledger-001.csv.
- Page 1998, Central Eurasian Union, as a separate Russia/Eurasia downstream candidate; it does not meet the year-count threshold.
- Five recursively discovered pages: 3484 New Korean Wave, 1234 Hypersonic Weapons, 2774 Project Rebirth, 1715 Korea, and 1436 Tactile-neural interface.
- Four chronology/authority pages: 88 Timeline of major events, 1683 Russia, 1729 Treaty of Odessa, and 1438 Eurasian Coalition.
- Four additional dependency pages: 1366 Caribbean annexation, 1479 Orbital Command Stations, 318 Mars, and 961 Trump-Russia scandal.

The CSV records exact page IDs, revision IDs, source paths, SHA-256 values, and review depth.

### Archive checksum

The uploaded SR-Doc-Audit.zip was available for direct verification. Its computed SHA-256 is:

d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8

This is a 64-character SHA-256. The 63-character transcription variant ending with db6cb6b9 was incorrect. The typo was present in five current research documents and in historical entries in session-log.md. The five current documents have been corrected. Historical session-log entries are preserved because the log is append-only; a correction entry is appended separately.

## 2. Coverage and discovery results

The Bronze manifest contains 507 Main-namespace pages, including 150 redirects and 357 non-redirect pages.

A whole-year, word-boundary scan of raw Wikitext produced:
- 116 non-redirect pages with at least one discrete year from 2024 through 2040 (117 when redirects are included).
- 262 non-redirect pages with at least one discrete year from 2041 onward.
- 82 pages mention both periods.
- 34 mention 2024–2040 but no discrete year from 2041 onward.
- 180 mention 2041 onward but no discrete year from 2024–2040.
- 61 mention neither period.

This reproduces Claude's 262 post-2041 count and 117 pre-2041 count when redirects are included. The count is method-sensitive: Silver pages.jsonl also treats decade labels such as 2050s as year tokens, producing a larger set. The 262 count here is specifically for discrete four-digit years, not decade labels.

The 14 unledgered exact-year pages are:
97 Little Cold War; 1317 De-Extinction; 1651 Korean reunification; 1702 List of World War III weapons; 1445 President of Mexico; 272 Earth; 1796 United States presidential election, 2040; 1936 Flags of the United States; 2356 List of states and territories of the United States; 1266 Reed Chen; 2136 Tanning the Donkey: The Life and Death of the Democratic Party; 1262 Maya Garcia; 1431 Arya Kanzaki; and 1739 Terran diaspora.

The 14-page count is reproducible when decade labels are excluded. A loose regex that matches 2030s or 2040s as though they were discrete years creates false positives. The five recursive pages listed above are included because their content is relevant to dependencies, not because they satisfy the 14-page threshold.

Page 1998 is a separate candidate. It contains no discrete 2024–2040 year mentions but describes a 2156 Central Eurasian Union, an associated state of the United States, with Chelyabinsk as its capital and Samara as its largest city. Its causal relationship to the 2029 Russian dissolution is not established by the page itself.

## 3. Findings

### NA-001 — Archive SHA-256 transcription defect

**Category:** Evidence / provenance  
**Severity:** High  
**Confidence:** High  
**Classification:** Invalid checksum transcription

The uploaded archive's computed digest is the 64-character value recorded above. The 63-character variant was present in the realism-first timeline, corrected-realism audit, corrected-realism proposal, RAG evaluation set, and RAG answer-generation pass. Those five current documents have been corrected. Earlier session-log entries remain unchanged; the append-only log receives a correction note.

### NA-002 — The 2041 dependency cliff is real, but not yet classified

**Category:** Causality / chronology  
**Severity:** High  
**Confidence:** High for the page count; unresolved for dependency severity

The exact-year scan finds 262 non-redirect Main pages with at least one discrete year from 2041 onward. Eighty-two also mention 2024–2040. This establishes the scale of the post-2041 audit, not the number of pages that depend on the Flood or another retired premise.

The first link-level map is in POST-2041-LINK-DISCOVERY-001.md. It must not be mistaken for a causal graph. Each candidate requires semantic review and counterfactual testing.

### NA-003 — Fourteen exact-year pages are missing from the current claim ledger

**Category:** Evidence / audit coverage  
**Severity:** High  
**Confidence:** High

All fourteen pages listed in Section 2 are absent from claim-ledger-001.csv. They should be added to a narrative-audit inventory with an explicit unreviewed/reviewed status, not silently inserted as validated claims.

Page 1998 is a separate downstream candidate, not part of this exact-year count.

### NA-004 — Russia's 2029 transition is under-specified, not yet proven to be three incompatible accounts

**Category:** Chronology / geopolitics  
**Severity:** High  
**Confidence:** High that clarification is needed; moderate that the sequence is reconcilable

The pages describe different stages that may be compatible:
- Page 1683, Russia, revision 11554: the Russian Republic infobox starts on 16 May 2029 and names the Union State as predecessor. The prose says the Republic was founded following the collapse of the Union State and Russia's balkanization. Its prose end year is 2138 while the infobox gives 2139.
- Page 97, Little Cold War, revision 11982: says the Russian Federation formally collapsed on 14 August 2029 after a coup.
- Page 88, Timeline of major events, revision 11722: describes a 2029–2038 period of NATO/UN operations to secure nuclear stockpiles in the former Russian Federation; it refers to a future Russian Republic that refuses to surrender its stockpile.
- Page 1729, Treaty of Odessa, revision 4297: describes a 2034 treaty between Poland and Turkey concerning spheres of influence over former Russian Federation territory.

A plausible sequence is Union State collapse and successor-state formation in May, formal Russian Federation collapse in August, followed by years of nuclear-security operations and a 2034 settlement. The text does not state this sequence clearly, but the dates and mechanisms are not automatically incompatible. Reclassify Claude's NA-004 as an unresolved succession chronology, not a confirmed three-way contradiction. Preserve the 2138/2139 discrepancy.

### NA-005 — Little Cold War contains an observed-baseline NATO error and requires careful Ukraine chronology

**Category:** Geopolitics / observed history  
**Severity:** High  
**Confidence:** High for the NATO claim; moderate for several front-line details

Page 97 says Western European states withdrew from NATO in the mid-2020s. NATO's current official membership list still contains 32 members, including France, Germany, Italy, the Netherlands, Spain, and the United Kingdom. The page's withdrawal statement is not supported by the observed baseline as of 25 November 2026.

The page's Ukraine chronology is mixed:
- Russian advances at Velyka Novosilka in January 2025 are real, but ISW reporting on 26–27 January described Ukrainian holdouts and approximately 89 percent Russian control; the exact date of complete capture needs qualification.
- Toretsk was assessed as seized by Russian forces by 1 August 2025.
- Chasiv Yar was largely under Russian control by August 2025, but describing the entire town as captured is too strong; fighting and Ukrainian counterattacks continued.
- The claim that Pokrovsk was fully captured in January 2026 is broadly consistent with reporting that the last confirmed Ukrainian positions were observed on 28 January, although the exact date of complete control remains uncertain.
- The Alaska summit on 15 August 2025 and Washington meeting on 18 August 2025 occurred. They produced no peace agreement. Security guarantees and territorial concessions were discussed, but page 97 should distinguish proposals, reported positions, and political interpretation from a settled agreement.
- The US-mediated Abu Dhabi talks of 10–11 November 2026 have already occurred by the audit date. They produced progress on a prisoner exchange but no breakthrough on territory. The handoff's description of them as merely scheduled is stale.

### NA-006 — The 2024 Mexican presidential succession contradicts observed history

**Category:** Observed baseline / chronology  
**Severity:** Critical  
**Confidence:** High

Page 1445, President of Mexico, revision 11417, lists Alejandro Gutierrez as president from 1 December 2024 to 1 December 2030. The official 2024 result declared Claudia Sheinbaum Pardo president-elect with 35,924,519 votes, 59.76 percent, for the term 1 October 2024 through 30 September 2030. This is a direct pre-2041 divergence and must be corrected or explicitly reclassified as non-canon speculative material.

### NA-007 — The 2024 gastric-brooding frog de-extinction claim is false

**Category:** Science / observed baseline  
**Severity:** High  
**Confidence:** High

Page 1317, De-Extinction, revision 11002, says a true cloning success with the extinct Australian gastric-brooding frog occurred in 2024. The Lazarus Project's 2013 publication reported early-stage cloned embryos containing the extinct frog's DNA. The embryos began dividing but died within about 24 hours; the project did not produce a living frog and was eventually put on ice. This is not a successful de-extinction. Later work on living frog clones reaching tadpole stage is not the same as reviving Rheobatrachus.

The page's 2028 thylacine revival is also unsupported by the observed baseline and should not be presented as an assured pre-2041 event.

### NA-008 — Mars settlement and terraforming are a major pre-2041 dependency cluster

**Category:** Science / technology / chronology  
**Severity:** Critical  
**Confidence:** High that the current text violates the realism-first constraint

The pages do not form a consistent chronology:
- Page 1739, Terran diaspora, revision 10956, says 100 colonists settled on Mars in 2023, with 25,000 by 2030 and more than 100,000 by 2040.
- Page 318, Mars, revision 11276, calls the 2026 landing the first crewed mission to Mars, says terraforming began in 2030, and describes a 2033 magnetoshield project.
- Page 1431, Arya Kanzaki, revision 3110, assumes a 2027 Mars trip and a 400-day expedition from Mars to Titan in 2036–2038.
- The 2023 settlement claim and the 2026 first-crewed-mission claim conflict unless the pages distinguish launch, arrival, settlement, and mission type.

NASA's page updated 27 March 2026 lists Mars population as zero and gives an example round-trip mission in 2039. NASA has no formal human Mars program. The 2026 Mars landing, mass settlement, 2030 terraforming, and 2036–2038 Titan expedition are not compatible with the current baseline. The current realism-first timeline already prohibits a pre-2041 crewed Mars landing, permanent colony, and terraforming; these pages must be explicitly added to its dependency map.

### NA-009 — Caribbean annexation is directly tied to retired Flood premises and has internal date conflicts

**Category:** Geopolitics / causality / chronology  
**Severity:** High  
**Confidence:** High that the dependency exists; moderate on each future political outcome

Page 1366, Caribbean annexation, revision 11800, links the 2035 annexation sequence to the Flood, sea-level rise, displacement, and hurricane effects. It also describes a 2026 US launch complex in Guyana and a free-association arrangement. Publicly documented US–Guyana agreements in 2026 concern security cooperation, liaison officers, and an enhanced defense partnership; the public sources reviewed do not substantiate a space launch complex or free association.

The territorial sequence is repeated across pages 272, 2356, and 1936. Puerto Rico's date differs:
- Page 2356 gives 27 June 2029 as the statehood date.
- Page 1936 changes the flag to 51 stars on 4 July 2029, which could be a flag-effective date.
- Page 272 gives 27 February 2030.
The 2030 date is inconsistent with the other two unless it describes a different legal milestone. The 2035 Guyana and 2037 Caribbean admissions are extraordinary geopolitical developments and need a credible, independent causal chain; they cannot inherit the removed Flood as an unexplained universal cause.

### NA-010 — US party-system continuity is unresolved across future political biographies

**Category:** Political institutions / continuity  
**Severity:** High  
**Confidence:** High that the page set is inconsistent; resolution pending

The pages give different party histories:
- Page 2136, Tanning the Donkey, revision 11203, describes Democratic Party fragmentation beginning in 2024, a Progressive victory in 2029, and the formation of a Conservative Party from party remnants.
- Page 1262, Maya Garcia, revision 11753, describes her as a Democrat through 2060 and as the first president from the Liberal caucus of the Democratic Party.
- Page 1796, United States presidential election, 2040, revision 11058, identifies Garcia as the Liberal nominee and says she became the first president of the Conservative Party.
- Page 1266, Reed Chen, revision 11778, records a Liberal Party affiliation beginning in 2033 and describes the 2040 election as the party's first White House win.

These descriptions require a single party-system chronology. Do not assume that a 2040 election result and a 2045–2049 presidential term are inherently contradictory: Garcia could have won in 2040 and been re-elected in 2044. The party labels, however, are not reconciled. The 2040 result also gives Garcia 43.2 percent while the infobox says 51 percent was needed, with no electoral-vote or state result to explain the outcome. The policy for assigning future deaths and offices to real people remains a maintainer decision.

### NA-011 — Trump-Russia scandal page misstates the Mueller findings and the 2024 immunity ruling

**Category:** Observed baseline / legal institutions  
**Severity:** High  
**Confidence:** High

Page 961, Trump-Russia scandal, revision 11717, says Mueller uncovered a conspiracy between the Trump organization and the Kremlin. The Mueller report states that the investigation did not establish that members of the Trump campaign conspired or coordinated with the Russian government in its election-interference activities. The page's claim is a direct observed-baseline error.

The page also describes the July 2024 Supreme Court decision as a ruling that presidents could not be prosecuted for official actions. That is overbroad. Trump v. United States held absolute immunity for acts within the President's exclusive constitutional authority, at least presumptive immunity for other official acts, and no immunity for unofficial acts. The page needs to preserve those distinctions.

### NA-012 — Hypersonic and orbital-strike claims require technology correction

**Category:** Technology / military realism  
**Severity:** High  
**Confidence:** High for the 2021 US fielding problem; moderate for the 2027 forecast

Page 1702, List of World War III weapons, revision 11938, lists a US BGM-711 Scorpion hypersonic cruise missile in service from 2021. Page 1234, Hypersonic Weapons, revision 9496, describes an AGM-25 Scorpion as the first operational hypersonic cruise missile in 2027. These entries require identification and reconciliation.

GAO's 2026 assessments show that US hypersonic programs were still undergoing delayed testing and fielding. The Army's first LRHW battery was delayed into 2026; the Navy's Conventional Prompt Strike shipboard flight testing was pushed to 2027; the Air Force's HACM remained in prototype/testing stages. This makes a US operational hypersonic cruise missile in 2021 unsupported by the observed baseline. A 2027 operational date is also more aggressive than the public test schedule and needs qualification.

Page 1234 also asserts that the US conducted a space-to-Earth orbital kinetic weapon test on 18 July 2020. CSIS's open-source assessments state that there were no open-source examples of a space-based global-strike weapon being tested. A 2026 US disclosure of weapons in orbit does not establish that the systems are kinetic or that a 2020 orbital bombardment test occurred. Treat the specific 2020 claim as unsupported, not as a verified historical event.

Page 1234 places a Mexican orbital-weapon deployment in 2028 in a section discussing the Mexican Vacuum Command's emergence in 2113. This is an apparent chronology inversion, likely a typo, but must remain unresolved until the authorial intent is established.

### NA-013 — Orbital Command Stations and tactile-neural interfaces add untracked pre-2041 technology dependencies

**Category:** Technology / institutions  
**Severity:** High  
**Confidence:** Moderate

Page 1479, Orbital Command Stations, revision 11985, describes a 2033 approval, 2037 construction at Tycho Base, and 2040 deployment. The scale of lunar infrastructure, orbital construction, crew, power, concealment, and military command capability needs a feasibility review. It is not currently represented as a discrete item in the realism-first timeline.

Page 1436, Tactile-neural interface, revision 3714, describes mass-market entertainment integration by 2028 and sensory feedback by 2034, followed by later brain-to-machine skill transfer. In 2026, BCIs are progressing rapidly, including a first commercial implantable device approved in China for hand-movement assistance in people with paralysis. This does not establish mass-market tactile interfaces or the uploading/downloading of skills. Preserve the distinction between assistive motor control, sensory feedback research, and cognitive enhancement.

### NA-014 — Korean reunification depends on the Great Famine, but the chronology is not strictly cause-after-effect

**Category:** Geopolitics / causality / demographics  
**Severity:** High  
**Confidence:** Moderate

Page 1651, Korean reunification, revision 8584, says the North Korean regime began to falter in December 2026 after China cut aid in anticipation of the 2027 Famine. Because a state can act in anticipation of a predicted famine, this is not automatically a cause-after-effect error. The actual problem is the unsupported scale and missing intermediate steps: 11 million deaths, mass defections, a 40-country intervention, South Korean occupation, and reunification in 2031.

Pages 1715 Korea and 3484 New Korean Wave are downstream dependencies. The Korean chain requires its own institutional, military, humanitarian, nuclear-security, and regional-agency analysis; it cannot be left as a simple consequence of a global famine.

### NA-015 — Japanese resurgence and Eurasian security architecture lack a disposition

**Category:** Geopolitics / chronology  
**Severity:** High  
**Confidence:** Moderate

Page 88 describes Japanese resurgence in 2039–2048, including a hypersonic demonstration in 2039, extraterritorial districts in Chita and Kamchatka, and US support for nationalist movements in China and Taiwan. Page 1438, Eurasian Coalition, revision 10183, describes a 2046 coalition involving former Russian states, Turkey, Poland, Japan, and the United States, alongside a Turkish occupation/pipeline story. Page 1729's 2034 Treaty of Odessa may be an intermediate step.

This is a potentially coherent post-Russia security architecture, but the transition from 2029 collapse through 2034 treaty, Turkish occupation, and 2046 coalition is underdeveloped. The current realism-first timeline already rejects a rapid Turkish occupation of Arabia and an Arctic-to-Bosporus pipeline. The 2039–2040 Japanese items need explicit dispositions.

### NA-016 — Central Eurasian Union is a post-2041 candidate, not a proven Russian-collapse dependent

**Category:** Geopolitics / future state system  
**Severity:** Medium  
**Confidence:** Low–moderate

Page 1998, Central Eurasian Union, revision 10824, describes a 2156 associated state of the United States with Chelyabinsk as capital and Samara as largest city. It is a useful candidate for the post-2041 state-system map, but the page itself does not establish a direct causal link to the 2029 Russian collapse. Keep the relationship unresolved until neighboring successor-state pages are reviewed.

## 4. Post-2041 dependency discovery

The initial link-level counts are recorded in POST-2041-LINK-DISCOVERY-001.md. Examples include 20 future-dated pages linking to The Flood, 27 linking to Mars, 10 to The Refreeze, 7 to Earth Working Group, and 8 each to Great Reset and White Tide.

These are explicit link counts, not causal-dependency counts. A linked page may be a cultural reference, summary, or incidental mention. Conversely, a page may depend on an event without linking to it.

## 5. External sources checked

- Mexico, TEPJF, 14 August 2024: final result and president-elect declaration for Claudia Sheinbaum, 59.76 percent, term 1 October 2024–30 September 2030: https://www.te.gob.mx/portal/front3/bulletins/detail/25895/0
- Mexico, INE, 9 June 2024: official computation transcript: https://central-preprod.ine.mx/2024/06/09/version-estenografica-de-la-sesion-extraordinaria-del-consejo-general-9-de-junio-de-2024/
- NATO, current member countries: https://www.nato.int/en/what-is-nato.html
- US Department of Justice, Mueller report: https://www.justice.gov/archives/sco/file/1373816/dl
- US Supreme Court, Trump v. United States, 23-939, 1 July 2024: https://www.supremecourt.gov/opinions/23pdf/23-939_e2pg.pdf
- ABC News, Project Lazarus gastric-brooding frog, 6 September 2025: https://www.abc.net.au/news/science/2025-09-06/gastric-brooding-frog-project-lazarus-deextinction/105494672
- UNSW, early-stage cloned embryos of extinct frog, 15 March 2013: https://www.unsw.edu.au/newsroom/news/2013/03/scientists-produce-cloned-embryos-of-extinct-frog
- NASA, Humans to Mars, page updated 27 March 2026: https://www.nasa.gov/humans-in-space/humans-to-mars/
- GAO, Navy Ship Modernization / Conventional Prompt Strike, 17 July 2026: https://www.gao.gov/products/gao-26-107974
- GAO, Weapon Systems Annual Assessment 2026: https://www.gao.gov/assets/gao-26-108457.pdf
- CSIS, International Perspectives on Space Weapons, 2020: https://aerospace.csis.org/wp-content/uploads/2020/05/Harrison_IntlPerspectivesSpaceWeapons-compressed.pdf
- CSIS, Space Threat Assessment 2025: https://www.csis.org/analysis/space-threat-assessment-2025
- Nature Biotechnology, China approves brain chip to overcome paralysis, 17 April 2026: https://www.nature.com/articles/s41587-026-03101-8
- Guyana Department of Public Information, Enhanced Defense Partnership with the United States, 21 October 2026: https://dpi.gov.gy/press-release-president-ali-and-u-s-secretary-of-war-hegseth-sign-joint-declaration-to-enhance-defense-partnership/

Russia/Ukraine battlefield checks used Institute for the Study of War assessments dated 26–27 January 2025, 1 August 2025, and 25 February 2026, plus contemporary reporting on the August 2025 Alaska/Washington meetings and the 10–11 November 2026 Abu Dhabi talks. The relevant claims remain differentiated in NA-005 rather than being treated as one settled chronology.

## 6. Progress and limitations

| Metric | Result |
|---|---:|
| Pages discovered | 507 Main pages |
| Pages inventoried | 507 |
| Pages semantically reviewed | 28 at varying depth: 19 full, 9 partial |
| Pages hash-verified | 28/28 |
| Claims/findings recorded | 16 numbered findings, with multiple subclaims |
| External issue clusters checked | 12 |
| Causal relationships evaluated | Initial qualitative pass; no complete causal graph |
| Regions completed | 0 of 11; Russia/Eurasia partial |
| Contradictions or material conflicts documented | 10+; several unresolved |
| Final retcons approved | 0 |

Unaudited work includes most of the 262 post-2041 pages, most of the corpus, nine regional audits, the full technology/institutions review, and the narrative-quality assessment.

## 7. Next tranche

1. Build the post-2041 page inventory and classify the 262 pages in bounded batches, beginning with Flood, Mars, Great Famine, Russia, and US territorial expansion dependencies.
2. Continue the observed-baseline sweep across all pages that state 2022–2026 events.
3. Complete the Russia/Eurasia chain: 97, 1683, 1729, 1438, 1998, 961, and related successor-state, Turkish, Polish, and Japanese pages.
4. Reconcile the US party-system and election chronology.
5. Return to the Great Famine / Market Crash / Revolutions / Great Reset cluster.

No canon edits, source data edits, manifest changes, RAG implementation changes, tests, builds, or PR/merge actions were performed in this tranche.
