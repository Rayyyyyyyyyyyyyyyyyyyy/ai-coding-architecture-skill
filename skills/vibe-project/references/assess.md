# Assess Project Architecture

Read this reference for assessment-only or combined explain-and-assess requests.
Use the map, traces, authority rules, and specialist ownership in [Project](../SKILL.md).


## Assess material boundaries

Use concrete repository signals to examine:

- **Ownership and dependency direction:** where a responsibility or policy is
  decided, whether consumers bypass its owner, and whether dependency cycles or
  shared internals force unrelated units to change together.
- **Authoritative state and data:** which unit owns the canonical value, where it
  changes and persists, how caches or replicas synchronize, and whether two
  writable representations can disagree without a defined reconciliation path.
- **Interfaces and contracts:** whether public APIs, events, schemas, files,
  commands, or configuration make the real contract explicit enough for
  producers and consumers to evolve without coordinated guesswork.
- **Runtime and external boundaries:** whether process, trust, deployment, or
  provider boundaries match the code's assumptions, and whether configuration
  and operational ownership are clear at those boundaries.
- **Failure and recovery:** what happens after partial success, timeout, retry,
  restart, duplicate delivery, or an unavailable dependency; identify any
  architectural coupling that prevents safe recovery or leaves state ambiguous.
- **Change locality:** use a realistic product or operational change to test
  whether one rule can be changed at its owner or must be repeated across
  unrelated units. Count coordinated edits only after confirming they implement
  the same decision.
- **Test seams:** determine whether consequential policies and contracts can be
  checked at their owning boundary and whether cross-unit assumptions have
  meaningful contract or integration evidence. Missing tests alone are not an
  architecture finding.

Directory shape, file length, language choice, framework preference, number of
services, unfamiliar patterns, duplicated-looking syntax, and missing tests are
investigation signals. Report them only when the traced implementation shows a
concrete consequence. Do not prescribe layers, microservices, TypeScript, a
folder tree, or another preferred style as a universal target.

## Report findings

Lead with the material findings, ordered by impact. Each finding must include:

- source evidence for the implemented connection or missing boundary;
- a concrete failure, recovery, or change scenario and its consequence;
- affected users, execution units, data, or operational responsibility;
- confidence, separating observed behavior from static inference;
- the smallest proportionate recommendation and the boundary that should own it.

Do not inflate a plausible smell into a finding when its consequence is
hypothetical or contradicted by repository evidence. Say when an inspected
boundary appears coherent and when no material problem was found. Finish with
the inspected execution units, material omissions, and runtime or deployment
limits so the conclusion cannot be mistaken for broader evidence.
