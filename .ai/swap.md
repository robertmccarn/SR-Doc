# SR-Doc — Agent Swap / Current Working State

**Repository:** robertmccarn/SR-Doc  
**Working branch:** experiment/corrected-realism  
**Branch HEAD before this swap refresh:** 829823096e824b8c8dfe10a9268e265ea1a9175c  
**Last verified:** 2026-11-25  
**Current workstream:** Independent narrative audit, validation tranche 001 complete; post-2041 survival map in progress.

## Start here

Read in this order:
1. agents.md
2. this file
3. research/continuity/DOCUMENTATION-GOVERNANCE.md
4. research/continuity/MASTER-RESEARCH-REGISTER.md
5. research/README.md
6. research/narrative-audit/MASTER-NARRATIVE-AUDIT.md
7. research/narrative-audit/validation-tranche-001.md
8. research/narrative-audit/POST-2041-LINK-DISCOVERY-001.md
9. research/continuity/realism-first-timeline-2024-2040.md
10. research/session-log.md

The repository is the source of truth. Do not rely on chat history when a repository record exists.

## Governing editorial constraint

There must be no departure from authentic real-world scientific, technological, demographic, economic, institutional, military, or geopolitical plausibility before 2041. Deliberate divergence may begin in 2041 or later, but later developments must remain causally and physically coherent.

Climate is one factor among many, not a universal master cause. Evaluate institutions, demographics, supply chains, technology, energy and minerals, finance, military competition, trade, culture and information, public health, geography, and regional agency.

Distinguish observed history, forecast, scenario assumption, inference, hypothesis, and unresolved claim. Preserve contradictions; do not silently reconcile them. A wiki link is not proof of causality.

## Operational boundaries

- Work only on experiment/corrected-realism unless the maintainer explicitly changes the instruction.
- This is a non-canon editorial branch.
- Do not modify accepted canon, Bronze or Silver source data, manifests, or RAG implementation without explicit authorization.
- Research and audit documentation may be updated in accordance with DOCUMENTATION-GOVERNANCE.md.
- Do not create or merge PRs, merge branches, or promote the branch without explicit approval.
- Never claim tests, builds, RAG CLI runs, or validation that were not actually executed.
- Use Bronze Wikitext as primary evidence; use Silver for navigation and parsed metadata.
- When the user requests corpus-page tranches, use the established 300-page batch size. The current narrative audit is a bounded thematic workflow, not a substitute for the corpus inventory.
- Update the master register, README, session log, and swap file when warranted. Update the swap file last.

## Completed work

### Repository continuity and Flood reconciliation

The branch contains the repo-backed continuity system:
- agents.md
- .ai/swap.md
- research/continuity/DOCUMENTATION-GOVERNANCE.md
- research/continuity/MASTER-RESEARCH-REGISTER.md
- research/README.md
- research/session-log.md

Flood claim reconciliation 001 reviewed 58 Main-namespace phrase-hit pages. The note records 58/58 source hash matches, 35 canonical direct-link edges across 29 pages, and explicit cautions against treating phrase hits or links as complete semantic dependency coverage. See research/continuity/flood-claim-reconciliation-001.md and its CSV.

### Narrative audit validation tranche 001

Audited starting HEAD: fdec89ff1221a36fa360630b0d7607b7c7d2f95d.

Twenty-eight Bronze pages were reviewed at varying depth: 19 full reads and 9 partial reads. All 28 raw SHA-256 values matched the Bronze manifest.

Fourteen exact-year pages with at least three discrete 2024–2040 year mentions were confirmed absent from claim-ledger-001.csv:
97 Little Cold War; 1317 De-Extinction; 1651 Korean reunification; 1702 List of World War III weapons; 1445 President of Mexico; 272 Earth; 1796 United States presidential election, 2040; 1936 Flags of the United States; 2356 List of states and territories of the United States; 1266 Reed Chen; 2136 Tanning the Donkey; 1262 Maya Garcia; 1431 Arya Kanzaki; 1739 Terran diaspora.

Additional recursive pages reviewed: 3484 New Korean Wave, 1234 Hypersonic Weapons, 2774 Project Rebirth, 1715 Korea, 1436 Tactile-neural interface, 1998 Central Eurasian Union, 88 Timeline of major events, 1683 Russia, 1729 Treaty of Odessa, 1438 Eurasian Coalition, 1366 Caribbean annexation, 1479 Orbital Command Stations, 318 Mars, and 961 Trump-Russia scandal.

