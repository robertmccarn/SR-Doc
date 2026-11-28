# SR-Doc — Agent Swap / Current Working State

**Repository:** robertmccarn/SR-Doc  
**Working branch:** experiment/corrected-realism  
**Historical HEAD marker (before an earlier swap refresh; not current):** aff0e114531a4a50fc62b411beb2934279fec0d6  
**Last verified:** 2026-11-27  
**Current workstream:** Narrative audit tranche 002 complete; chronology proposal register 001 created as non-canon conversation-origin material; independent review pending before tranche 003. The 43-page gap inventory is established; the full semantic audit and post-2041 dependency map remain in progress.

## Start here

Read in this order:
1. `agents.md`
2. this file
3. `research/continuity/DOCUMENTATION-GOVERNANCE.md`
4. `research/continuity/MASTER-RESEARCH-REGISTER.md`
5. `research/continuity/chronology-proposal-register-001.md`
6. `research/README.md`
7. `research/narrative-audit/MASTER-NARRATIVE-AUDIT.md`
8. `research/narrative-audit/validation-tranche-002.md`
9. `research/narrative-audit/claim-ledger-gap-002.csv`
10. `research/narrative-audit/validation-tranche-001.md`
11. `research/narrative-audit/POST-2041-LINK-DISCOVERY-001.md`
12. `research/continuity/realism-first-timeline-2024-2040.md`
13. `research/session-log.md`

The repository is the source of truth. Verify Git state and current file versions before acting.

## Governing editorial constraint

There must be no departure from authentic real-world scientific, technological, demographic, economic, institutional, military, or geopolitical plausibility through 2040-12-31. Deliberate divergence may begin in 2041 or later, but later developments must remain causally and physically coherent.

Climate is one factor among many, not a universal master cause. Evaluate institutions, demographics, supply chains, technology, energy/minerals, finance, military competition, trade, culture/information, public health, geography, and regional agency.

Distinguish observed history, forecast, scenario assumption, inference, hypothesis, and unresolved claim. Preserve contradictions; do not silently reconcile them. A wiki link or year mention is not proof of causality.

## Operational boundaries

- Work only on `experiment/corrected-realism` unless the maintainer explicitly changes the instruction.
- This is a non-canon editorial branch.
- Do not modify accepted canon, Bronze/Silver source data, manifests, or RAG implementation without explicit authorization.
- Research and audit documentation may be updated under `DOCUMENTATION-GOVERNANCE.md`.
- Do not create/merge PRs, merge branches, or promote this branch without explicit approval.
- Never claim tests, builds, RAG CLI runs, or validations that were not actually executed.
- Use Bronze Wikitext as primary evidence; use Silver for navigation and parsed metadata.
- When the user requests corpus-page tranches, use the established 300-page batch size. The current narrative audit is a bounded thematic workflow.
- Update master register, README, session log, and swap when warranted. Update swap last.

## Completed work

### Repository continuity and Flood reconciliation

The branch contains the repo-backed continuity system:
- `agents.md`
- `.ai/swap.md`
- `research/continuity/DOCUMENTATION-GOVERNANCE.md`
- `research/continuity/MASTER-RESEARCH-REGISTER.md`
- `research/README.md`
- `research/session-log.md`

Flood claim reconciliation 001 reviewed 58 Main-namespace phrase-hit pages. It records 58/58 source hash matches, 35 canonical direct-link edges across 29 pages, and cautions against treating phrase hits or links as complete semantic dependency coverage. See `research/continuity/flood-claim-reconciliation-001.md` and its CSV.

### Narrative audit validation tranche 001

Starting audited HEAD: `fdec89ff1221a36fa360630b0d7607b7c7d2f95d`.

Twenty-eight Bronze pages were reviewed at varying depth: 19 full semantic reads and 9 partial reads. All 28 raw SHA-256 values matched the Bronze manifest.

