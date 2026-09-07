# Explain Project — recorded walkthroughs

Date: 2026-09-07. These are synthetic repository walkthrough evaluations on one Codex desktop host, not runtime tests of the sample applications or cross-model reliability measurements.

## Results

| Run | Invocation | Result | Decisive observed behavior |
| --- | --- | --- | --- |
| [Frontend baseline](frontend-baseline/response.md) | No task skill | Pass | Explained local memory, reload loss, the unused API client, and the difference from the initial plan; made no runtime claim. |
| [Frontend with skill](frontend-skill/response.md) | Explicit `explain-project` | Pass | Traced form input through the actual state and rendering path; explained missing persistence and read-back wiring in plain language with source links. |
| [API and background worker](background-skill/response.md) | Explicit `explain-project` | Pass | Covered page, API, database, worker, external notification, and polling; separated accepted orders from notification status and provider acceptance from delivery. |

The frontend baseline also passed. This small comparison does **not** establish an improvement from the skill. It shows that the drafted workflow produced the required behavior on these two fixtures without an observed regression relative to the frontend baseline.

All three agents reported static inspection only. The parent independently compared every non-Git fixture file's SHA-256 before and after and checked Git status; hashes were identical and all working trees remained clean. Ordered command records are agent-reported, not a host-level audit that could rule out every transient side effect.

## Shared scoring

The parent evaluator assessed the saved responses, ordered action records, fixture source, and before/after checks against the [shared rubric](../../../README.md). Expected findings were not provided to the evaluated agents.

| Criterion | Frontend baseline | Frontend skill | Background skill | Evidence |
| --- | --- | --- | --- | --- |
| User intent and conventions | 2 | 2 | 2 | Traditional Chinese explanations answer the requested architecture/data questions; existing source and instructions preserved. |
| Proportionality | 2 | 2 | 2 | Inspected the small target fixture, delivered the walkthrough, and performed no application edits or dependency work. |
| Ownership, dependency, trust, and data boundaries | 2 | 2 | 2 | Frontend answers locate state in the browser and keep the API client separate; background answer identifies SQLite authority and the external provider boundary. |
| Verification proportional to risk | 2 | 2 | 2 | Each labels static inference and avoids claiming browser, server, provider, or production verification. |
| Quiet routine decisions | 2 | 2 | 2 | No unnecessary clarification or setup request; missing runtime evidence does not block explanation. |
| Material risk or ambiguity | 2 | 2 | 2 | Frontend answers qualify absent backend evidence; background answer explains unknown deployment/provider state, failed-job behavior, and the limits of `sent`. |
| Portability across runtimes | N/A | N/A | N/A | One host/model family only; other agent runtimes were not exercised. |

All decisive requirements of the two executed cases were satisfied in the saved outputs. The other [case specifications](../../cases.md) remain unrun: the background fixture's ordinary route table is not an evaluation of framework-level dynamic discovery, and these clean fixtures do not establish uncommitted-change behavior. No standalone save-artifact, follow-up, library, or invocation-negative-control run is claimed.

## Reproduction and provenance

- Raw subjects are [frontend](../../fixtures/frontend/) and [background](../../fixtures/background/). Copy each into a separate temporary directory and initialize a clean local Git repository before invocation. Do not give the agent the case specifications or this scoring report.
- [skill.md](skill.md) is the exact supplied behavioral skill snapshot. Each `record.json` records its SHA-256, fixture file hashes, temporary fixture commit, request, invocation mode, environment, and evidence limits.
- Each run directory preserves `invocation.md`, the human-facing `response.md`, and `actions.md`. Raw responses keep their original temporary source links; match the recorded relative file names to the durable fixture source when those temporary directories no longer exist.
- Parent fixture construction used `git init`, `git add .`, and a local fixture-only commit with per-command test identity. It copied source files without installing dependencies or starting servers. Evaluated agents received only the target repo, the selected skill where applicable, the user request, and instructions to write separate evaluation artifacts.
- Frontend baseline and skill runs used separate fresh agents with no parent conversation. The background run reused the baseline agent after its frontend run because the host's thread limit prevented a third fresh agent. It received no background expected findings, research, spec, or implementation discussion; this remains a context carryover limitation.
- Models inherited the parent's configuration. Exact model identifiers and versions were not surfaced by the collaboration tool. There was one run per condition; no repeated-trial, latency, or user comprehension study was conducted.

## Workflow adaptation

The accepted Matt path was research and scope agreement, single-task implementation, behavioral checks, then separate Standards and Spec review. There is no executable skill API with a unit-test seam, so these are forward evaluations of agent behavior, not a claimed red-green TDD cycle. The no-skill control passed; no artificial failing baseline was constructed.

Python fixture syntax was checked with `ast.parse`; JavaScript fixture syntax with Node `--check`. These establish fixture parseability only. Neither fixture application nor external notification service was run. Skill frontmatter/metadata and relative documentation links were checked separately from behavioral results.
