---
name: rescue-vibe-project
description: User-invoked recovery of one trustworthy slice in a brittle existing project, without assuming a rewrite.
disable-model-invocation: true
---

# Rescue Vibe Project

First present the findings and agree on a repair checklist with the user. Then restore one verified, changeable vertical slice; do not certify the whole repository.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Baseline

- Investigate and gather evidence before implementation. Do not edit project files, apply fixes, or change dependencies, configuration, or persistent data before checklist agreement.
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

## Agree on the checklist before implementation

Present the issues found as a numbered checklist before making repairs. For each item, include the evidence/location, user impact and priority, proposed repair scope, and how success will be verified. Distinguish confirmed failures from unverified suspicions, and mark which items you recommend fixing now versus deferring.

Propose the smallest vertical slice that restores a user outcome or reliable development baseline. Ask the user to confirm or adjust the checklist and wait for an explicit response. Invoking this skill, a general request to rescue the project, or silence does not approve the proposed items. If no actionable issue is found, report that result instead of inventing a repair.

Record the agreed items and deferred items in the conversation, then implement only the agreed scope. A clear approval of the presented checklist is sufficient; do not ask again for each agreed item. If new findings require expanding or materially changing that scope, update the checklist and obtain agreement on the change before implementing it.

## Repair one slice

Repair the vertical slice agreed in the checklist. Invoke only installed skills whose signal occurs; invoking a supporting skill does not bypass checklist agreement:

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
