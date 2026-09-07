# Project notes

Use the existing DOM conventions for UI changes.

## Architecture note from the initial plan

The task form sends new items to `/api/tasks` through `task-client.js`.
The server persists tasks so they survive browser reloads.
