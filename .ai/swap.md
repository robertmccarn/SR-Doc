# SR-Doc — AI session swap memory

> **Role:** Compact, repo-backed handoff snapshot for AI work. This file is mutable working memory, not canon, source evidence, or a chronological log.
> **Last verified against GitHub: 2026-11-21 (after successful schema-contract CI run and benchmark documentation)
> **Branch:** `audit/continuity-research`
> **Branch HEAD before this swap refresh: ebd6724c361cbcde2ba3005ff59e420cf883cb79
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
- Four contrast regression checks were recorded as passing against the uploaded version-002 SQLite index; see `research/rag/contrast-smoke-tests-001.json`. This is a smoke/regression check, not a benchmark.
- Source-aware infobox extraction is now implemented in `research/rag/extract_infobox_claims.py`, with schema `research/rag/infobox-claim.schema.json` and conservative event-scoped comparison in `research/rag/evaluate_infobox_claims.py`. The evaluator requires same page subject, an explicit reviewed `event_scope_id`, template family, and exact normalized parameter name. Repeated parameters without event-scope annotation remain unresolved, not conflicts. Detailed evidence: `research/rag/infobox-claims-pass-001.md`.
- Regression test source is `research/rag/test_infobox_claims.py`, and `research/rag/infobox-claims-pass-001.md`. The five committed parser/comparison regression tests passed in GitHub Actions (run 44925739208, Python 3.11.18). The committed extractor, schema, and evaluator sources were subsequently verified against their Git blob SHAs and executed against the pinned ZIP: 507 main-namespace pages, 143 infobox invocations, 4,381 claims, 4,381 unique IDs, zero source errors; all claims passed JSON Schema and exact offset/provenance checks; a second run was byte-identical. Evaluator output: zero scoped conflict candidates and two unresolved groups (page 636 `office`; page 1343 `order`). Machine report: `research/rag/infobox-claim-validation-001.json`. The 20-case evaluation baseline has passed independent source-locator review: all ten registered source identities, 51 cited locator/content ranges, and seven title/map-boundary checks passed; Q09/Q16/Q17 locator corrections are recorded in `research/rag/evaluation-locator-validation-001.json`. Maintainer approval received 2026-11-21; retrieval pass 001 records page recall, locator coverage, entity/redirect resolution, and schema correction. All 20 evidence packets now validate against the updated schema. Q18's map reference is present in raw Wikitext and page-manifest `images` metadata, but its binary is absent from the asset manifest and ZIP; see the correction in `research/rag/evaluation-set-001.md`.

Key files:
- `research/rag/build_index.py`
- `research/rag/build_alias_index.py`
- `research/rag/search.py`
- `research/rag/test_search.py`
- `research/rag/evidence-packet.schema.json`
- `research/rag/evaluation-set-001.md`
- `research/rag/evaluation-locator-validation-001.json`
- `research/rag/retrieval-benchmark-pass-001.json`
- `research/rag/README.md`
- `research/continuity/RESEARCH-ASSISTANT-PROTOCOL.md`

Generated local index ZIP is `SR-Doc-RAG-Index-002.zip`; it is a build artifact, not a committed database. Rebuild from the exact validated archive and run the alias-index builder after the base index builder.

## 3. Current known test case / continuity issue

- Page 1413, **Second Chinese Civil War**, contains infobox dates 2027–2048 and a combatant period marked 2105–2111.
- Page 1408, **Third Chinese Civil War**, covers phases beginning in 2105 and extending through 2126.
- The contrast retriever surfaces the page-1413 multi-range passage and page 1408 for comparison.
- This is a confirmed source-level inconsistency candidate, not a resolved chronology. Field labels, event scope, and any creator/community explanation still need review.
- The date regex is heuristic; it does not parse infobox field semantics. Lexical OR matching can be noisy. Retrieval pass 001 found all expected pages by top five unique candidates, but first-stage locator coverage was 47/55; full-page expansion raised it to 55/55. Contrast candidate precision remains noisy and no semantic contradiction precision is claimed.

## 4. Immediate next steps

1. Inspect the current branch and read this swap plus `agents.md`, `DOCUMENTATION-GOVERNANCE.md`, master register, RAG README, and recent session log.
2. Generate answer outputs from the retrieved evidence packets and score answer-element coverage, claim support, citation precision, contradiction disclosure, and abstention separately. Retrieval pass 001 is exploratory because local index/search scripts were source-equivalent reconstructions, not byte-identical Git blobs.
3. Improve first-stage passage selection: Q09/Q10/Q15 missed page-1408 infobox/phase locators, and Q16 missed the FRoC history stub and Association establishment field until full-page expansion. Q09's page-1413 date-value locator was normalized to chars 114–125 in the evaluation set; see correction 003.
4. Keep the two reviewed repeated-parameter groups (page 636 `office`; page 1343 `order`) unresolved. No event-scope annotation is supported by the captured Wikitext.
5. Preserve the two unresolved event-scope groups; do not infer event_scope_id from layout alone.
6. Continue the broader parser-coverage review and preserve the Chinese political-history Talk/Thread context and succession claim matrix.

## 5. Open questions / blockers

- What is the most reliable extraction boundary for infobox templates without a full MediaWiki renderer? Raw template parameter parsing may need nested-brace-aware parsing.
- Which of the observed infobox template families should be supported first? Start with the already audited high-value families and document exclusions.
- How should claim identity be represented so repeated dates for different phases are not mistaken for conflicts?
- The 20-question evaluation set is maintainer-approved; retrieval pass 001 is recorded. Answer-generation/citation scoring remains pending.
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
- Last verified HEAD before this swap refresh is recorded at the top of this file.
- Latest milestone: five committed parser/comparison regression tests passed in GitHub Actions; continuity validation, compileall, and existing pytest suite also passed. The committed extractor/evaluator ran against the pinned archive; all 4,381 claims passed schema/offset/provenance validation, with deterministic repeat output. See `research/rag/infobox-claim-validation-001.json`.
- New files: `research/rag/extract_infobox_claims.py`, `research/rag/evaluate_infobox_claims.py`, `research/rag/infobox-claim.schema.json`, `research/rag/test_infobox_claims.py`, `research/rag/infobox-claim-validation-001.json`.
- Updated permanent docs: RAG README, infobox pass-001 note, evaluation set and locator report, master register, research README, session log, and `agents.md`.
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
