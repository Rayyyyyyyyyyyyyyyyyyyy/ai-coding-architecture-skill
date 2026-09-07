# Add project architecture assessment skill

Status: resolved

Create a repo-wide architecture assessment skill with clear ownership and
evidence standards, then align collection routing, documentation, metadata, and
behavioral cases.

Acceptance criteria:

- Requests to identify architectural problems in an existing repository can
  discover the skill without a pending implementation request.
- The assessment covers cross-unit ownership, dependency, state/data authority,
  interface, runtime/external, recovery, locality, and test-seam concerns.
- Findings contain source evidence, a concrete consequence, impact/confidence,
  and a proportionate recommendation.
- Superficial signals do not become automatic findings.
- Whole-repository conclusions account for all major execution units and state
  explicit inspection limits.
- Ownership remains distinct from frontend detail, explanation, architecture
  records, safety, debugging, experience completeness, and verification.
- Advice remains read-only.
- Metadata, routing, user docs, collection counts, and meaningful behavioral
  cases agree with the new skill and validation passes.

## Comments

- 2026-09-07: Claimed by `/root/add_project_architecture_assessment` for implementation.

## Answer

Added the discoverable, implicitly invokable `assess-project-architecture`
skill. It performs read-only, evidence-based assessment across the repository's
implemented execution units and boundaries. A whole-repository review must
account for each major execution unit or label it uninspected; focused reviews
remain bounded and cannot become a repository-wide health claim.

The skill evaluates ownership and dependency direction, authoritative state and
data, interfaces and contracts, runtime and external boundaries, failure and
recovery, change locality, and test seams. Each material finding requires source
evidence, a concrete consequence, affected scope, confidence, and the smallest
proportionate owning-boundary recommendation. Directory shape, file length,
language or framework choice, service count, unfamiliar organization, and
missing tests remain investigation signals until traced evidence establishes an
impact.

Ownership and routing now distinguish:

- `explain-project` for a human walkthrough of current wiring;
- `assess-project-architecture` for cross-unit or whole-repository architecture
  health;
- `coding-architecture` for detailed frontend architecture assessment and
  implementation;
- `architecture-context` for durable intent, with safety, debugging, journey,
  verification, and handoff concerns retained by their specialist skills.

README counts and descriptions, philosophy, routing, composition, OpenAI UI
metadata, the evaluation suite index, four skill-specific behavioral cases, and
two cross-skill routing cases were updated to match.

Validation evidence:

- `quick_validate.py` reported `Skill is valid!` for
  `assess-project-architecture`, `coding-architecture`, and `explain-project`.
- All 20 `SKILL.md` frontmatter and `agents/openai.yaml` documents parsed as
  YAML.
- `git diff --check`, relative Markdown-link resolution, and the expected count
  of 10 skill directories passed.
- A collection-wide quick-validation loop reached and passed the first seven
  skills, then stopped on the pre-existing `disable-model-invocation` key in
  `rescue-vibe-project`, which this validator version does not allow. That skill
  and key were outside this issue and unchanged.
- A fresh independent Winter forward assessment used only the completed skill
  and repository path. It accounted for the React client, Vite development and
  build paths, Python ingestion and synchronization commands, Git operations,
  CI, Netlify configuration, storage state, and tests. It produced six ordered
  findings with source evidence, concrete failure or change-cost scenarios,
  confidence, proportionate scope, coherent-boundary counterevidence, and clear
  runtime/external limits. It kept the repository read-only and did not reduce
  the review to the large JSX file or language choice.

The behavioral files are case specifications, not recorded executions. The
Winter forward assessment was an informal behavior probe and was not preserved
as an `evaluations/*/runs` record; production and external integrations were not
exercised.
