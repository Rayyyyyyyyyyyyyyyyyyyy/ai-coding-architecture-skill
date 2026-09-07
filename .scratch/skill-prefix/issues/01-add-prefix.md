# Add collection prefix

Status: resolved

Implement the `vibe-` collection identifier for all eight skill entry points.
Check names, metadata, default prompts, active links, and historical snapshots.

## Comments

- User requested an identifying prefix; selected `vibe-` to match the collection title.

## Answer

All eight skills now use `vibe-` in their directories, frontmatter, display
names, and default invocation prompts. Current evaluation suites, cross-skill
references, routing, recovery workflow, and README use the same names. README
includes the old short and long names for migration. Historical execution
snapshots and fixtures remain unchanged; global installed copies were not edited.

All eight skills pass quick validation. Parsed YAML confirms directory/name/
prompt consistency, current relative Markdown links resolve, and the active
reference scan contains no unprefixed invocations. `git diff --check` passes.
This is a naming change; no new behavioral runs were performed. No commit made.
