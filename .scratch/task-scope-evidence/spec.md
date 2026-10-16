# Preserve task scope across assessment, diagnosis, and verification

The user reported an optimization assessment drifting into speculative debugging
and repeated repairs to newly added tests, then approved targeted skill updates.
Existing rules already constrain scope; strengthen the decision points where
derived work can lose its connection to the original outcome.

Scope: update `vibe-frontend`, `vibe-debug`, `vibe-verify`, and the shared
composition rule. Add behavioral case specifications for improvement value,
symptom and expectation provenance, verification cost reassessment, and genuine
in-scope work that should continue. Preserve existing authorization boundaries.
Do not change installed skill copies, introduce approval ceremonies, or add a
fixed retry or time budget.

Acceptance: improvement recommendations weigh observed maintenance cost and
benefit against change and verification cost; diagnostic expectations have an
independent basis; new tests do not manufacture requirements; verification
reassesses infrastructure work without weakening acceptance. Case specifications
cover both scope drift and legitimate work. Run skill metadata validation and
diff checks; distinguish authored cases from executed behavioral evaluations.
No browser checks are authorized.

Follow-up: the user approved consolidating repeated instructions in the three
skill entrypoints. Preserve their routing, authority, evidence, and stopping
conditions while reducing wording. Keep behavioral cases separate and unchanged;
review their requirements against the condensed instructions, validate metadata,
and report before/after word counts without claiming behavioral runs occurred.

Publication follow-up: the user explicitly requested updating global installs
and pushing the changes. This supersedes the earlier installed-copy exclusion.
Use the existing Git commit versioning convention (no version file or release
tags are configured), push the completed work to `origin/main`, and refresh the
existing Codex and Claude Code global copies from that source. Back up installed
files and verify their contents against the published repository. Browser checks
remain unauthorized.
