# Narrative audit — validation tranche 002

**Status:** Completed bounded validation and expanded ledger-gap inventory; narrative audit remains in progress  
**Repository:** robertmccarn/SR-Doc  
**Branch:** `experiment/corrected-realism`  
**Starting HEAD:** `cbde12c17c507a74f3220858481a0930740e4f59`  
**Audit date:** 2026-11-25  
**Primary source:** uploaded `SR-Doc-Audit.zip`, SHA-256 `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`

## 1. Scope and safeguards

This tranche independently checked the material new claims in Claude's read-only report, reopened the pages Claude had identified as unread where they intersected the current audit, expanded the exact-year ledger gap from the prior 14-page threshold set to the complete 43-page set, and checked selected 2025–2026 observed-baseline claims against public primary or high-quality sources.

The work is read-only with respect to source lore. No accepted canon, Bronze/Silver Wikitext, manifests, or RAG implementation was changed. No tests, builds, or RAG CLI runs were performed. No PR, merge, or branch promotion was created.

The Bronze archive remains the evidence authority. The 43 pages in the expanded inventory were individually re-hashed from their raw archive bytes; **43/43 matched** their manifest `raw_sha256` values. Exact IDs, titles, revisions, hashes, paths, year counts, and dispositions are in [claim-ledger-gap-002.csv](claim-ledger-gap-002.csv).

## 2. Reconciled claim-ledger gap

### Method

Scanned the 357 non-redirect Main-namespace Wikitext pages in `bronze/manifests/pages.json` and their referenced raw files. A qualifying year is a standalone four-digit token from 2024 through 2040, using:

```regex
(?<![A-Za-z0-9])(?:202[4-9]|203[0-9]|2040)(?![A-Za-z0-9])
```

This excludes decade labels such as `2030s` and `2040s`. The existing `claim-ledger-001.csv` has 243 grouped observations across 107 distinct page IDs; three IDs are redirects, leaving 104 represented non-redirect Main pages.

### Results

| Measure | Result |
|---|---:|
| Main namespace | 507 pages |
| Non-redirect Main pages | 357 |
| Pages with at least one standalone 2024–2040 year | 116 |
| Those pages represented in claim ledger 001 | 73 |
| **Unrepresented pages** | **43** |
| Unrepresented pages with 1 mention | 17 |
| Unrepresented pages with 2 mentions | 12 |
| Unrepresented pages with 3+ mentions | 14 |
| Previously identified 3+ mention subset | 14 |
| **Additional pages beyond prior subset** | **29** |
| Raw hashes matched for all 43 gap pages | 43/43 |

This reproduces Claude's revised count. The prior 14-page result was not the full gap; it was the subset meeting a three-mention threshold. The 43-page list is a discovery inventory, not a declaration that every page contains a material, incorrect, or causally dependent claim. Several pages contain future-person biographies or extraterrestrial-local chronology, and those are not automatically equivalent to Earth-history divergence.

The 29 additional pages received a targeted review of every qualifying year-bearing context and relevant page framing. This is not a claim that all 29 received a full semantic read. The existing tranche-001 review depth for the original 14 is preserved rather than overwritten.

## 3. Independent review of Claude's findings

### NA-003 — 43-page ledger gap

**Confirmed.** The standalone-year scan reproduces 116 pages, of which 73 are already represented and 43 are not. The complete page list and provenance are in the CSV. The original 14 are a subset; 29 more pages must be assessed. Do not insert all 43 into the substantive claim ledger as if they were validated claims. First classify each page's actual claim and review depth.

### NA-004 — Russia's 2029 succession chronology

**Mostly confirmed; unresolved.** Page 1683 (`Russia`, rev. 11554) starts the Russian Republic on 16 May 2029 and names the Union State as predecessor. Page 97 (`Little Cold War`, rev. 11982) places formal Russian Federation collapse on 14 August 2029. A staged sequence remains possible, but the source text does not clearly distinguish the Union State from the Russian Federation, and other material calls the predecessor the Eurasian Union. Preserve the date and naming conflict. Do not describe it as reconciled.

