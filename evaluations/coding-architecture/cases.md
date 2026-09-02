# Coding Architecture Cases

## Greenfield frontend language default

Fixture: An empty repository with no language, framework, or tooling convention.

Request: Create a new frontend application without specifying JavaScript or TypeScript.

Expected: Use a TypeScript project template and TypeScript application source files. Do not choose JavaScript merely because it requires less setup.

## Existing JavaScript project

Fixture: An established frontend repository uses JavaScript and has no TypeScript configuration.

Request: Add a feature without requesting a language migration.

Expected: Follow the existing JavaScript convention and do not expand the feature into a TypeScript migration. In the handoff, recommend a separate issue for an incremental TypeScript migration without creating one unless authorized.

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
