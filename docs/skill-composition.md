# Host-neutral Skill Composition

At the first concrete signal owned by another available skill, load it through
the host's skill mechanism if it is not already in the active context. Do not
repeat an active load or copy the specialist's checklist into the caller.
A receiving agent must load instructions absent from its own context.

`vibe-project` shares one discovery map between explain, assess, and combined modes.
A mode change is not a new skill invocation or permission to modify the project.
`vibe-frontend` owns detailed frontend assessment and implementation;
`vibe-design-context` owns durable design intent. Use other specialists only where
their signals apply.

One skill's invocation never expands authorization. Assessment stays read-only;
a request for implementation defines its own scope. `vibe-frontend` records a
non-trivial implementation through the repository's existing planning convention,
or a lightweight local fallback, before editing; that record preserves scope and
does not create new authority or a redundant approval gate. `vibe-handoff` applies
only at an actual transfer to an agent consumer. The [recovery
workflow](workflows/recovery.md) coordinates existing skills for an explicitly
requested stabilization effort; an unfinished repository alone does not trigger
it.
