# Project Cases

Use `vibe-project` in the mode selected by the user. Explanation cases and fixtures
remain in [the explanation suite](../explain-project/cases.md); its old directory
name preserves historical run paths and is not an installed skill name.

## Combined explanation and assessment

Fixture: The API and worker fixture below has one reachable order flow and
competing job-state writers. No implementation has been requested.

Request: 用 $vibe-project 帶我看懂這個 repo 的資料流，順便指出架構問題。先不要改。

Expected: Use one shared map and trace to explain the flow, then assess the
competing state owners with source evidence, concrete consequences, confidence,
and proportionate recommendations. Explain current behavior separately from
the judgment. Keep inquiry read-only; do not demand separate mode invocations
or repeat discovery as if this were two unrelated tasks.

## Assessment follow-up reuses the walkthrough

Fixture: A previous explanation established the entry points and state flow.
One worker changed since that turn; other relevant evidence remains available.

Request: 那剛才這條流程的架構有問題嗎？

Expected: Reuse the established map, inspect the changed worker and any missing
evidence, and assess the selected boundary. Do not restart the whole survey or
treat prior static findings as runtime proof. Do not implement recommendations.

## Explicit report artifact

Fixture: A source-grounded assessment is complete and the user wants it saved.

Request: Save the assessment to docs/architecture-review.md.

Expected: Write only the requested report with findings and evidence limits.
Do not repair code, create tickets, or synchronize design records.

## Repository-wide assessment across execution units

Fixture: A repository contains a browser application, API process, background
worker, scheduled reconciliation command, relational database, and external
provider adapter. The API and worker both write job status using separate
transition rules. The browser polls the API, while the provider callback can
arrive before or after the worker result. Workspace configuration and runtime
registration reveal all four executable units. Some architecture documentation
describes an older single-process design.

Request: Where does this repository's architecture have material problems?
Assess the whole repository without changing anything.

Expected:

- inspect repository instructions, workspace configuration, executable entry
  points, runtime registration, storage and external integration setup;
- account for the browser, API, worker, and reconciliation command, and name any
  material unit or external boundary that was not inspected;
- trace at least one state-changing path and the background/provider path far
  enough to establish the implemented state owners and observable outcomes;
- treat the outdated documentation as intent evidence rather than proof of the
  active architecture;
- report the competing job-transition ownership only with source evidence, a
  concrete ordering or recovery scenario, affected units/data, impact,
  confidence, and a proportionate recommendation assigning one owning boundary;
- distinguish behavior observed in a runtime from static inference and avoid
  claiming deployed database or provider behavior from repository files alone;
- keep the repository read-only and do not create an issue, architecture record,
  implementation plan, refactor, or completion-verification claim.

## Healthy unconventional repository

Fixture: A small product keeps its API and scheduled work in one process and its
browser application in a few large JavaScript modules. One database is the
documented and implemented source of truth. Public request and job contracts are
validated at their boundaries, failure recovery is explicit, and focused tests
exercise the consequential rules and cross-unit contract. The layout does not
follow a conventional layered folder structure.

Request: Audit this repository's architecture and tell me what should be fixed.
Do not modify it.

Expected: Inspect the reachable execution units and representative boundaries,
then state that no material finding was established if the evidence supports
that conclusion. Do not treat the monolith, JavaScript, large files, directory
shape, process count, or unfamiliar organization as architecture defects, and
do not recommend TypeScript, microservices, layers, or additional abstractions
without a demonstrated consequence.

## Focused boundary does not become a whole-repository claim

Fixture: A repository contains several applications and workers. The request is
limited to how the import CLI hands parsed records to the core application. The
inspected path reveals that both sides independently normalize the same enum,
and a new enum value requires coordinated edits. Other runtime units are not
relevant to that boundary and are not inspected.

Request: Is the import boundary architecturally sound? Review it without making
changes.

Expected: Inspect the CLI registration, caller, normalization, application
contract, and focused evidence needed for that boundary. If reporting the
duplicated contract, provide the concrete change scenario, impact, confidence,
and smallest owning-boundary recommendation. State the focused scope and do not
generalize the result into a whole-repository health assessment.

## Actual failure routes to diagnosis

Fixture: A multi-process application intermittently loses webhook updates. Both
`vibe-project` and `vibe-debug` are installed. No
reproduction or causal evidence exists yet.

Request: Diagnose why webhook updates are intermittently lost. Do not fix it.

Expected: Select `vibe-debug` to establish reproducible causal evidence
rather than using an architecture assessment as a speculative bug diagnosis.
Use `vibe-project` only if the established cause or an explicit
follow-up request requires judging a system boundary.
