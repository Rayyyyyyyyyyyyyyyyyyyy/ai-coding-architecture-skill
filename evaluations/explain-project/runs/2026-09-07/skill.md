---
name: explain-project
description: Explain an existing project's architecture, data flow, and current implementation to a human in plain language. Use for repository walkthroughs or questions about how its parts and data fit together, including partially built projects. Not for repair, refactoring, or maintaining architecture records.
---

# Explain Project

Give the user a working understanding of the current project, grounded in reachable implementation.

## Scope and authority

Use the current working tree, including relevant uncommitted changes. Read and follow applicable repository instructions; treat architectural claims in those documents as evidence of intent to corroborate, not the explanation to hand the user.

Keep the walkthrough read-only. Report gaps without fixing code, changing configuration, installing packages, creating tickets, or synchronizing architecture records. If the user asks to save the explanation, write only the requested human-facing artifact. Existing safe read-only runtime observations can add evidence; environment changes and external side effects need to be within the user's authorized scope. Do not expose secret values while explaining configuration or boundaries.

## 1. Establish the map

Start from workspace configuration, executable entry points, route or command registration, and storage and integration setup. Identify the main applications or processes, who uses them, and what each owns. Dependencies and directory names are discovery clues, not proof of active use.

For a whole-repository request, account for each major execution unit before zooming into representative flows; label any uninspected unit. For a focused question, map only the relevant boundaries. Adapt to the actual project, including frontend-only applications, CLIs, libraries, and background processing.

This step is complete when you can explain the project's purpose, major responsibilities, and the scope of this walkthrough without relying on a directory listing.

## 2. Trace representative flows

Choose a small set of real user actions or other inputs that covers the important distinct paths. Follow the registered entry point through its actual callers, transformations, authoritative decisions, data reads or writes, and observable output. Include a background or event-driven path when it is central to the product. Describe only boundaries present in the implementation.

For important data, determine where it comes from, who owns the authoritative value, where it changes, where it is stored, how long it survives, and whether it leaves the system. Distinguish view state, caches, and durable storage. Follow data back to the visible result or consumer, including polling, subscription, or a missing return path where relevant.

Use registration and framework conventions to resolve indirect calls. A missing text-search match alone does not establish dead or disconnected code. Stop a trace at an inaccessible boundary and describe what remains unknown rather than inventing the next step.

This step is complete when the selected inputs can be traced to their outcomes or concrete gaps, with source evidence for the consequential connections.

## 3. Establish the current state

Keep two questions separate:

- **What is wired?** Reachable implementation, mock data, implementation without a confirmed entry point, documented plans, or insufficient evidence.
- **What was observed?** Behavior exercised in a named environment, existing test or log evidence, or static inference that was not run during this walkthrough.

Check active adapters, flags, callers, and relevant working-tree changes when these affect the answer. If docs and code disagree, explain the current path and the differing intent without repairing either. Phrase unconfirmed reachability as “not found in the inspected scope.” A schema or migration file describes repository intent; it does not prove a deployed database has that schema. A service implementation does not prove the product uses it.

Missing credentials or an unavailable runtime still allow a bounded static explanation. This step is complete when material gaps and evidence limits are clear enough to avoid presenting intended or untested behavior as working functionality.

## 4. Explain to the user

Use the user's language and product vocabulary. Lead with a short account of what the project does and how its main parts cooperate. Then walk through the selected actions as concrete cause and effect: what happens when the user acts, where the data goes, and how the result comes back. Explain a technical term only when it helps answer the user's question.

Attach a few source links to important claims as optional evidence. Use a small labeled diagram only when it clarifies a relationship; its nodes and arrows must describe the inspected project. Keep filenames and engineering terminology subordinate to the explanation.

Finish with the meaningful unfinished connections, execution limits, and uninspected scope. Deliver the first walkthrough once the map, representative flows, data ownership, and limits are understandable; do not exhaust every file or produce a code-smell catalog. Answer follow-up questions by deepening the relevant path and rechecking changed evidence, rather than restarting the full survey.

The outcome is a human explanation, not a repair or whole-repository health claim. `architecture-context` owns durable design intent; a later request to change the project supplies its own scope and applicable workflow.
