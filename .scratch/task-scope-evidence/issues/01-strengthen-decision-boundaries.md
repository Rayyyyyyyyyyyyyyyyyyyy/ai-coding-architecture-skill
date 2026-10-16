# Strengthen task and evidence boundaries

Status: resolved
Triage: ready-for-agent

Implement the approved narrow updates described in [the spec](../spec.md).

## Comments

- User approved the proposed changes with “可以喔”.

## Answer

Updated the three skills and shared composition rule. Frontend recommendations
now weigh concrete maintenance benefit against change and verification cost;
debugging identifies symptom and expectation provenance; verification traces
assertions to in-scope requirements and reassesses growing infrastructure work
without weakening acceptance. Existing authorization boundaries remain intact.

Added eight behavioral case specifications across frontend, debug, verify, and
cross-skill suites, including positive controls for useful refactoring, an
observed in-scope regression, and a small authorized test-import repair.

Verification:

- All three skills passed `skill-creator/scripts/quick_validate.py`.
- `git diff --check` passed; final diff reviewed for scope and consistency.
- The eight cases are specifications, not executed behavioral evaluation runs.
- No browser checks were run. Installed copies under `~/.agents/skills` were not
  updated; this change applies to repository sources.
