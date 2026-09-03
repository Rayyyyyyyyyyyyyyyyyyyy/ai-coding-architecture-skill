---
name: rescue-vibe-project
description: User-invoked recovery of one trustworthy slice in a brittle existing project, without assuming a rewrite.
disable-model-invocation: true
---

# Rescue Vibe Project

Restore one verified, changeable vertical slice; do not certify the whole repository.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Baseline

- Preserve and distinguish existing uncommitted work.
- Recover runtime, package manager, commands, architecture context, persistence/external boundaries, and the critical user journey.
- Record exact known-good behavior and failures across install, build, start, and the selected path.
- Treat code, tests, schemas, migrations, callers, runtime behavior, and documentation as separate evidence.
- Do not start with framework replacement, broad upgrades, reformatting, deletion, or a new architecture.

## Triage

Prioritize:

1. install/build/start/critical-path blockers;
2. security, authz, secrets, persistent data, destructive operations;
3. regressions and missing feedback loops;
4. conflicting ownership/models/boundaries blocking safe change;
5. local maintainability blocking the selected repair.

Defer cosmetic debt, speculative abstraction, dependency churn, and unrelated modernization.

## Repair one slice

Choose the smallest vertical slice that restores a user outcome or reliable development baseline. Invoke only installed skills whose signal occurs:

| Signal | Invoke through the host mechanism |
| --- | --- |
| causal failure investigation | `debug-with-evidence` |
| dependency/trust/auth/data/runtime/destructive risk | `safe-change` |
| non-trivial frontend boundary | `coding-architecture` |
| relevant journey states | `experience-completeness` |
| durable architectural intent | `architecture-context` |
| exit verification | `verify-before-done` |

Reuse existing conventions, add the nearest regression-capable feedback loop, keep changes reversible, and update architecture context only when durable intent changes.

## Exit

Stop when:

- the selected outcome works at the strongest locally available boundary;
- a focused feedback loop detects its regression;
- material security, data, compatibility, external, and production limits are explicit;
- unrelated failures remain separated from the verified slice.

Continue only within the authorized rescue scope. Stop for product decisions, unavailable external access, destructive migration, or broad rewrite.

On actual agent transfer invoke `a2a-handoff`. Report the verified slice and remaining boundaries, not a code-smell catalog or whole-repository health claim.
