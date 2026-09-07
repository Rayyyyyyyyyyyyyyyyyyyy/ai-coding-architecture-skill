# Standards review — explain-project

Reviewed the fixed feature snapshot in `feature-review.patch` against original HEAD `7a753725156fc43b91649de6d672bff04778cb8d` plus the saved pre-feature working tree. Earlier unrelated skill edits are excluded. Read the corresponding current files and the supplied repository and skill-writing standards.

## Hard standards violations

None found in the reviewed scope.

The skill has one distinct, human-facing responsibility, preserves read-only authority, separates implementation evidence from execution observations, and uses a self-contained workflow. Discovery remains enabled as explicitly accepted. The numbered sections have observable completion conditions without requiring a universal application architecture or an exhaustive file survey.

The two root instruction entrypoints reference shared setup documents. Their duplication is an explicit user choice, not an actionable duplication finding. Local Markdown tracking and default triage labels match that choice. The short legacy scope pointer avoids a second maintained specification.

## Heuristic smells

No actionable smells found. Scope, examples, and evaluation expectations repeat some concepts for different readers and evidence roles; this is not sufficient evidence of divergent behavioral ownership. The minimal fixture services are appropriate raw subjects for explanation and are not assessed as production applications.

## Limits

This is a read-only Standards-axis review, not a Spec-axis or runtime certification. Behavioral evaluation records were not available in the fixed snapshot and remain pending; their absence is not scored as a failure. Tooling-enforced checks were excluded as requested. Standards considered include `AGENTS.md`, `CLAUDE.md`, `docs/agents/`, collection philosophy/composition/routing, `evaluations/README.md`, and the supplied skill-creator and writing-great-skills guidance, with explicit user choices taking precedence.
