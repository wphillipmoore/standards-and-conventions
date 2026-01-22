# Standards and Conventions - Agent Instructions

#include docs/standards-and-conventions.md
#include docs/repository-standards.md

## User Overrides (Optional)

Always apply this repository's `AGENTS.md` as the baseline. If
`~/AGENTS.md` exists and is readable, load it after and apply it as an
additive, user-specific overlay. The user-specific overlay may add
constraints but must not replace or weaken the repository instructions.
If it cannot be read, say so briefly and continue.

This repository is the canonical source of development standards and
conventions. Treat the documents here as the default baseline for other
repositories, with local overrides captured elsewhere when needed.

## Mandatory standards intake (before any other action)

After reading this file and any `~/AGENTS.md` overlay, you MUST load the
repository-local `docs/standards-and-conventions.md`. Treat it as the required
entry point for all other standards. If the file cannot be retrieved, stop and
notify the user.

Then, before any other action, you MUST open every canonical or required
reference listed there that is relevant to the task at hand. Do not proceed
until those documents are loaded.

## Start Every Work Session: Create a Feature Branch

**Critical first step after mandatory standards intake**: before making any
changes in a new session, you MUST:

1. Check current branch: `git branch --show-current`
2. If on an eternal branch (`develop`, `release`, `main`), create a feature
   branch immediately:
   ```bash
   git checkout -b feature/<descriptive-name>
   ```
3. If already on a short-lived branch, continue work there.

**Guardrail**: re-check the branch before any edit or commit. If you are on an
eternal branch, stop and create a feature branch before touching files.

Branch naming and rules are defined in `docs/code-management/branching-and-deployment.md`.

## Before You Act: Consult Documentation First

This repository is documentation-first. All required workflow rules are in the
standards. Always read the relevant documents before acting.

If a required canonical standard cannot be retrieved, treat it as a fatal
exception: stop and notify the user. Do not proceed with assumptions or
alternate sources.

### Required Reading Before Common Operations

**Git Operations (commit, push, branch, merge)**
- MUST READ: `docs/code-management/branching-and-deployment.md`
- MUST READ: `docs/code-management/commit-messages-and-authorship.md`
- MUST READ: `docs/standards-and-conventions.md` for approved AI co-author IDs

**Pull Request Operations (create, submit, merge)**
- MUST READ: `docs/code-management/pull-request-workflow.md`

**Documentation Standards**
- MUST READ: `docs/foundation/markdown-standards.md`

## Working Rules
- Read the relevant standards before editing or adding documentation.
- Keep guidance generic; remove project-specific names, paths, or tooling.
- Preserve intent and rationale when generalizing standards.
- Update or create Tables of Contents per the Markdown standards.
- Prefer small, focused edits that keep documents easy to scan.

## Documentation First
This repo is documentation-first. Do not add code unless it is an example
explicitly required to explain a standard.

## File Layout
- Core standards live under `docs/`.
- Follow `docs/foundation/markdown-standards.md` when adding documentation.

## Multi-Line Messages
When creating multi-line commit messages or pull request bodies, prefer using
temporary files instead of shell heredocs in command substitution. This avoids
shell escaping issues and preserves exact formatting.

## The RTFM Principle
If you find yourself guessing at workflow rules, using trial-and-error, or
backtracking due to errors, stop and read the relevant documentation before
proceeding.

## User Confirmation Checkpoints

**Docs-only exception**: If the diff includes only documentation files (anything
under `docs/` plus top-level `README.md` or `CHANGELOG.md`), skip both
confirmation checkpoints and proceed directly through PR creation and
finalization. Local validation is optional per the docs-only rule in
`docs/code-management/pull-request-workflow.md`.

**Finalize override**: If the user explicitly says "Finalize PR", treat that as
approval to submit and finalize the PR for the current work without asking for
"Submit PR?" or "Finalize PR?" again. This permission expires as soon as new
work is performed (any new commit or file modification).

### Checkpoint: Before Submitting Pull Request

After completing work and committing to your feature branch:
1. Run the repository's canonical validation command if it is documented.
2. If no command is documented, ask the user for the required validation.
3. Ask: "Submit PR?"

Only proceed with PR submission after explicit user approval (or the Finalize
override above).

### Checkpoint: Before Finalizing Pull Request

After submitting the PR, ask: "Finalize PR?" unless the Finalize override is
active.

"Finalize" means: merge the PR, delete the remote branch, update the local
copy of the target branch, and run final validation (skip for docs-only).
