# Frontend architecture assessment

Strengthen `coding-architecture` so it can assess an existing frontend before a
specific implementation or refactor has been requested.

The skill should distinguish a large file or JavaScript codebase as an
investigation signal from a demonstrated architecture problem. It should inspect
responsibility and change boundaries, state and effect ownership, frontend data
contracts, test seams, and type/runtime validation. Findings must include code
evidence, impact, and a proportionate recommended scope while advice remains
read-only.

For established JavaScript projects, ordinary feature implementation should
continue to follow the existing language. An architecture assessment may discuss
TypeScript or runtime validation only when repository evidence shows that either
would address a material contract or maintainability problem. Assessment does not
authorize a migration.

Update discovery metadata, routing documentation, and behavioral cases so a
request such as “review this React project's architecture” selects this skill and
does not degrade into a line-count or folder-layout critique.
