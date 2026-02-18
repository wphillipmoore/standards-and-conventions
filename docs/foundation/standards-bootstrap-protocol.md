# Standards bootstrap protocol

## Purpose

Provide a deterministic, AGENTS-only startup procedure for loading standards
and establishing the minimum working context before any action.

## Scope

Use at session start, when switching repositories, or when the user explicitly
requests a re-bootstrap. Do not re-run bootstrap automatically after context
compaction.

## Inputs

- Repository `AGENTS.md` (required).
- User overlay `~/AGENTS.md` (optional).
- Repository `docs/standards-and-conventions.md` (required).
- Every referenced include file listed in the standards entry point (required).

Bootstrap must be manual. Do not write or run scripts or tools to resolve
include chains.

## Protocol

1. Confirm the repository root and target.
2. Read the repository `AGENTS.md` in full.
3. If `~/AGENTS.md` exists, read it immediately after the repository
   `AGENTS.md`. If it does not exist, state that briefly and continue.
4. Open the repository `docs/standards-and-conventions.md`.
5. Traverse the include list in order. For each `<!-- include: path -->`, open
   the file directly and read it in full. If any file is missing, stop and
   notify the user.
6. For the task at hand, open every required reference listed under
   "Required Reading Before Common Operations" before acting.
7. Extract the repository profile and validation policy from
   `docs/repository-standards.md`.

## Required output

Before any edits or commands, record a short "standards snapshot" that states:

- repository_type
- branching_model
- docs-only scope or exception
- validation policy (required vs optional, plus canonical command if defined)

If any item is unknown or missing, stop and ask for clarification.

## Failure modes

Stop and notify the user when:

- `AGENTS.md` or `docs/standards-and-conventions.md` is missing.
- Any include target is missing or cannot be read.
- The repository profile is incomplete or contains placeholders.
- Required references for the task have not been read.

## Maintenance

Update this protocol whenever bootstrap rules or required references change.
