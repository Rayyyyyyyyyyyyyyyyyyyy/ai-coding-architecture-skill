---
name: verify-before-done
description: Collect proportionate evidence for an executable change and limit completion claims to what it proves. Use for implementation completion or explicit verification, not planning or explanation.
---

# Verify Before Done

Separate implementation, verification, provisioning, and production claims.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Authority

- **Verification only:** run or inspect evidence; do not mutate code, tests, config, fixtures, or external systems to make it pass.
- **Implementation finishing:** fix an authorized in-scope cause exposed by verification, then rerun the affected check.

If the request asks only whether existing work is correct, use verification-only mode.

## Assertions

- Recover requirements from the request, repository, tests, types, and owning boundary.
- Define the smallest observable assertions that prove the change. Add a negative assertion only when required by accepted behavior or policy.
- Do not invent UX, authz, idempotency, data, or deployment policy. Surface missing policy as an unverified boundary.
- Keep evidence proportional to risk and coupling.

## Evidence

| Type | Proves |
| --- | --- |
| structural | types, lint, build, packaging, diff scope |
| focused executable | changed assertion and regression behavior |
| runtime interaction | rendering, input, timing, wiring, side effects |
| trusted boundary | allow/deny/deduplicate/persist/reject policy |
| external/deployed | real provider, credentials, migration, infrastructure, production |

Use the cheapest evidence that directly proves each assertion; combine types only when required. Run focused checks before broader checks. Exercise representative API/CLI inputs and selected UI states when static evidence is insufficient.

For a bug fix, rerun the red-capable loop. If none exists, state the confidence limit; when causal investigation is authorized, invoke `debug-with-evidence`. Inspect the final diff for scope drift, generated artifacts, debug code, and bypasses.

On failure:

- verification-only: report without mutation;
- implementation-finishing: fix only an authorized in-scope cause;
- stop for product decisions, unavailable external state, new authorization, or scope expansion.

## Claim

- **Implemented:** code/config changed.
- **Locally verified:** relevant local evidence passed.
- **Externally provisioned:** required external configuration exists.
- **Production verified:** deployed behavior was exercised in production.

Never promote evidence across these states. Record checks as passed, failed, not run, unavailable, or blocked; do not claim an unobserved result. Report decisive evidence and material unverified boundaries. On actual agent transfer invoke `a2a-handoff`.
