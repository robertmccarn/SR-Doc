# SR-Doc — AI session swap memory

> **Role:** Compact, repo-backed handoff snapshot for AI work. This file is mutable working memory, not canon, source evidence, or a chronological log.
> **Last verified against GitHub:** 2026-11-25 (after corrected-realism branch audit pass 001)
> **Branch:** `experiment/corrected-realism`
> **Branch HEAD before this swap refresh:** `15f49da1c2377cf38f83f3139bd7af04cbf18230`
> **Maintainer:** User-directed SR-Doc workflow; agents may update this file under `research/continuity/DOCUMENTATION-GOVERNANCE.md`.

## 1. Mission and standing constraints

Continue the source-grounded SR-Doc corpus audit and research-assistant/RAG implementation. The `experiment/corrected-realism` branch is a user-authorized, non-canon editorial offshoot; its proposal must not be mistaken for accepted lore. The repository and captured source data—not chat history, model memory, or this swap file—are authoritative.

- Current user-designated working branch is `experiment/corrected-realism`; work here unless explicitly directed otherwise. Treat `audit/continuity-research` at `d93184ad0f78af7b96d264e2bd00d95a8bd61736` as the read-only base for this offshoot.
- No merge, PR, branch promotion, canon edit, or Bronze/Silver source modification without explicit user approval.
- Bronze captures/manifests are immutable evidence.
- Preserve contradictions; never silently adjudicate or normalize claims.
- Distinguish observed, computed, inferred, hypothesis, and unresolved.
- Main namespace is the default lore evidence. Talk/Thread/User/community namespaces are contextual/editorial and require explicit opt-in.
- Do not claim tests or builds ran unless execution actually succeeded. Record test scope and limitations.
- Never place credentials, tokens, private keys, personal secrets, or other sensitive data here.

## 2. Active workstream

**Current branch: non-canon corrected-realism editorial audit.**
- Proposal: `research/continuity/corrected-realism-proposal-001.md`.
- Audit report: `research/continuity/corrected-realism-audit-001.md`.
- Audit pass 001 verified 13 relevant Bronze page hashes against the pinned archive manifest and reviewed all five paths changed relative to the audit base, plus `agents.md` and governance. No canon/source-data edits were made.
- Material decisions remain open: Flood mortality/displacement and sea-level curve; Great Famine 2032/2033 endpoint and three episodes; Second Chinese Civil War 2027–2048; White Tide's WIP scale and 2033/2035 endpoints; 2023 Mars landing and 2029–2033 terraforming; Turkey/Russia timeline-only geopolitical claims.
- Do not edit canon or source pages as part of this editorial branch without a separate explicit authorization.

**Inherited baseline: RAG source-aware claim extraction and contradiction evaluation.**

Implemented baseline:
- Read-only archive validator; pinned archive SHA-256: `d1af0775d69def6ef442b66393e3ad84db66cb6b9ecf9138170573fdfe0a02c8`.
- Section-aware chunk builder: 3,579 page metadata rows; 7,598 chunks; 3,092 pages with text; 487 records without non-whitespace chunks.
- SQLite FTS5 lexical retrieval; default namespace 0; explicit `--include-context`.
- Exact page-ID lookup and exact title/direct redirect lookup via `--title`; aliases retain redirect provenance and do not merge identities.
- Date-bearing contrast mode via `--contrast`; returns diversified lexical candidates and heuristic `date_signals`, flags multiple date ranges for human review.
- Four contrast regression checks were recorded as passing against the uploaded version-002 SQLite index; see `research/rag/contrast-smoke-tests-001.json`. This is a smoke/regression check, not a benchmark.
- Source-aware infobox extraction is now implemented in `research/rag/extract_infobox_claims.py`, with schema `research/rag/infobox-claim.schema.json` and conservative event-scoped comparison in `research/rag/evaluate_infobox_claims.py`. The evaluator requires same page subject, an explicit reviewed `event_scope_id`, template family, and exact normalized parameter name. Repeated parameters without event-scope annotation remain unresolved, not conflicts. Detailed evidence: `research/rag/infobox-claims-pass-001.md`.
- Regression test source is `research/rag/test_infobox_claims.py`, and `research/rag/infobox-claims-pass-001.md`. The five committed parser/comparison regression tests passed in GitHub Actions (run 44925739208, Python 3.11.18). The committed extractor, schema, and evaluator sources were subsequently verified against their Git blob SHAs and executed against the pinned ZIP: 507 main-namespace pages, 143 infobox invocations, 4,381 claims, 4,381 unique IDs, zero source errors; all claims passed JSON Schema and exact offset/provenance checks; a second run was byte-identical. Evaluator output: zero scoped conflict candidates and two unresolved groups (page 636 `office`; page 1343 `order`). Machine report: `research/rag/infobox-claim-validation-001.json`. The 20-case evaluation baseline has passed independent source-locator review: all ten registered source identities, 51 cited locator/content ranges, and seven title/map-boundary checks passed; Q09/Q16/Q17 locator corrections are recorded in `research/rag/evaluation-locator-validation-001.json`. Maintainer approval received 2026-11-21; retrieval pass 001 records page recall, locator coverage, entity/redirect resolution, and schema correction. All 20 evidence packets now validate against the updated schema. Q18's map reference is present in raw Wikitext and page-manifest `images` metadata, but its binary is absent from the asset manifest and ZIP; see the correction in `research/rag/evaluation-set-001.md`. Manual answer-generation pass 001 is now recorded in `research/rag/answer-generation-pass-001.md`: 20/20 answer-key criteria met, 20/20 cited cases, 4/4 contradiction disclosures, and 3/3 required abstention/qualified-absence cases. This was manual source-grounded composition from retrieved page IDs plus full-page expansion, not CLI-generated answers or independent scoring; automated citation precision and independent claim-support remain unmeasured.