### NA-005 — NATO and the 2025–2026 observed baseline

**Core correction confirmed; Claude's added context is materially important.** NATO's official current membership list still contains 32 members. No Western European state withdrawal from NATO is evidenced by the sources reviewed. The page-97 claim that Western European countries withdrew is therefore false as an observed-baseline claim.

The alliance is nevertheless under substantial US-origin stress:
- The 2026 Iran war produced public criticism by President Trump of allies that declined to join US/Israeli operations or help reopen the Strait of Hormuz. Some European allies restricted US access, basing, or overflight for offensive operations.
- In April 2026 Trump said he was strongly considering US withdrawal from NATO. The July 2026 CRS report records that statement and the statutory restriction on unilateral presidential withdrawal.
- US force posture in Europe was reduced: a December 2025 change removed one rotational brigade combat team and one division headquarters; a May 2026 deployment cancellation reduced the in-theater brigade count. CRS recorded approximately 86,000 US personnel assigned or deployed to NATO countries in Europe in March 2026. A further force-posture review was announced.
- Greenland rhetoric created a second alliance stress point. Trump publicly pressed for US control of Greenland and did not initially rule out force. By November 2026, however, Denmark and Greenland had ratified a September security agreement that expands US military access while reaffirming Danish sovereignty and Greenlanders' right to self-determination.

**Editorial implication:** page 97's broad thesis of alliance stress/decline may be retained as a scenario, but its mechanism must be rebuilt. The observed pressure runs through US policy, force posture, Iran-war disagreements, and Greenland—not Western European exits from NATO. Distinguish alliance membership, Article 5 credibility, US presence, access/basing rights, and political trust; they are not interchangeable.

### NA-006 — Mexico's 2024 succession

**Confirmed.** The source page's Alejandro Gutierrez succession is incompatible with the observed 2024 result and Claudia Sheinbaum's inauguration. The original official-election source used in tranche 001 remains the correct verification basis.

### NA-007 — Gastric-brooding frog and thylacine

**Frog finding confirmed; Claude's correction about "put on ice" is itself incorrect.** The 2025 ABC account says the gastric-brooding frog embryos began dying within 24 hours, repeated attempts failed, and Project Lazarus was put back on ice after several more unsuccessful years. Thus the phrase "put on ice" is supported, although it does not prove the researchers have permanently abandoned the idea. No living gastric-brooding frog was produced.

The 2028 thylacine claim is a future forecast, not a false observed-history claim. Colossal's published process describes multiple unfinished steps—comparative genome work, cell lines, hundreds of gene edits, embryo creation, surrogacy, gestation, and maturation—and speaks of a goal "within the next decade," not a verified 2028 birth. Classify 2028 as unsupported and highly uncertain, not already disproven.

### NA-008 — Mars and outer-planet chronology

**Confirmed and expanded.** Pages 318 (`Mars`, rev. 11276) and 1431 (`Arya Kanzaki`, rev. 3110) were re-opened. Page 1739 still conflicts internally by describing 100 colonists on Mars in 2023 while also saying settlement starts in 2024. It then projects 25,000 by 2030 and more than 100,000 by 2040. Page 318 gives a 2026 first crewed mission and 2030 terraforming; page 1431 assumes a 2027 Mars trip and a 2036–2038 Mars-to-Titan expedition.

The 29-page gap review adds:
- Page 1405: a 2033 human Jupiter/Callisto expedition and settlement.
- Page 1426: a 2036 crewed Saturn mission.
- Page 2127: a 2031 Mars colony and 2039 space elevator.
- Page 3662: a 2037 Mars research facility.
- Page 1685: a 2035 Earth space elevator and 2038 trans-American rail system.

NASA's current public material treats human Mars as a difficult future program, not an existing settlement. NASA's Strategic Analysis Cycle 2021 architecture studied a roughly 2039 departure opportunity and a 760–850-day round trip. The National Academies' 2022 decadal survey describes human Mars planning in the late 2030s. These are planning studies, not evidence of a 2023–2027 landing or mass colonization. NASA's Europa Clipper materials describe Jupiter's radiation environment as exceptionally hazardous; NASA's Saturn exploration page lists robotic missions, not a crewed Saturn program. A crewed Jupiter/Saturn expedition by 2033–2036 is not a credible pre-2041 scenario.

