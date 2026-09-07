# Editor state ownership

The persisted document owns content shared across collaborators. Selection belongs to the local editor session: two people can inspect different blocks without changing each other's cursor or creating a content revision. Saves include only the document. Reloading intentionally clears the local selection.

This record describes the current boundary; it does not record when the decision was made or whether earlier implementations used another model.
