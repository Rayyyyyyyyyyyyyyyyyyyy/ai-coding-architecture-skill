# Validation — 2026-09-07

## Method

Two independent subagents started without conversation history. Each received the corresponding revised skill path, a fixture path, and the user request below. They could read only the fixture and necessary skill references, could not edit files, and did not receive evaluation cases or expected findings. These are post-change behavioral probes, not a controlled before/after comparison or browser interaction tests.

## Consistent design inquiry

Agent: `/root/probe_design_inquiry`

Skill: `skills/vibe-design-context/SKILL.md`

Fixture: `evaluations/vibe-design-context/fixtures/consistent-intent`

Request: “Why is selection kept outside the persisted document? Explain the reasoning from this repository.”

Observed response: explained that local selection lets collaborators inspect different blocks without moving another person's cursor or creating content revisions. Cited ARCHITECTURE.md and corroborated it with local selection storage and document-only serialization in editor.js. Explicitly said the repository did not establish decision history.

Verdict: passed. The agent answered the direct question despite consistent code and documentation, grounded its reasoning, and did not invent history.

## Existing dialog assessment

Agent: `/root/probe_existing_dialog`

Skill: `skills/vibe-ux/SKILL.md`

Fixture: `evaluations/vibe-ux/fixtures/existing-dialog`

Request: “Review the existing preferences dialog and tell me which user-experience states or interactions are missing. Do not implement changes.”

Observed response: identified missing named dialog semantics, opening/return focus, Escape dismissal, and fixed-width overflow against the documented 320px support. Distinguished conditional modal containment from established behavior. Proposed bounded fixes; did not invent async, retry, or persistence requirements. Explicitly described the result as source inspection without browser interaction.

Verdict: passed. Existing controls and viewport requirements selected the relevant assessment without a diff.

## Mechanical checks

- All three affected skills passed skill-creator's quick_validate.py.
- Current Markdown links under skills, docs, evaluation cases, and README resolved.
- No remaining code-literal SKILL.md or reference Markdown paths were found under skills; the repaired safety pointer is now a checked Markdown link.
- git diff --check passed.
- Both fixture directories retained exactly their original files and SHA-256 hashes after the probes.

Pre-probe fixture hashes:

```text
cfd2a22e96dd2efb3647f58f025745efa001b06692e7b318065e269f44efe4a5  consistent-intent/ARCHITECTURE.md
f3a455757dfba9e31dd6a4c89afdaf61d8abece25ac795f21f796a4d3292760f  consistent-intent/editor.js
9a5eb01b2799c52b30258d1540c073181c30dae7a3078b424bb45bff0be3e135  existing-dialog/README.md
2d9b1341b4e53c382e79cae834affa7bb2d8997e4934073672475ae8f256c2b2  existing-dialog/index.html
```

Scope: repository source only; global installed skills were not synchronized.