### NA-009 — Caribbean annexation and Guyana

**Dependency and date conflicts confirmed; absence claims remain bounded.** Page 1366 (`Caribbean annexation`, rev. 11800) was re-opened. It links the territorial sequence to Flood/displacement premises and describes a Guyana launch complex/free-association pathway. Public Guyanese sources reviewed document security cooperation, EEZ surveillance, counter-cartel cooperation, and an enhanced defence partnership; they do not substantiate the claimed space-launch complex or free-association arrangement. This is an absence-of-public-corroboration finding, not proof that no private proposal exists.

Puerto Rico's three dates remain unresolved: 27 June 2029 (page 2356), 4 July 2029 (page 1936, potentially flag-effective date), and 27 February 2030 (page 272). Do not silently choose one.

### NA-010 — US presidential and party chronology

**Direct contradiction confirmed; wider cluster discovered.** Page 214 (`President of the United States`, rev. 11892) lists Dylan J. Price as the 49th president from 20 January 2037 to 20 January 2045, and Maya Garcia as the 50th from 20 January 2045 to 20 January 2049. Page 1796 says Garcia won the 2040 election and succeeded Price. Page 1797 treats Garcia as the incumbent before the 2044 election. Page 1262 calls Garcia the 49th president; page 1266 calls Reed Chen the 52nd, while page 214 numbers him 53rd. Party labels also vary between Democratic, Liberal, and Conservative.

The new gap review adds page 1136 (`Liberal Party (United States)`, rev. 11713), whose prose says the party was founded in 2029 while its infobox says 2052. Pages 2135 and 2136 introduce fictional books as publications in 2024 and the 2030s, respectively, and pages 2136/2451 repeat the future party-system narrative.

The earlier suggestion that Garcia could have won in 2040 and been re-elected in 2044 does not resolve page 214's 2037–2045 Price term or page 1797's incumbent assumption. This remains a maintainer-level chronology decision; preserve all competing values.

### NA-011 — Trump-Russia wording

**Claude's qualification is accepted provisionally.** Page 961's wording about Mueller and Michael Flynn is more ambiguous than the earlier tranche paraphrase suggested; it does not literally state a proven Trump–Kremlin conspiracy in the direct terms previously attributed to it. The Supreme Court immunity summary remains overbroad. The DOJ report and Supreme Court opinion were not re-fetched in this tranche, so this is a wording correction, not a new legal-source verification.

### NA-012 — Hypersonic weapons and mismatched GAO evidence

**Evidence mismatch confirmed; current HACM status updated.** The earlier GAO Navy Conventional Prompt Strike citation is not evidence about the Raytheon air-launched HACM program. GAO-26-108457 is the relevant 2026 assessment: it says HACM had effectively zero schedule margin, had reduced its rapid-prototyping flight plan from seven to five tests, and needed at least the first three tests to inform a FY2027 rapid-fielding/procurement decision.

The first HACM flight-test release was subsequently confirmed by the Air Force on 6 October 2026. The service still aims to begin fielding in FY2027, but that is a program goal with substantial schedule and test risk—not proof that a weapon was already operational in 2021 or that the fictional AGM-25 Scorpion designation is real. Page 1702's Northrop Grumman BGM-711 Scorpion service date of 2021 remains unsupported/contradicted by the public baseline. Keep the claimed July 2020 orbital strike unsupported absent corroboration.

### NA-013 — Tactile-neural interface

**Partially confirmed; terminology needs decomposition.** Page 1436 (`Tactile-neural interface`, rev. 3714) was re-opened. Current research supports distinct capabilities: non-invasive BCI signal decoding; invasive clinical BCI trials for communication/motor control; limited sensory feedback through cortical stimulation in small clinical cohorts; and external haptic gloves that create force/tactile cues without neural implantation. A 2028 consumer device may plausibly combine simple non-invasive control with external haptics, but that is not equivalent to a high-bandwidth neural interface or immersive, direct sensory writing into the brain. The 2034 claim needs a precise definition of input/output pathway, invasiveness, resolution, latency, safety, clinical indication, and commercial availability.

