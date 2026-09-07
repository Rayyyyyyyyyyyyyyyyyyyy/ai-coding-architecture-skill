---
name: coding-architecture
description: Assess or structure non-trivial frontend changes through semantic reuse, composition, clear ownership, and justified abstraction. Keep advice-only requests read-only. Not for backend-only work or cosmetic edits.
---

# Coding Architecture

Make the smallest cohesive frontend change that fits the existing system.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Scope

- **Advice or assessment:** when asked to analyze architecture or find refactoring opportunities, report candidate issues with evidence, impact, and recommended scope; do not edit files or invoke implementation-completion verification.
- **Implementation:** when development or refactoring is requested, apply the decision order within the authorized scope. Do not require a second approval for routine in-scope choices; obtain agreement before expanding the scope or resolving a missing product decision.
- Follow user and repository instructions.
- Preserve the framework, design system, directory conventions, state model, and test strategy unless the task requires change.
- Own frontend language selection, component/state boundaries, semantic reuse, frontend data normalization, and abstraction decisions.
- Do not reorganize unrelated modules or absorb security, UX completeness, verification, or handoff ownership.

## Language

- Greenfield JavaScript ecosystem with no convention: TypeScript unless the user or runtime requires JavaScript.
- Existing TypeScript scope: stay in TypeScript.
- Existing JavaScript scope: stay in JavaScript unless migration is requested; do not propose an incidental migration.

## Decision order

**Reuse → Compose → Extract → Abstract**

1. Inspect conventions, primitives, data shapes, state ownership, dependencies, callers, and tests.
2. Reuse an equivalent contract; visual similarity alone is insufficient.
3. Compose when consumers need arrangement without merged responsibilities.
4. Extract behavior that repeats semantically, changes for the same reason, obscures ownership, or needs an independent test boundary.
5. Abstract only for a concrete boundary: multiple real implementations, vendor isolation, business rules, replacement, or testability.

Line count, prop count, and hypothetical reuse are investigation signals, not extraction criteria.

## Boundary rules

- Keep one state owner; derive values instead of synchronizing copies. Use context/store only for real cross-tree coordination.
- Keep business rules outside dense rendering conditionals when independently meaningful.
- Normalize untrusted or vendor data at its entry boundary into a canonical application model.
- Keep feature code local until semantic reuse is demonstrated; expose shared code through a small named API.
- Prefer existing framework/design-system/platform capability. On a real dependency-risk signal, invoke `safe-change`.
- Prefer domain names over `utils`, `helpers`, `common`, or universal configurable components.

Report only a material boundary, abstraction, or intentional convention deviation. On implementation completion invoke `verify-before-done`; on actual agent transfer invoke `a2a-handoff`.
