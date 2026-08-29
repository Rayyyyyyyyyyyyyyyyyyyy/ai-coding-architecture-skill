---
name: ai-coding-architecture
description: Apply a pragmatic architecture contract when implementing, refactoring, planning, or reviewing application code. Use for changes involving feature structure, components, hooks, schemas, domain models, services, adapters, repositories, external data or AI boundaries, state, forms, responsive UI, accessibility, testing, dependencies, or code-review decisions where maintainability, reuse, composition, coupling, and appropriate abstraction matter.
---

# AI Coding Architecture

Apply the contract as engineering decision guidance while respecting the user's request and the repository's own instructions and conventions.

## Establish context

1. Read repository instructions and inspect the existing implementation before proposing or making changes.
2. Identify the project's current framework, design system, directory conventions, domain model, state approach, and test strategy.
3. Search for equivalent components, hooks, utilities, services, types, schemas, adapters, and repositories.
4. Read [references/architecture-contract.md](references/architecture-contract.md) before architectural implementation, refactoring, or review. For a narrowly scoped change, focus on the relevant numbered sections plus sections 15, 16, 39, 48, 49, and 50.
5. Treat examples in the contract as illustrative. Adapt them to the project's actual stack and domain rather than imposing the travel examples or suggested directory tree literally.

## Make decisions in order

Use this sequence:

1. Reuse an existing implementation.
2. Compose existing parts.
3. Extract behavior or knowledge that is meaningfully repeated.
4. Abstract only to solve a concrete boundary, coupling, replacement, testability, or complexity problem.

Prefer the smallest change that preserves behavior and improves clarity. Do not perform unrelated rewrites or introduce architecture theater.

## Preserve boundaries

- Keep feature-specific UI, logic, hooks, types, schemas, services, and utilities with the owning feature until reuse is real.
- Normalize and validate untrusted external inputs at system boundaries before exposing canonical domain models to feature logic or UI.
- Keep vendor response types and implementation details out of presentation components.
- Keep business rules out of dense rendering conditionals when they represent meaningful domain behavior.
- Keep state as local as practical, derive values instead of synchronizing duplicates, and use effects primarily for external synchronization.
- Use the project's existing UI primitives and design tokens before creating new primitives or visual conventions.
- Add services, adapters, repositories, interfaces, contexts, stores, and dependencies only when each has a concrete responsibility.

## Implement and verify

1. Define or confirm important domain contracts before building dependent UI behavior.
2. Make responsibilities and public APIs small, semantic, and predictable.
3. Cover loading, empty, error, partial-data, responsive, and accessibility behavior when relevant.
4. Prioritize tests for business rules, normalization, parsing, schema validation, adapters, complex stateful behavior, and critical user flows.
5. Run the repository's required checks and inspect the final diff for accidental scope expansion.
6. Use the code-review checklist in section 49 of the reference before declaring completion.

## Resolve conflicts

Follow higher-priority user and repository instructions when they conflict with this contract. Preserve established project conventions unless changing them is explicitly requested or clearly necessary. State material deviations and their concrete reason in the handoff.