### NA-014 — Korean reunification chain

**Dependency confirmed; DPRK baseline still unresolved.** Pages 1715 (`Korea`, rev. 10807) and 3484 (`New Korean Wave`, rev. 11014) were re-opened. Page 1715 places reunification in 2029–2031; page 3484 treats the post-reunification cultural wave as a 2031 consequence. These depend on the Great Famine/regime-collapse chain in page 1651 unless a separate trigger is established. The December 2026 DPRK baseline was not independently researched in this tranche.

### NA-015 — Treaty of Odessa and Eurasian Coalition

**Direct dependency confirmed.** Page 1729 (`Treaty of Odessa`, rev. 4297) is a 2034 treaty over former Russian Federation territory. Under the binding rule that the Russian Federation remains intact through 2040, this 2034 premise cannot stand as written. It must be removed, rewritten around a credible non-dissolution mechanism, or moved after 2041. Page 1438 (`Eurasian Coalition`, rev. 10183) is a separate 2046–2055 post-divergence alliance and may survive only if its successor-state architecture is re-seeded after 2041.

### NA-016 — Central Eurasian Union

**No direct Russian-dissolution dependency found in the source page.** Page 1998 (`Central Eurasian Union`, rev. 10824) was read. It describes a 2156 associated state of the United States with Chelyabinsk as capital and Samara as largest city. It does not state that it is a successor to, or territorially dependent on, the 2029 Russian Republic. Do not infer causal succession from the name alone. Classify as independent/unresolved pending neighbouring-page review, not as a demonstrated Russian-collapse dependency.

## 4. Disposition of the 29 additional gap pages

| Page IDs | Initial reading |
|---|---|
| 317, 1372, 1375, 1377, 1537, 1750, 2235 | Future-person biographies/birth years; no immediate contradiction found in the date-bearing context. Retain as contingent character projections, not observed facts. |
| 964 | 2027 VR-market crash; a contingent scenario requiring mechanism, not an observed fact. |
| 1111 | 2039 mass armour/drone conflict and associated technology; linked to the retired Russian-collapse sequence and requires a full technology/logistics audit. |
| 1136 | Liberal Party founded 2029 in prose versus 2052 in infobox; direct internal date contradiction. |
| 1405, 1426 | Human Jupiter/Callisto 2033 and Saturn 2036 missions; incompatible with a credible pre-2041 space program. |
| 1436 | 2028 mass-market TNI and 2034 sensory feedback; distinguish non-invasive BCI, implantable BCI, and external haptics. |
| 1685, 2127 | Space elevators in 2035/2039; CNT fiber manufacturing and tether-scale reliability remain far from a demonstrated elevator system. |
| 1696 | 2029 future publication and postnaturalism movement; possible as a contingent publication, but its de-extinction context must not be treated as an accomplished 2024 breakthrough. |
| 1715, 3484 | 2029–2031 Korean reunification and downstream cultural consequence; direct dependency on the unresolved famine/regime-collapse chain. |
| 1718 | 2039 Turkish election/political projection; 2044 presidency is post-divergence. No immediate internal conflict identified in the reviewed date context. |
| 1739, 1431, 2127, 3662 | Mars settlement, missions, or facility before 2041; direct conflicts with the approved realism-first space envelope. |
| 1749, 3673 | Extraterrestrial-local chronologies expressed in CE years; no Earth-event dependency established by the reviewed pages. |
| 1797 | 2044 election treats Garcia as incumbent; conflicts with the 2045 start date in page 214. |
| 2135 | Fictional nonfiction book presented as published in 2024; an invented past publication in the observed period. Requires removal/re-dating or explicit non-Earth/fictional framing. |
| 2136, 2451 | Party-system narrative and 2032 election; overlaps the unresolved 2029/2040/2044 US political chronology. |
| 3099 | 2029 transfer of the ISS from low Earth orbit to geostationary orbit; requires a propulsion, mass, energy, and mission architecture not supplied by the page. |
| 3494 | 2035 Serbia/Bosnia territorial change; no credible mechanism or international response is supplied. |
| 3651 | 2031 Hong Kong independence; a major geopolitical rupture with no causal or institutional mechanism supplied. |