Key files:
- `research/rag/build_index.py`
- `research/rag/build_alias_index.py`
- `research/rag/search.py`
- `research/rag/test_search.py`
- `research/rag/evidence-packet.schema.json`
- `research/rag/evaluation-set-001.md`
- `research/rag/evaluation-locator-validation-001.json`
- `research/rag/retrieval-benchmark-pass-001.json`
- `research/rag/answer-generation-pass-001.md`
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

1. Continue from `research/continuity/corrected-realism-audit-001.md` and `research/continuity/corrected-realism-proposal-001.md`; keep this branch non-canon.
2. Resolve the editorial mode: realism-first retcon versus lore-preserving technology divergence.
3. Reconcile the Second Chinese Civil War's 2027–2048 source date with the revised 2024–2034 chronology.
4. Choose the intended White Tide scale and reconcile the WIP article's multi-million force/casualty claims, 2028–2035 infobox, 2033 Battle of Salmon endpoint, and the timeline's 2028–2031 range.
5. Define the Flood's sea-level curve, 300m death estimate, and 2.4bn displacement categories; reconcile Great Famine's 2032/2033 end date and mortality accounting.
6. Decide whether the 2023 Mars expedition remains canon; if retconned, revise the full 2025–2033 colony/terraforming sequence, not only the first landing date.
7. Only after these decisions, produce a full replacement timeline and dependency checklist. Do not edit Bronze/canon pages without separate explicit authorization.
8. Deferred RAG task on the audit baseline: execute exact committed index/search Git blobs against the pinned archive and regenerate evidence packets; preserve the benchmark pass-001 reconstruction caveat until then.

## 5. Open questions / blockers

- What is the most reliable extraction boundary for infobox templates without a full MediaWiki renderer? Raw template parameter parsing may need nested-brace-aware parsing.
- Which of the observed infobox template families should be supported first? Start with the already audited high-value families and document exclusions.
- How should claim identity be represented so repeated dates for different phases are not mistaken for conflicts?
- The 20-question evaluation set is maintainer-approved; retrieval pass 001 and manual answer-generation pass 001 are recorded. Automated answer-generation, citation precision, and independent claim-support evaluation remain pending.
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
- Branch: `experiment/corrected-realism`
- Base: `audit/continuity-research` at `d93184ad0f78af7b96d264e2bd00d95a8bd61736` (read-only reference)
- Last verified HEAD before this swap refresh is recorded at the top of this file.
- Latest milestone: five committed parser/comparison regression tests passed in GitHub Actions; continuity validation, compileall, and existing pytest suite also passed. The committed extractor/evaluator ran against the pinned archive; all 4,381 claims passed schema/offset/provenance validation, with deterministic repeat output. See `research/rag/infobox-claim-validation-001.json`.
- New files: `research/rag/extract_infobox_claims.py`, `research/rag/evaluate_infobox_claims.py`, `research/rag/infobox-claim.schema.json`, `research/rag/test_infobox_claims.py`, `research/rag/infobox-claim-validation-001.json`.
- Updated permanent docs: RAG README, infobox pass-001 note, evaluation set and locator report, master register, research README, session log, and `agents.md`.
- No PR, merge, branch promotion, or canon/source-data edit was performed for that milestone.
- Current branch: `experiment/corrected-realism`, branched from audit HEAD `d93184ad0f78af7b96d264e2bd00d95a8bd61736`. Proposal and audit: `research/continuity/corrected-realism-proposal-001.md` and `research/continuity/corrected-realism-audit-001.md`. Audited all five changed paths against base, plus agent/governance instructions; verified 13 Bronze source hashes and external calibration references. Key unresolved decisions include Chinese Civil War 2027–2048, White Tide scale, Flood mortality/displacement, Great Famine dates, and Mars 2023–2033 technology. Master register, README, agent guide, session log, and swap are synchronized. No tests, canon edits, PR, merge, or branch promotion.

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
