# SR-Doc — agent operating guide

This file is the concise, current handoff for AI agents working on the research branch. It replaces the former append-only 851-line file; the complete former file is preserved verbatim at `research/continuity/agents-md-history-2026-11-20.md`.

## Start here

0. Verify the active branch and HEAD, then read `.ai/swap.md` for the current cross-window handoff. Treat it as orientation, not authority; verify its claims against Git and source files.
1. For lore-answer behavior, read `research/continuity/RESEARCH-ASSISTANT-PROTOCOL.md`.
2. For RAG implementation status and next tasks, read `research/rag/README.md`.

3. Read `research/continuity/DOCUMENTATION-GOVERNANCE.md` and follow it for every documentation change.
4. Read `research/continuity/MASTER-RESEARCH-REGISTER.md` for canonical status, evidence hierarchy, inventories, reconciled counts, findings, and next steps.
5. Read `research/README.md` for navigation and `research/session-log.md` for chronology.
6. Read the relevant detailed tranche/continuity notes before extending an investigation.
7. Verify current branch and latest file versions before writing. Do not rely on commit SHAs from old conversations.

## Mission

Conduct a careful, source-grounded audit of SR-Doc's captured wiki corpus and repository. Identify data integrity issues, missing dependencies, internal continuity conflicts, and structural risks. Preserve information and provenance. Do not rewrite canon as part of an audit.

## Non-negotiable rules

- Work on `audit/continuity-research` unless the user explicitly directs otherwise.
- Never merge, open a PR, promote a branch, or edit canon without explicit user approval.
- Treat Bronze captures and manifests as immutable evidence. Never overwrite, normalize, or repair them.
- Distinguish observed facts, computed results, inferences, hypotheses, and unresolved questions.
- Preserve contradictory dates, names, numbers, and claims. Describe conflicts; do not silently resolve them.
- Treat Talk, Thread, User, and other community namespaces as editorial/contextual evidence, not automatically canon.
- A raw filename mention is not proof of rendered use. An extracted image reference is not a complete rendered dependency graph. No discovered reference is not proof of an orphan.
- Keep page reads/hash verification, media checksum checks, visual triage, semantic review, and continuity validation as separate statuses.
- Follow `research/continuity/DOCUMENTATION-GOVERNANCE.md`: do not append findings to this file; preserve detailed notes; synchronize master register, README, and session log according to the change protocol.
- Never claim a file was read, verified, visually reviewed, or committed unless the corresponding operation actually succeeded.

## Canonical status snapshot

As of 2026-11-20:
- 3,579/3,579 page records directly read and SHA-256 verified.
- Main namespace 507/507.
- 900 media manifest records; 899 physical files. Entry 815 / page ID 3525 / `File:K8ch1z55ucnz.png` is missing.
- All 899 available media files decoded/parsed and visually triaged at contact-sheet thumbnail scale; 728 exact SHA-1/size matches, 171 mismatches, zero decode failures.
- Cross-reference totals: 792 exact extracted asset references, 11 literal-only mentions, 97 with no discovered mention, 1,696 exact page-reference edges.
- File namespace has 906 records; all 900 media page IDs resolve. Six File pages are outside the media manifest, including three redirects.
- 141 extracted image titles have no exact media-manifest counterpart; most are template/module dependencies.
- Initial Chinese political-history audit has identified unresolved chronology and infobox inconsistencies.

These counts and definitions are maintained in the master register. If new verification changes them, update the register and README and append a correction to the session log.

## Working procedure

1. Define a bounded scope and enumerate exact source pages/manifest ranges before analysis.
2. Use the original Bronze Wikitext/manifests as source of truth. Recompute hashes when the task is about source integrity.
3. Keep raw evidence separate from interpretation. Quote only the minimum useful source excerpt and record page title/ID and relevant fields.
4. For dependency work, distinguish:
   - explicit raw `[[File:...]]`/`[[Image:...]]` links;
   - extracted page-manifest `images` metadata;
   - template/module parameter values and aliases;
   - File-page redirects;
   - actual rendered output (only if a parser/rendering run verifies it).
5. For continuity work, build a dated claim matrix with source, exact claim, confidence, and conflicting evidence. A missing article or map is an unresolved evidence gap, not permission to invent content.
6. Record methods, counts, exclusions, caveats, and every unresolved issue in a focused note.
7. Update the master register and README only for material status changes; append a dated session-log entry. Keep this file operational, not append-only.
8. Preserve all earlier detailed notes. Consolidate by indexing and cross-linking, not deleting or compressing away evidence.

## Repository notes and structure

- `.ai/swap.md` — compact cross-window session handoff; verify against actual Git state.
- `research/continuity/DOCUMENTATION-GOVERNANCE.md` — normative documentation and swap-memory maintenance protocol; read before editing research documentation.
- `research/continuity/MASTER-RESEARCH-REGISTER.md` — canonical master register; read first for current factual status.
- `research/continuity/agents-md-history-2026-11-20.md` — verbatim archival copy of the old long handoff.
- `research/README.md` — concise status/navigation.
- `research/session-log.md` — append-only chronology; older status claims may be superseded.
- `research/page-ledger.csv`, `research/media-ledger.csv` — structured audit ledgers.
- `research/page-notes/` — page-manifest tranche evidence.
- `research/media-notes/` — media binary and cross-reference tranche evidence.
- `research/continuity/` — thematic synthesis and continuity investigations.

## Current next work

Follow the ordered recommendations in the master register. The active implementation priority is the SR-Doc RAG workstream. Section-aware chunks, SQLite FTS5 lexical retrieval, exact title/redirect resolution, date-bearing contrast retrieval, source-aware infobox parameter extraction and a claim schema are implemented. The committed extractor has now run against the pinned archive: 4,381/4,381 claims passed JSON Schema and exact offset/provenance validation, with byte-identical repeat output; see `research/rag/infobox-claim-validation-001.json`. The evaluator leaves page 636 `office` and page 1343 `order` unresolved because neither has a reviewed event_scope_id. The maintainer approved the 20-question evaluation baseline on 2026-11-21. Retrieval pass 001 is recorded in `research/rag/retrieval-benchmark-pass-001.json`: 19/19 expected-page sets found within top five unique candidates; first-stage locator coverage 47/55, rising to 55/55 after full-page expansion; exact-title and redirect resolution passed. The pass also found and fixed an evidence-packet schema mismatch (`exact_title`/`redirect_target` statuses). Next: generate answers from retrieved packets and score answer-element coverage, citation precision, claim support, contradiction disclosure, and Q18/Q19 abstention. The local index/search execution was a source-equivalent reconstruction, not byte-identical to the committed scripts; retain that limitation in future reporting. Measure retrieval and claim-comparison quality before considering embeddings. Preserve the Chinese political-history Talk/Thread context and succession claim matrix as outstanding work; do not silently discard them.

## Reporting standard

For each work unit, report:
- exact scope and source range;
- method and verification performed;
- counts/results;
- confirmed findings versus interpretations;
- unresolved questions and limitations;
- files created/updated and resulting commit;
- branch and explicit statement that no merge/PR/canon edit occurred, where applicable.