This table is an initial disposition, not a full semantic audit of all 29 pages. Future-person biographies and extraterrestrial calendars are intentionally not treated as equivalent to observed Earth-history claims.

## 5. Selected 2025–2026 observed-baseline update

The realism-first timeline currently needs a more complete observed-baseline layer. This tranche verified the following relevant context:

- **NATO membership:** 32 members remain on NATO's official list.
- **Iran and NATO:** allies differed over participation in the 2026 Iran conflict and Hormuz security; some denied or restricted operational access. Trump publicly criticized the refusals and, in April, said he was strongly considering withdrawal. CRS records the statement and the statutory constraint on unilateral withdrawal.
- **US force posture:** the US reduced rotational force posture in Europe and canceled a planned Poland brigade rotation. This is a real shift in US posture, not evidence of Western European NATO exits.
- **Greenland:** the 2026 dispute strained alliance trust. The September security agreement and November ratifications expanded US access while preserving Danish sovereignty and Greenlandic self-determination. Treat the outcome as a negotiated security arrangement, not annexation.
- **Guyana:** public 2025–2026 documents describe defense/security cooperation, EEZ surveillance, and counter-cartel coordination. They do not corroborate the page's launch-complex/free-association sequence.
- **Space:** NASA and National Academies sources describe Mars as a future, high-risk program, with 2039 appearing as a study opportunity—not a completed 2020s settlement. NASA's Saturn record is robotic; Jupiter's radiation environment is severe.
- **Materials:** 2025 reviews show progress in CNT fibers but identify macro-scale strength, defect control, production consistency, and radiation durability as unresolved barriers. Space-elevator tethers remain conceptual.
- **BCI/haptics:** clinical implantable BCI, non-invasive BCI, and external haptic feedback are distinct technical categories. None supports a mass-market, high-fidelity direct neural sensory interface as a demonstrated 2028 product.
- **HACM:** the first flight-test release occurred in October 2026, but a FY2027 fielding target remains high-risk.
- **De-extinction:** the frog project remains an unsuccessful embryo experiment put on ice; the thylacine project remains a multi-stage research program without a verified 2028 birth.

### External references checked

- NATO member list: https://www.nato.int/en/about-us/organization/nato-member-countries
- CRS, *NATO: Issues for the July 2026 Ankara Summit*: https://www.everycrsreport.com/files/2026-07-02_R49018_36b5027ccd45ed7627059a87f7eb70c21b46b299.pdf
- Operation Atlantic Resolve, Lead IG report, Apr–Jun 2026: https://oig.usaid.gov/sites/default/files/2026-11/OAR_Q3_Jun2026_Final_508.pdf
- Stars and Stripes, US troop levels/possible cuts, 15 Nov 2026: https://www.stripes.com/theaters/europe/2026-11-15/us-troop-levels-europe-eucom-nato-23470991.html
- Reuters, Iran operation/NATO allies, 17 Mar 2026: https://www.reuters.com/world/middle-east/nato-countries-dont-want-get-involved-iran-operation-trump-says-2026-03-17/
- Reuters, Greenland agreement ratification, 19 Nov 2026: https://www.reuters.com/world/denmark-expected-ratify-trump-deal-over-greenland-thursday-2026-11-19/
- Guyana DPI, EEZ security cooperation, 25 Mar 2026: https://dpi.gov.gy/guyana-strengthening-eez-security-through-us-partnership-pres-ali-says/
- NASA, Humans to Mars: https://www.nasa.gov/humans-in-space/humans-to-mars/
- NASA, Strategic Analysis Cycle 2021 Mars architecture: https://ntrs.nasa.gov/citations/20220002632
- National Academies, Mars planning in the late 2030s: https://uwnxt.nationalacademies.org/read/26522/chapter/21
- NASA, Saturn exploration: https://science.nasa.gov/saturn/exploration/
- NASA, Europa Clipper radiation environment: https://science.nasa.gov/wp-content/uploads/2024/09/europa-clipper-press-kit.pdf
- ACS Central Science, CNT fiber barriers and space-elevator concept: https://pmc.ncbi.nlm.nih.gov/articles/PMC12203435/
- Nature Reviews Bioengineering, clinical implantable BCI trials: https://www.nature.com/articles/s44222-024-00239-5
- Trends in Neurosciences, non-invasive BCI review (2026): https://www.sciencedirect.com/science/article/pii/S0166223626000809
- International Journal of Human-Computer Studies, VR kinesthetic gloves (2025): https://doi.org/10.1016/j.ijhcs.2025.103507
- ABC, gastric-brooding frog Project Lazarus (6 Sep 2025): https://www.abc.net.au/news/science/2025-09-06/gastric-brooding-frog-project-lazarus-deextinction/105494672
- Colossal, thylacine process: https://colossal.com/thylacine/
- GAO-26-108457, HACM: https://www.gao.gov/assets/gao-26-108457.pdf
- Air & Space Forces Magazine, first HACM flight-test release (6 Oct 2026): https://www.airandspaceforces.com/air-force-first-flight-test-hypersonic-attac-cruise-missile/

