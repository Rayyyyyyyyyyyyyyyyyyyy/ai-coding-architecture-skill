# Behavioral Evaluation Cases

Use these cases to compare agent behavior with and without the skill, or before and after a substantial skill revision. Evaluate the implementation and reasoning, not whether the response repeats wording from `SKILL.md`.

## Evaluation method

For each case, provide the agent with a small realistic repository fixture and the user request. Do not reveal the expected decisions. Score the result on:

1. respect for the requested scope and repository conventions;
2. semantic reuse rather than reuse based only on visual similarity;
3. proportional extraction and abstraction;
4. clear ownership of state, business rules, and external data;
5. verification proportional to the change's risk.

## Cases

### 1. Existing dialog primitive

The repository already has a design-system dialog wrapper. Ask the agent to add a confirmation dialog to one feature.

Expected behavior: discover and reuse the wrapper, keep feature-specific behavior in the feature, and avoid creating another modal primitive.

### 2. One-off promotional card

Ask the agent to add a visually distinctive promotional card used on one page. The repository has several cards with similar spacing but different semantics.

Expected behavior: reuse low-level design tokens or primitives where appropriate, but do not force the new card and unrelated cards into a generic configurable component.

### 3. Large mixed-responsibility component

Provide a component that combines rendering, external synchronization, a meaningful business rule, and several ordinary view conditions. Ask for a behavior-preserving refactor.

Expected behavior: split along cohesive responsibilities rather than line count, extract the business rule and external synchronization where useful, and keep simple view logic near the UI.

### 4. Second external provider

The application currently exposes one provider's response shape directly to several components. Ask the agent to add a second provider with a different response shape.

Expected behavior: introduce a canonical application model and provider adapters at the boundary, without creating speculative repositories or dependency-injection machinery that the two implementations do not need.

### 5. Shared state temptation

Ask the agent to share a filter value between a parent and two nearby children in an application that already uses a global store elsewhere.

Expected behavior: keep ownership local and pass state explicitly unless the fixture demonstrates genuine cross-tree coordination; do not use the global store merely to avoid ordinary prop passing.

## Failure signals

- unrelated directory or architecture reorganization;
- a new primitive that duplicates the existing design system;
- generic components controlled by unrelated boolean modes;
- context, stores, services, adapters, or interfaces without a concrete boundary;
- raw provider types leaking further into the UI;
- tests that assert implementation wording instead of observable behavior.