The original 14 unledgered pages with at least three standalone 2024–2040 year mentions were:
97 Little Cold War; 1317 De-Extinction; 1651 Korean reunification; 1702 List of World War III weapons; 1445 President of Mexico; 272 Earth; 1796 United States presidential election, 2040; 1936 Flags of the United States; 2356 List of states and territories of the United States; 1266 Reed Chen; 2136 Tanning the Donkey; 1262 Maya Garcia; 1431 Arya Kanzaki; 1739 Terran diaspora.

Artifacts:
- `research/narrative-audit/MASTER-NARRATIVE-AUDIT.md`
- `research/narrative-audit/validation-tranche-001.md`
- `research/narrative-audit/POST-2041-LINK-DISCOVERY-001.md`
- `research/narrative-audit/page-review-001.csv`

### Narrative audit validation tranche 002

Starting branch HEAD: `cbde12c17c507a74f3220858481a0930740e4f59`.

The full exact-year ledger gap is now **43 pages**, not 14. The earlier 14-page count was the subset with three or more mentions. The reproducible scan uses standalone 2024–2040 tokens and excludes decade labels such as 2030s.

- 357 non-redirect Main pages.
- 116 pages contain at least one standalone 2024–2040 year.
- 73 of those are represented in `claim-ledger-001.csv`.
- 43 are missing: 17 with one mention, 12 with two, and 14 with three or more.
- All 43 raw source hashes match the Bronze manifest.
- The 29 additional pages received targeted date-context review, not full semantic reads.

Artifacts:
- `research/narrative-audit/validation-tranche-002.md`
- `research/narrative-audit/claim-ledger-gap-002.csv`

Nine priority pages reopened for source context: 1366 Caribbean annexation, 318 Mars, 1431 Arya Kanzaki, 1436 Tactile-neural interface, 1998 Central Eurasian Union, 2136 Tanning the Donkey, 1715 Korea, 3484 New Korean Wave, and 2774 Project Rebirth.

## Current verified metrics

- Bronze page manifest: 3,579 records; Main namespace: 507; non-redirect Main pages: 357.
- Standalone 2024–2040 discovery: 116 pages; 73 represented in claim ledger 001; 43 missing.
- Gap-page source hashes: 43/43 matched the pinned Bronze manifest.
- 262 non-redirect Main pages contain discrete 2041+ year mentions; this is discovery only, not semantic classification.
- 82 pages mention both 2024–2040 and 2041+; 34 mention only 2024–2040; 180 mention only 2041+; 61 mention neither.
- Post-2041 page-level survival classifications: 0 of 262.
- Regions complete: 0 of 11.

Pinned archive SHA-256:
`d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`

## Chronology proposal register 001

- `research/continuity/chronology-proposal-register-001.md` contains 16 conversation-origin proposals. Every entry is **PROPOSAL, conversation-origin, not canon, not approved**.
- The register preserves reported relationships to pages 88, 94, 107, 1106, 1438, and 214. It does not edit the realism-first timeline or resolve conflicts.
- Source relationships were supplied in the maintainer's 2026-11-27 instruction; independent Bronze re-fetch/hash verification remains outstanding.
- Master register, research README, and append-only session log have been synchronized. The next action is to send the exact commit packet for independent review; do not begin tranche 003 until that review is answered.

## Important validated findings and corrections

