# Consolidate and rename skills

Status: resolved

Implement the eight short names and project modes described in ../spec.md.
Validate discovery names, metadata, local links, mode selection, and scope.
Keep old evaluation executions unchanged; document their historical names.

## Comments

- Implementing the user-approved short-name proposal and consolidation.

## Answer

Renamed the six specialist directories, frontmatter names, display names,
invocation prompts, references, and current evaluation suites. `safe-change`
retains its name. Combined explanation and system architecture assessment in
`project`, using shared discovery and an assessment-only reference. Moved rescue
coordination into `docs/workflows/recovery.md` and adapted its case suite to the
documented workflow. There are eight discoverable skill directories and no old
name aliases.

README now provides intent-based navigation, short invocation examples, an old
to new name table, and installation/history limits. Routing, composition,
philosophy, current evaluation indexes/cases, and old research links align.
Historical execution snapshots and fixtures remain byte-for-byte unchanged.

Validation:

- All eight skills pass `quick_validate.py`.
- Parsed frontmatter/metadata agree with all eight directory names and `$name`
  invocation prompts.
- Current relative Markdown links resolve and `git diff --check` passes.
- Manual mode review caught and corrected a conflicting explanation-first output
  rule for assessment-only requests.
- Added combined-mode, follow-up evidence reuse, and requested-report cases;
  these specifications were not executed as new behavioral evaluation runs.

No global installed copies were changed and no commit was created.
