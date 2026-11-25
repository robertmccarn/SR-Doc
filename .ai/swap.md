# SR-Doc — AI session swap memory

> **Role:** Compact, repo-backed handoff snapshot for AI work. This file is mutable working memory, not canon, source evidence, or a chronological log.
> **Last verified against GitHub:** 2026-11-25 (after realism-first retcon decision and timeline update)
> **Branch:** `experiment/corrected-realism`
> **Branch HEAD before this swap refresh:** `9171b18e18332b00e011142542a7b216fb13468e`
> **Maintainer:** User-directed SR-Doc workflow; agents may update this file under `research/continuity/DOCUMENTATION-GOVERNANCE.md`.

## 1. Mission and standing constraints

Continue the source-grounded SR-Doc corpus audit and research-assistant/RAG implementation. The `experiment/corrected-realism` branch is a user-authorized, non-canon editorial offshoot. The maintainer has selected a realism-first retcon: no departure from authentic realism before 2041. The current editorial authority is `research/continuity/realism-first-timeline-2024-2040.md`. The repository and captured source data—not chat history, model memory, or this swap file—are authoritative.

- Current user-designated working branch is `experiment/corrected-realism`; work here unless explicitly directed otherwise. Treat `audit/continuity-research` at `d93184ad0f78af7b96d264e2bd00d95a8bd61736` as the read-only base for this offshoot.
- No merge, PR, branch promotion, canon edit, or Bronze/Silver source modification without explicit user approval.
- Bronze captures/manifests are immutable evidence.
- Preserve contradictions; never silently adjudicate or normalize claims.
- Distinguish observed, computed, inferred, hypothesis, and unresolved.
- Main namespace is the default lore evidence. Talk/Thread/User/community namespaces are contextual/editorial and require explicit opt-in.
- Do not claim tests or builds ran unless execution actually succeeded. Record test scope and limitations.
- Never place credentials, tokens, private keys, personal secrets, or other sensitive data here.

## 2. Active workstream

**Current branch: non-canon realism-first retcon through 2040.**
- Binding decision (2026-11-25): no departure from authentic real-world scientific, technological, demographic, economic, institutional, military, or geopolitical plausibility before 2041.
- Current editorial authority: `research/continuity/realism-first-timeline-2024-2040.md`.
- Source audit: `research/continuity/corrected-realism-audit-001.md` (13 relevant Bronze page hashes matched the pinned archive manifest).
- Superseded historical draft: `research/continuity/corrected-realism-proposal-001.md`. Retain for source inventory/history only; do not implement its 2024–2034 chronology.
- The replacement note distinguishes observed history through 2026-11-25 from conditional 2027–2040 scenarios, defines hard constraints, records the retcon matrix, and lists known dependent pages plus validation gates.
- Required retcons: remove the global Flood/near-30m sea-level curve and extreme death/displacement totals; remove the global Great Famine and extraordinary mortality; remove the 2027–2048 Second Chinese Civil War and Three Gorges Dam trigger; reduce White Tide to bounded domestic extremism at most; remove Russian dissolution/nuclear seizure and Turkish occupation/pipeline; remove the 2023/2026 crewed Mars program and 2029–2033 terraforming; remove unsupported U.S. 400m population, 90m displacement, and wholesale housing seizure.
- No canon edits, Bronze/Silver modifications, manifest changes, RAG implementation changes, PR, merge, or branch promotion are authorized. A later canon-edit phase requires separate explicit approval.

**Inherited baseline: RAG source-aware claim extraction and contradiction evaluation.**

## 3. Current known test case / continuity issue

- Page 1413, **Second Chinese Civil War**, contains infobox dates 2027–2048 and a combatant period marked 2105–2111.
- Page 1408, **Third Chinese Civil War**, covers phases beginning in 2105 and extending through 2126.
- The contrast retriever surfaces the page-1413 multi-range passage and page 1408 for comparison.
- This is a confirmed source-level inconsistency candidate, not a resolved chronology. Field labels, event scope, and any creator/community explanation still need review.
- The date regex is heuristic; it does not parse infobox field semantics. Lexical OR matching can be noisy. Retrieval pass 001 found all expected pages by top five unique candidates, but first-stage locator coverage was 47/55; full-page expansion raised it to 55/55. Contrast candidate precision remains noisy and no semantic contradiction precision is claimed.

## 4. Immediate next steps

1. Continue from `research/continuity/realism-first-timeline-2024-2040.md`; do not use the superseded 2024–2034 chronology as the working recommendation.
2. Perform dependency discovery for every retired event, entity, date, number, and consequence: exact titles, page links, categories, redirects, infoboxes, text mentions, and transclusions. Distinguish direct dependencies from mere mentions.
3. Build a claim ledger with source page/revision, old value, proposed disposition, evidence, confidence, and every dependent page.
4. Reconcile the timeline and dependent pages together; validate quantitative definitions, institutions, logistics, science/technology readiness, and event start/peak/end/aftermath dates.
5. Do not edit accepted canon until the user separately authorizes a canon-edit phase.
6. Deferred RAG task on the audit baseline: execute exact committed index/search Git blobs against the pinned archive and regenerate evidence packets; preserve the benchmark pass-001 reconstruction caveat until then.

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
