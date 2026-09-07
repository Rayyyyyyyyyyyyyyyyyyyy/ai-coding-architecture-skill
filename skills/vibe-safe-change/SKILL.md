---
name: vibe-safe-change
description: Guard dependency, secret, trust, auth, persistent-data, runtime, destructive-action, and recovery boundaries during implementation, explicit risk review, or diagnosis of a suspected safety-boundary violation. Not for presentation-only edits.
---

# Vibe Safe Change

Preserve trust, data, compatibility, and recoverability within the authorized scope.

Load each named skill through the host mechanism; call the Skill tool when exposed. Do not reload an active skill.

## Authority

- **Implementation:** apply the active risk branch. Writing a migration, config example, or plan does not authorize production execution, secret rotation, data mutation, package installation, or external configuration.
- **Review:** report risks and mitigations; do not mutate code or systems.
- **Diagnosis:** identify the violated safety boundary; invoke `vibe-debug` only when causal investigation is required. Do not fix unless requested.

If ambiguity affects security, data, infrastructure, cost, or an external system, stop before mutation.

## Risk branch

Read only the relevant section of [references/risk-guide.md](references/risk-guide.md):

| Branch | Invariants |
| --- | --- |
| dependencies | package-manager consistency, necessity, compatibility, supply chain |
| secrets/data | trusted placement, no exposure, incident boundary |
| authn/authz/trust | server-side identity and resource authorization |
| persistence/schema | compatibility, migration order, preservation, rollback limits |
| runtime/operations | configuration, topology, cost, operational ownership |
| destructive/recovery | exact target, reversibility, stopping condition, authority |

Inspect only evidence for the active branch. Preserve established safe conventions; do not expand a focused task into a security rewrite, platform migration, or infrastructure project.

Handle routine reversible choices silently. Surface before proceeding when a choice risks exposure, data loss, weakened authz, breaking compatibility, migration, infrastructure/cost, or ambiguous security/data semantics.

After authorized implementation changes executable behavior or configuration, provide the risk-specific assertion and invoke `vibe-verify`. Review and diagnosis alone do not invoke completion verification. Report only material decisions, unresolved limits, migrations, recovery constraints, and unauthorized actions. On actual agent transfer invoke `vibe-handoff`.
