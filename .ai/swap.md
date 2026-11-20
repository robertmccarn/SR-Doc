# SR-Doc — AI session swap memory

> **Role:** Compact, repo-backed handoff snapshot for AI work. This file is mutable working memory, not canon, source evidence, or a chronological log.
 > **Last verified against GitHub:** 2026-11-20 (immediately before this swap refresh commit)
> **Branch:** `audit/continuity-research`
> **Branch HEAD at last verification:** `ef0426be4e495d1579301b1ebfb38b0c622ef982`
> **Maintainer:** User-directed SR-Doc workflow; agents may update this file under `research/continuity/DOCUMENTATION-GOVERNANCE.md`.

## 1. Mission and standing constraints

Continue the source-grounded SR-Doc corpus audit and research-assistant/RAG implementation. The repository and captured source data—not chat history, model memory, or this swap file—are authoritative.

- Work on `audit/continuity-research` unless explicitly directed otherwise.
- No merge, PR, branch promotion, canon edit, or Bronze/Silver source modification without explicit user approval.
- Bronze captures/manifests are immutable evidence.
- Preserve contradictions; never silently adjudicate or normalize claims.
- Distinguish observed, computed, inferred, hypothesis, and unresolved.
- Main namespace is the default lore evidence. Talk/Thread/User/community namespaces are contextual/editorial and require explicit opt-in.
- Do not claim tests or builds ran unless execution actually succeeded. Record test scope and limitations.
- Never place credentials, tokens, private keys, personal secrets, or other sensitive data here.

## 2. Active workstream

**RAG: source-aware claim extraction and contradiction evaluation.**

Implemented baseline:
- Read-only archive validator; pinned archive SHA-256: `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`.
- Section-aware chunk builder: 3,579 page metadata rows; 7,598 chunks; 3,092 pages with text; 487 records without non-whitespace chunks.
- SQLite FTS5 lexical retrieval; default namespace 0; explicit `--include-context`.
- Exact page-ID lookup and exact title/direct redirect lookup via `--title`; aliases retain redirect provenance and do not merge identities.
- Date-bearing contrast mode via `--contrast`; returns diversified lexical candidates and heuristic `date_signals`, flags multiple date ranges for human review.
- Four regression checks recorded as passing against the uploaded version-002 SQLite index; see `research/rag/contrast-smoke-tests-001.json`. This is a smoke/regression check, not a benchmark.

Key files:
- `research/rag/build_index.py`
- `research/rag/build_alias_index.py`
- `research/rag/search.py`
- `research/rag/test_search.py`
- `research/rag/evidence-packet.schema.json`
- `research/rag/evaluation-set-001.md`
- `research/rag/README.md`
- `research/continuity/RESEARCH-ASSISTANT-PROTOCOL.md`

Generated local index ZIP is `SR-Doc-RAG-Index-002.zip`; it is a build artifact, not a committed database. Rebuild from the exact validated archive and run the alias-index builder after the base index builder.

## 3. Current known test case / continuity issue

- Page 1413, **Second Chinese Civil War**, contains infobox dates 2027–2048 and a combatant period marked 2105–2111.
- Page 1408, **Third Chinese Civil War**, covers phases beginning in 2105 and extending through 2126.
- The contrast retriever surfaces the page-1413 multi-range passage and page 1408 for comparison.
- This is a confirmed source-level inconsistency candidate, not a resolved chronology. Field labels, event scope, and any creator/community explanation still need review.
- The date regex is heuristic; it does not parse infobox field semantics. Lexical OR matching can be noisy. No recall/precision benchmark exists.

## 4. Immediate next steps

1. Inspect the current branch and read this swap plus `agents.md`, `DOCUMENTATION-GOVERNANCE.md`, master register, RAG README, and recent session log.
2. Build **source-aware infobox claim extraction**: preserve exact parameter names/values, page ID/title, revision, source hash, section/character locator, and raw source text. Do not infer semantics from date patterns alone.
3. Add claim records to a separate derived artifact/table; never alter Bronze/Silver inputs.
4. Compare claims only where subject/event/field semantics plausibly align. Emit candidate conflicts with supporting evidence IDs and explicit review status; never pick a canonical answer.
5. Complete reviewed expected evidence/page IDs for the 20-question evaluation seed, then measure evidence recall and contradiction candidate recall/precision.
6. Update this swap after the implementation milestone, plus master register/README/session log under documentation governance.

## 5. Open questions / blockers

- What is the most reliable extraction boundary for infobox templates without a full MediaWiki renderer? Raw template parameter parsing may need nested-brace-aware parsing.
- Which of the observed infobox template families should be supported first? Start with the already audited high-value families and document exclusions.
- How should claim identity be represented so repeated dates for different phases are not mistaken for conflicts?
- The 20-question evaluation set still needs reviewed source passage IDs and expected answer elements.
- Redirect-chain resolution, namespace aliases, and broader entity aliases remain out of scope for the current resolver pass.
- The contrast heuristic is not a semantic contradiction detector.

## 6. Durable decisions

- Repository is the knowledge authority; this file is a compact pointer/status snapshot only.
- Keep working memory separate from permanent research evidence and from the append-only session log.
- Bronze/Silver are immutable; all extraction and indexing is derived and reproducible.
- Keep lexical retrieval as the baseline. Defer embeddings until measured retrieval gaps justify them.
- Redirect mappings preserve original page identity and provenance; no fuzzy entity merge.
- Retrieval may surface conflicting candidates; only human/source review can classify or resolve them.
- Default lore retrieval excludes community namespaces.
- Do not merge, open PRs, promote branches, or edit canon without explicit approval.

## 7. Recent repository state

- Repository: `robertmccarn/SR-Doc`
- Branch: `audit/continuity-research`
- Last verified HEAD: `7d75aa432c11ba32f9f474d8df439a5df54f2ba1`
- Last milestone: date-bearing contrast retrieval pass 001.
- Recent changed files include `research/rag/search.py`, `research/rag/test_search.py`, `research/rag/contrast-smoke-tests-001.json`, RAG README, master register, research README, session log, and `agents.md`.
- No PR, merge, branch promotion, or canon/source-data edit was performed for that milestone.

## 8. Memory system established

- Canonical swap path: `.ai/swap.md`.
- Memory procedures: section 12 of `research/continuity/DOCUMENTATION-GOVERNANCE.md`.
- Session startup pointer: `agents.md`.
- Research navigation: `research/README.md`; canonical status pointer: `research/continuity/MASTER-RESEARCH-REGISTER.md`.
- The setup itself is recorded in `research/session-log.md`. No secrets are stored here.

## 9. Session closeout checklist

Before ending a work session:
- Verify branch and HEAD from GitHub.
- Update current state, decisions, blockers, and immediate next steps here.
- Remove completed items from the active list; retain durable decisions.
- Promote durable technical decisions to permanent docs/ADRs and implementation to code/tests.
- Update master register/README/session log when required by governance.
- Re-fetch changed files and verify committed content.
- Record the resulting HEAD SHA and whether any tests actually ran.