1. Page 1445's 2024 Mexican presidential succession conflicts with observed history and Claudia Sheinbaum's inauguration.
2. Page 1317's claim of a successful 2024 gastric-brooding frog de-extinction is false. Correction: the 2025 ABC report says Project Lazarus was put back on ice after repeated unsuccessful embryo attempts; this does not prove permanent abandonment. The 2028 thylacine claim is an unsupported future forecast, not already disproven.
3. Page 97's claim that Western European states withdrew from NATO is false. NATO still has 32 members. The real 2025–2026 alliance stress is US-origin: Iran-war disagreements, force-posture reductions, and the Greenland dispute.
4. The US presidential chronology is a direct contradiction: page 214 lists Price through Jan 2045 and Garcia from Jan 2045; page 1796 says Garcia won in 2040; page 1797 treats Garcia as incumbent before the 2044 election. Page 1136 also conflicts internally on Liberal Party founding (2029 prose vs 2052 infobox). Preserve all values.
5. Pages 318, 1739, 1431, 1405, 1426, 2127, 1685, and 3662 contain Mars/outer-planet/space-elevator claims incompatible with the realism-first technology envelope before 2041.
6. Page 1366 ties Caribbean annexation to retired Flood premises; Guyana public sources reviewed support defense/security cooperation but do not substantiate a launch complex or free-association mechanism. Puerto Rico dates conflict across pages 272, 1936, and 2356.
7. Page 961's Mueller wording was paraphrased too strongly in the first audit; legal-source re-fetch remains outstanding. Supreme Court immunity characterization remains overbroad.
8. The Navy CPS GAO citation is not HACM evidence. GAO-26-108457 is the relevant HACM assessment; first flight-test release occurred Oct 2026, while FY2027 fielding remains a high-risk goal.
9. Page 1436 conflates non-invasive BCI, implantable BCI, cortical sensory feedback, and external haptics. A basic BCI/haptic combination is not equivalent to high-fidelity direct neural sensory input.
10. Pages 1715 and 3484 depend on the 2029–2031 Korean reunification chain unless a separate trigger is supplied.
11. Page 1729's 2034 Treaty of Odessa depends on former Russian Federation territory and conflicts with the rule that Russia remains intact through 2040. Page 1438's 2046–2055 Eurasian Coalition may survive only if re-seeded after 2041.
12. Page 1998 Central Eurasian Union does not state a direct dependency on 2029 Russian dissolution. Do not infer succession from its name.
13. Preserve the 2029 Russian sequence and predecessor-name conflict; it may be sequential but is not reconciled.
14. The 262-page post-2041 universe remains unclassified; link counts are discovery leads, not causal determinations.

## 2025–2026 observed-baseline additions

- NATO roster remains 32.
- The Iran war produced allied disagreements over participation, access, basing, and overflight; Trump publicly considered US withdrawal from NATO in April 2026.
- US rotational force posture in Europe was reduced; this is not evidence of Western European NATO exits.
- The Greenland dispute culminated in a November 2026 security agreement that expands US military access while preserving Danish sovereignty and Greenlandic self-determination.
- NASA and National Academies sources describe Mars as a difficult future program, not a completed 2020s settlement; no crewed Saturn mission is planned.
- CNT fiber advances do not demonstrate the defect-controlled, high-integrity, tether-scale materials required for a space elevator.
- Clinical BCI, non-invasive BCI, and external haptic technologies remain distinct.
- Public Guyana records reviewed describe defense/security cooperation, not the page's launch-complex/free-association pathway.

Detailed sources and qualifications are in `research/narrative-audit/validation-tranche-002.md`.

## Immediate next work

1. Complete full semantic reads for the 29 additional gap pages; extract claims and dependencies into a reviewed ledger without automatically promoting every year token.
2. Sweep all claims dated 2019–2026 against observed history, starting with the highest-impact pages and exact source dates.
3. Reconcile the US presidential/party chronology across pages 214, 1262, 1266, 1136, 1796, 1797, 2135, 2136, and 2451.
4. Rebuild the Russia/Odessa/Eurasian succession chain without pre-2041 Russian dissolution.
5. Continue the 262-page post-2041 survival map in bounded batches, starting with Flood, Mars, Great Famine/Korea, Russia/Eurasia, and US territorial expansion.
6. Add a fuller observed 2025–2026 baseline to the realism-first timeline after a dedicated source review.

## Safety and closeout

No canon, Bronze/Silver source data, manifests, or RAG implementation changed in validation tranche 002. No tests, builds, or RAG CLI runs were executed. No PR, merge, or branch promotion was performed.

At the end of each tranche, verify branch and HEAD, update the master register and README, append the session log, refresh this swap file last, and report actual final verification results.
