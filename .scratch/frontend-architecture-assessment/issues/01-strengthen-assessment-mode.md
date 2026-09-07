# Strengthen existing-frontend assessment mode

Status: resolved

Revise `coding-architecture` to own evidence-based architecture assessment of an
existing frontend, including responsibility concentration and justified typing
recommendations, while preserving its current implementation and scope rules.

Acceptance criteria:

- Existing-frontend architecture review is discoverable without a pending code change.
- Routing distinguishes a request to understand current architecture
  (`explain-project`) from a request to judge frontend architecture health
  (`coding-architecture`).
- Assessment covers material responsibility, state/effect, data-contract, test-seam,
  and type-safety concerns without treating file length or JavaScript alone as defects.
- Assessment may inspect adjacent producers to establish a frontend contract but
  keeps findings and recommendations within frontend architecture.
- Advice stays read-only and reports evidence, impact, and recommended scope.
- Existing JavaScript feature work does not become an incidental TypeScript migration.
- UI metadata, routing documentation, and meaningful behavioral cases agree with the skill.
- The skill passes the repository's applicable validation.

## Comments

Claimed for implementation through an actual agent handoff on 2026-09-07.

## Answer

Strengthened `coding-architecture` with a distinct, read-only existing-frontend
assessment mode. Discovery and routing now distinguish explaining how a project
works (`explain-project`) from judging whether frontend boundaries are healthy
(`coding-architecture`), including review requests with no pending change.

The assessment follows reachable frontend implementation and evaluates
responsibility/change boundaries, component/state/effect ownership, frontend
data contracts and runtime validation, type guarantees, and test seams. It
requires source evidence, a concrete impact scenario, and the smallest useful
recommended scope. Large files, colocated components, JavaScript, and missing
tests remain investigation signals rather than automatic defects. Existing
JavaScript implementation stays JavaScript unless migration is requested;
read-only assessment may recommend typing or validation only with concrete
evidence and does not authorize migration.

The skill may inspect an adjacent server, build step, worker, or producer only
to establish the frontend contract. Findings and recommendations stay within
frontend architecture. UI metadata, README guidance, routing/philosophy docs,
and coding/cross-skill evaluation cases were updated to match.

Validation evidence:

- `quick_validate.py` reported `Skill is valid!` for both `coding-architecture`
  and the routing-adjusted `explain-project` skill.
- YAML/frontmatter parsing, `git diff --check`, and relative Markdown-link checks
  passed.
- An initial isolated Winter forward check correctly rejected broad component,
  folder, and TypeScript changes, but recommended a Vite middleware mutation;
  this exposed and led to the explicit mixed-runtime scope rule.
- A second fresh, isolated Winter forward check stayed within the frontend. It
  identified the blocklist state/effect/undo contract as a material boundary,
  proposed one focused frontend hook, treated the 639-line JavaScript module as
  a signal rather than a verdict, used the manifest producer only as contract
  evidence, and made no server, Python, or TypeScript migration recommendation.

The two forward checks were informal behavior probes rather than recorded suite
runs under `evaluations/*/runs`; no browser/runtime behavior was exercised.
