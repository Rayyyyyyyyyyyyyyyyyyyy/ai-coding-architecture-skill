---
name: coding-architecture
description: Enforce maintainable frontend architecture when implementing or refactoring UI. Use existing UI frameworks, reusable components, composables/hooks, clear boundaries, and justified abstractions instead of page-specific or duplicated code.
---

# Coding Architecture

Build for maintainability and composition, not just for the current screen.

Follow this order when solving problems:

**Reuse → Compose → Extract → Abstract**

## Architecture rules

1. Inspect the existing codebase before creating a new component, hook, composable, utility, service, type, or abstraction. Reuse or extend existing implementations when appropriate.
2. Use the project's existing UI framework and design system. Prefer framework primitives over custom implementations for buttons, dialogs, forms, tabs, cards, menus, and similar UI.
3. Use feature-based, component-driven architecture. Keep components small, focused, reusable, and responsible primarily for rendering and interaction.
4. Prefer composition over configuration. Avoid god components and components controlled by many boolean props. Use compound components when related UI parts benefit from independent composition.
5. Extract reusable stateful or behavioral logic into hooks/composables. Keep business logic outside presentational components.
6. Keep state as local as practical. Derive values instead of duplicating synchronized state. Avoid unnecessary effect chains and prop drilling.
7. Use schema-first, type-safe domain models for important application data. Normalize external API, file, or AI data at the boundary before exposing it to UI components.
8. Use services or adapters when they isolate external dependencies, vendor APIs, data sources, or meaningful business behavior. Do not leak vendor-specific structures throughout the application.
9. Introduce abstractions only for concrete reasons such as repeated behavior, dependency isolation, multiple implementations, complex business rules, or testing boundaries.
10. Avoid premature abstraction, speculative generalization, unnecessary design patterns, duplicate concepts, generic `utils` dumping grounds, and architecture theater.
11. Prefer explicit domain names and clear module boundaries. Feature-specific code stays inside its feature until reuse is demonstrated.
12. Before adding a dependency, verify that the framework, UI library, standard library, or existing project dependency does not already solve the problem.

## Preferred patterns

Favor these when appropriate:

- Feature-based architecture
- Component-driven UI
- Design-system driven development
- Composition over inheritance
- Compound Component Pattern
- Custom Hooks / Composables
- Separation of Concerns
- Single Responsibility Principle
- Schema-first domain modeling
- Adapter Pattern
- Service Layer
- Dependency Inversion when justified

Do not apply patterns mechanically. Use the simplest structure that preserves clear boundaries, composability, reuse, and replaceability.

## Before finishing

Check that the implementation:

- reuses existing primitives and components where possible;
- does not duplicate existing logic or concepts;
- has no unnecessary god component or boolean-prop explosion;
- keeps business logic separate from presentation where useful;
- keeps external data and vendor dependencies behind clear boundaries;
- remains easy for another developer or coding agent to understand and extend.