## 6. Corrections and unresolved items carried forward

1. **Supersede the 14-page gap as a complete-coverage metric** with the 43-page standalone-year inventory. Keep the original 14 as a threshold subset and historical tranche result.
2. **Do not update the claim ledger as though all 43 are adjudicated.** Use the gap CSV as the discovery queue; promote only extracted claims with evidence and status.
3. **Correct the previous frog wording:** "put on ice" is supported by the 2025 ABC account; it means paused, not necessarily permanently abandoned.
4. **Correct the BCI framing:** separate non-invasive BCI, implantable BCI, cortical sensory feedback, and external haptics.
5. **Reconcile the US party chronology** across pages 214, 1262, 1266, 1136, 1796, 1797, 2135, 2136, and 2451 without choosing a convenient version.
6. **Rebuild the Russia-to-Odessa chain** under the no-dissolution-before-2041 constraint; keep the 2029 naming/date sequence unresolved.
7. **Re-seed the post-2041 Eurasian Coalition** independently if it is to survive; page 1998 does not establish a direct Russian predecessor relationship.
8. **Split the Russia hard prohibition into graded cases:** a domestic regime/constitutional crisis is improbable but not impossible; rapid state dissolution and foreign seizure of nuclear stockpiles are much less plausible and need distinct treatment.
9. **Add an observed 2025–2026 geopolitical baseline** to the editorial timeline in a later focused update. Do not treat the limited baseline in this tranche as a complete global review.
10. Continue the broader 2019–2026 historical-claim sweep; the 43-page scan is a year-token discovery queue, not a substitute for that sweep.

## 7. Progress and limitations

| Metric | Result |
|---|---:|
| Non-redirect Main pages | 357 |
| Pages with standalone 2024–2040 years | 116 |
| Represented in claim ledger 001 | 73 |
| Gap pages | 43 |
| Original ≥3-mention subset | 14 |
| Additional gap pages | 29 |
| Gap-page hashes matched | 43/43 |
| Additional pages with targeted date-context review | 29/29 |
| Pages receiving full semantic review in this tranche | 0 |
| Previously unread priority pages reopened | 9 |
| New independent finding groups | 12 |
| Regions completed | 0 of 11 |

The nine priority pages reopened were 1366 Caribbean annexation, 318 Mars, 1431 Arya Kanzaki, 1436 Tactile-neural interface, 1998 Central Eurasian Union, 2136 Tanning the Donkey, 1715 Korea, 3484 New Korean Wave, and 2774 Project Rebirth. Other 43-page candidates were read at targeted year-context depth, not full narrative depth.

No source lore, canon, Bronze/Silver data, manifests, or RAG implementation was modified. No automated tests, builds, or RAG CLI runs were executed. No PR, merge, or branch promotion occurred.