Audit artifacts:
- research/narrative-audit/MASTER-NARRATIVE-AUDIT.md
- research/narrative-audit/validation-tranche-001.md
- research/narrative-audit/POST-2041-LINK-DISCOVERY-001.md
- research/narrative-audit/page-review-001.csv

## Current verified metrics

- 507 Main-namespace pages; 357 non-redirect Main pages.
- 116 non-redirect pages contain discrete 2024–2040 year mentions (117 including redirects).
- 262 non-redirect pages contain discrete 2041+ year mentions.
- 82 pages mention both periods; 34 mention only 2024–2040; 180 mention only 2041+; 61 mention neither.
- 14 exact-year pages are confirmed absent from the existing claim ledger.
- The 262-page count is discovery only. It is not a semantic audit completion count.
- A link-level scan found 27 future-dated pages linking to Mars, 20 to The Flood, 10 to The Refreeze, 7 to Earth Working Group, 8 each to Great Reset and White Tide, and other clusters. These counts are not causal classifications.

## Important validated findings and corrections

1. Archive SHA-256 of the uploaded SR-Doc-Audit.zip is:
   d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8
   The 63-character transcription was incorrect. Five current research documents were corrected. Historical session-log entries remain unchanged under the append-only rule; the correction is appended.
2. Page 1445's 2024 Mexican presidential succession conflicts with the observed 2024 election and Claudia Sheinbaum's 1 October 2024 inauguration.
3. Page 1317's claim of a successful 2024 gastric-brooding frog de-extinction is false; the Lazarus Project did not produce a living frog.
4. Page 97's assertion that Western European states withdrew from NATO in the mid-2020s is unsupported; the official NATO roster still has 32 members.
5. Page 961 misstates the Mueller report as establishing a Trump-campaign/Russia conspiracy and overstates the 2024 Supreme Court immunity ruling.
6. Pages 318, 1739, and 1431 contain a pre-2041 Mars settlement/terraforming/Titan mission cluster that conflicts with the realism-first rule and contains a 2023/2026 chronology conflict.
7. Page 1366 ties Caribbean annexation to retired Flood and displacement premises; pages 272, 2356, and 1936 repeat the US expansion sequence and disagree on Puerto Rico's date.
8. Pages 2136, 1262, 1266, and 1796 do not share a reconciled US party-system chronology.
9. Pages 1702 and 1234 contain unsupported pre-2041 hypersonic/orbital-strike claims; page 1234 also has an apparent 2028/2113 chronology inversion.
10. Page 1479's 2033–2040 Orbital Command Stations and page 1436's 2028–2034 tactile-neural interface claims need technology audits.
11. Page 1651's Korean reunification chain depends on the Great Famine, but a December 2026 aid cut may be anticipatory rather than a strict cause-after-effect error.
12. Claude's claim that the Russia 2029 accounts are three incompatible narratives was too strong. A staged sequence may reconcile May 2029 Union State collapse/successor formation, August 2029 formal Russian Federation collapse, 2029–2038 nuclear-security operations, and the 2034 Treaty of Odessa. The prose needs clarification; the 2138/2139 end-date conflict remains.

## Next work

1. Continue the 262-page post-2041 survival map in bounded semantic batches. Classify pages as direct dependency, latent dependency, independent, or unresolved, with a counterfactual for each. Start with Flood, Mars, Great Famine/Korea, Russia/Eurasia, and US territorial expansion.
2. Continue the observed-baseline sweep across 2022–2026 claims, prioritizing pages 97, 961, 1317, 1445, 318, 1234, and 1366.
3. Complete the Russia/Eurasia regional chain: pages 97, 1683, 1729, 1438, 1998, 961, and related successor-state, Turkish, Polish, and Japanese pages.
4. Reconcile the US party-system and election chronology.
5. Return to the Great Famine / Market Crash / Revolutions / Great Reset cluster.

## Safety and closeout

No canon, Bronze/Silver data, manifests, or RAG implementation changes were made in validation tranche 001. No tests, builds, or RAG CLI runs were executed. No PR, merge, or branch promotion was performed.

At the end of each tranche, verify the current branch and HEAD, update the master register and README, append the session log, refresh this swap file last, and report the actual final HEAD and verification results.
