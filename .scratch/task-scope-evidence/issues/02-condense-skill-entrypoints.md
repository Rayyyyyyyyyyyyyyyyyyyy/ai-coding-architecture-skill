# Condense skill entrypoints without losing decision boundaries

Status: resolved
Triage: ready-for-agent

Consolidate repeated rules in `vibe-frontend`, `vibe-debug`, and `vibe-verify`
under the approved follow-up in [the spec](../spec.md). Preserve routing and
the decision boundaries covered by existing behavioral cases. Do not add
references or new process requirements just to shorten the entrypoints.

## Comments

- User approved the consolidation with “ok”. Before-edit word counts, including
  frontmatter: frontend 1,255; debug 569; verify 512.

## Answer

Consolidated authority, evidence, reporting, and stopping instructions within the
three existing entrypoints, without adding references or changing discovery
metadata. Final word counts including frontmatter: frontend 771 (38.6% less),
debug 434 (23.7% less), verify 445 (13.1% less). Total: 2,336 to 1,650 (29.4% less).

Static comparison against the case specifications retained:

- frontend review scope, language, change-record reuse/fallback, state ownership,
  provider normalization, meaningful extraction, and maintenance-value decisions;
- debugging authority, symptom/expectation provenance, red-capable evidence,
  instrumentation routing, three-attempt reframing, and in-scope regression fixes;
- verification-only versus finishing authority, evidence/claim levels, negative
  assertions, cost reassessment, and necessary acceptance criteria;
- cross-skill scope containment and conditional verification/handoff invocation.

All three skills passed `quick_validate.py`; metadata remained unchanged, local
reference links resolved, and `git diff --check` passed. Behavioral case
specifications were unchanged by this consolidation and were not executed as
agent evaluations. No browser checks or installed-copy updates were performed.
