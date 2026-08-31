# Behavioral Evaluation Cases

Use these cases to compare agent behavior with and without the skill, or before and after a substantial skill revision. Evaluate the implementation and reasoning, not whether the response repeats wording from `SKILL.md`.

## Evaluation method

For each case, provide the agent with an isolated, minimal repository fixture and the user request. Give the expected behavior only to the evaluator, not the agent. Score the result on:

1. respect for the requested scope and repository conventions;
2. semantic reuse rather than reuse based only on visual similarity;
3. proportional extraction and abstraction;
4. clear ownership of state, business rules, and external data;
5. recovery and preservation of repository-local architecture context;
6. verification proportional to the change's risk.

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

### 4. Cross-agent second provider

The fixture represents work continued from another agent. A local `ARCHITECTURE.md` documents the flow `provider → adapter → canonical model → feature`. Ask the agent to add a second provider with a different response shape.

Expected behavior: discover and preserve the documented data flow, add the provider adapter at the existing boundary, and avoid speculative repositories or dependency-injection machinery.

### 5. Shared state temptation

Ask the agent to share a filter value between a parent and two nearby children in an application that already uses a global store elsewhere. The feature's `ARCHITECTURE.md` explicitly assigns this state to the feature subtree.

Expected behavior: read the local architecture context, keep ownership local, and pass state explicitly unless genuine cross-tree coordination requires a change.

### 6. Similar components with an explicit semantic boundary

Provide two visually similar components. Local architecture documentation says they intentionally remain separate because they represent different domain contracts and change for different reasons. Ask the agent to add behavior shared at the visual level.

Expected behavior: reuse low-level primitives when useful while preserving the documented semantic separation; do not merge the components into one boolean-driven abstraction.

### 7. Material architecture change

The fixture has an existing `ARCHITECTURE.md`. Ask for a legitimate change that moves state ownership or changes a public dependency boundary.

Expected behavior: implement the requested change and update the nearest relevant architecture document in the same change, without rewriting unrelated documentation.

### 8. Trivial presentational badge

Ask the agent to add a simple, feature-local status badge in a directory without architecture documentation.

Expected behavior: implement the badge normally and do not create `ARCHITECTURE.md`; the change introduces no durable architectural knowledge.

### 9. Stale architecture documentation

Provide a local architecture document that conflicts with current types, callers, tests, and a recent repository decision. Ask for a nearby non-trivial change.

Expected behavior: identify the exact conflict, use repository evidence to determine which side is stale, and synchronize it when safe. If intent remains materially ambiguous, preserve the current boundary and surface the decision instead of guessing.

## Failure signals

- unrelated directory or architecture reorganization;
- a new primitive that duplicates the existing design system;
- generic components controlled by unrelated boolean modes;
- context, stores, services, adapters, or interfaces without a concrete boundary;
- raw provider types leaking further into the UI;
- ignoring relevant local architecture documentation;
- leaving architecture documentation stale after changing a documented boundary;
- creating `ARCHITECTURE.md` for trivial or self-evident implementation details;
- blindly following stale documentation despite stronger repository evidence;
- tests that assert implementation wording instead of observable behavior.
