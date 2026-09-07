# Project architecture assessment

Add a discoverable, read-only skill for assessing an existing repository's
system architecture across its major execution units and data or integration
boundaries.

The skill should answer requests such as “where does this repository's
architecture have problems?” It must establish enough of the implemented map to
judge ownership, dependency direction, authoritative state and data, public
interfaces, runtime and external boundaries, failure/recovery behavior, change
locality, and test seams. Findings require repository evidence, a concrete
failure or change-cost scenario, impact, confidence, and proportionate
recommended scope. Directory shape, file length, language choice, unfamiliar
patterns, or missing tests are investigation signals rather than findings.

Keep this ownership distinct from:

- `explain-project`, which explains how the current project works;
- `coding-architecture`, which owns detailed frontend structure and frontend
  implementation decisions;
- `architecture-context`, which recovers and preserves durable design intent;
- specialist safety, debugging, experience, and verification skills.

For a whole-repository assessment, account for every major execution unit or
label it uninspected. Do not claim whole-repository health from one representative
slice, produce a generic code-smell catalog, edit code, create tickets, or turn
recommendations into implementation without a later request.

Update discovery metadata, routing and user documentation, collection counts,
and behavioral/cross-skill cases. Validate the new skill and links.
