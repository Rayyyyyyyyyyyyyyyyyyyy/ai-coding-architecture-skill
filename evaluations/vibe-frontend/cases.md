# Coding Architecture Cases

## Greenfield frontend language default

Fixture: An empty repository with no language, framework, or tooling convention.

Request: Create a new frontend application without specifying JavaScript or TypeScript.

Expected: Use a TypeScript project template and TypeScript application source files. Do not choose JavaScript merely because it requires less setup.

## Existing JavaScript project

Fixture: An established frontend repository uses JavaScript and has no TypeScript configuration.

Request: Add a feature without requesting a language migration.

Expected: Follow the existing JavaScript convention and do not expand the feature into a TypeScript migration or unsolicited migration recommendation.

## Existing frontend architecture review without a pending change

Fixture: An established React application keeps several components in one large
JavaScript entry module. The root component also loads an external manifest,
persists preferences, owns filtering and overlay state, performs layout
measurement, and sends a mutation request. Components rely directly on the
manifest shape; no runtime schema or focused rule/effect tests exist.

Request: Review this frontend's architecture, tell me what is materially wrong,
and recommend the smallest useful refactoring scope. Do not change code.

Expected:

- inspect reachable frontend entry points, representative flows, callers, and
  tests rather than judging the directory listing alone;
- distinguish file length, colocated components, and JavaScript as investigation
  signals from demonstrated problems;
- assess module/component responsibilities, state and effect ownership, the
  external data contract and runtime validation, current type guarantees, and
  test seams;
- report only material findings with source evidence, a concrete change or
  failure impact, and proportionate recommended scope;
- follow a server endpoint or manifest producer only far enough to establish the
  frontend contract; do not turn server, worker, build-pipeline, or producer
  architecture into findings or recommended changes owned by this skill;
- keep the repository read-only and do not invoke implementation-completion
  verification;
- recommend TypeScript, runtime validation, or both only if the inspected
  contract or maintainability evidence justifies the cost, and do not imply that
  assessment authorizes a migration.

## Healthy JavaScript frontend assessment

Fixture: A small established JavaScript frontend has cohesive local components,
a single state owner, boundary validation for external data, and focused tests
for consequential rules. Several components are intentionally colocated.

Request: Does this frontend need an architecture or TypeScript refactor? Review
it without making changes.

Expected: Inspect the active boundaries and explain when no material problem is
found. Do not treat JavaScript, file length, colocation, or a preferred folder
tree as defects; do not recommend TypeScript without concrete evidence that it
would address a material contract or maintainability problem.

## Existing TypeScript project

Fixture: An established frontend repository uses TypeScript throughout the relevant application scope.

Request: Add a feature without specifying a language.

Expected: Implement the feature in TypeScript and do not introduce JavaScript application files to avoid typing the change.

## Existing dialog primitive

Fixture: The repository has a design-system dialog wrapper.

Request: Add a confirmation dialog to one feature.

Expected: Reuse the wrapper, keep feature behavior local, and avoid another modal primitive.

## One-off promotional card

Fixture: Several cards share spacing but represent different product concepts.

Request: Add a visually distinctive card used on one page.

Expected: Reuse low-level tokens or primitives where useful without forcing unrelated cards into a generic configurable component.

## Large mixed-responsibility component

Fixture: One component combines rendering, external synchronization, a business rule, and ordinary view conditions.

Request: Refactor without changing behavior.

Expected: Split along cohesive responsibilities rather than line count, extract the business rule and external synchronization where useful, and keep simple view logic near the UI.

## Shared state temptation

Fixture: A parent and two nearby children share a filter. A global store exists elsewhere.

Request: Add another consumer of the filter.

Expected: Keep ownership local unless genuine cross-tree coordination is demonstrated; do not use the store merely to avoid ordinary prop passing.

## Provider boundary

Fixture: One provider response currently reaches several components directly.

Request: Add a second provider with a different shape.

Expected: Introduce a canonical application model and focused provider adapters without speculative repositories or dependency-injection machinery.

## Backend-only architecture negative control

Fixture: A service repository contains no frontend application and needs a queue-consumer boundary changed.

Request: Refactor the worker so message acknowledgement belongs to the processing service.

Expected: Do not invoke this frontend architecture skill or impose component, hook, design-system, or frontend state guidance on the backend change.

## Cosmetic edit negative control

Fixture: An established frontend uses a design-system badge with a supported color prop.

Request: Change one local badge from neutral to warning.

Expected: Make the cosmetic edit using the existing API without starting a component-architecture review or extracting a new abstraction.

## Verification ownership

Fixture: A frontend change introduces a focused adapter and the repository has relevant tests and build commands.

Request: Implement the adapter-backed UI change.

Expected: Use this skill to decide the frontend boundary, but leave evidence selection and completion claims to `vibe-verify`; do not duplicate a generic build, lint, test, UX, and handoff checklist inside the architecture workflow.

## Refactoring advice remains read-only

Fixture: A frontend component combines independent business rules and rendering; callers and focused tests are available.

Request: Analyze refactoring opportunities and recommend where to split this component.

Expected: Report candidate boundaries with code evidence, impact, and proposed scope. Do not edit source, tests, or documentation and do not invoke implementation-completion verification.

## Approved refactoring proceeds

Fixture: A previous assessment proposed extracting a calculation while preserving local state ownership and public behavior.

Request: Implement the calculation extraction you proposed; leave state ownership alone.

Expected: Apply and verify the requested extraction without redundant approval. Preserve state ownership and defer any newly discovered unrelated refactoring opportunity.
