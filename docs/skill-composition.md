# Host-neutral Skill Composition

Cross-skill composition is an action, not a prose reminder. At the first
concrete signal owned by another installed skill, invoke that skill through the
host's skill-loading mechanism when it is not already loaded in the active
model context. Do not reload it at each later mention or copy its checklist into
the consuming skill. A later turn or receiving agent must load it again when
its context does not contain the skill.

The mechanism is host-specific: use the host operation that loads the named
skill; when a Skill tool exists, call it. The behavior is not host-specific. A
skill must not be invoked without its trigger merely to run the whole collection,
and one skill's invocation never expands the user's authorization.

`a2a-handoff` is invoked only at an actual agent-consumer transfer event.
`rescue-vibe-project` is never composed implicitly; only the user may invoke it.
