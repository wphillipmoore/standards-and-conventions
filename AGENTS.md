# Standards and Conventions - Agent Instructions

## User Overrides (Optional)

Always apply this repository's `AGENTS.md` as the baseline. If
`~/AGENTS.md` exists and is readable, load it after and apply it as an
additive, user-specific overlay. The user-specific overlay may add
constraints but must not replace or weaken the repository instructions.
If it cannot be read, say so briefly and continue.

This repository is the canonical source of development standards and
conventions. Treat the documents here as the default baseline for other
repositories, with local overrides captured elsewhere when needed.

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

Branch naming and rules are defined in `docs/site/docs/code-management/branching/branching-and-deployment.md`.

## Before You Act: Consult Documentation First

This repository is documentation-first. All required workflow rules are in the
standards. Always read the relevant documents before acting.

If a required canonical standard cannot be retrieved, treat it as a fatal
exception: stop and notify the user. Do not proceed with assumptions or
alternate sources.

### Required Reading Before Common Operations

#### Git Operations (commit, push, branch, merge)

- MUST READ: `docs/site/docs/code-management/branching/branching-and-deployment.md`

#### Documentation Standards

- MUST READ: `docs/site/docs/standards/markdown-standards.md`

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

- Core standards live under `docs/site/docs/`.
- Follow `docs/site/docs/standards/markdown-standards.md` when adding
  documentation.

## Shell command policy

**Do NOT use heredocs** (`<<EOF` / `<<'EOF'`) for multi-line arguments to CLI
tools such as `gh`, `git commit`, or `curl`. Heredocs routinely fail due to
shell escaping issues with apostrophes, backticks, and special characters.
Always write multi-line content to a temporary file and pass it via `--body-file`
or `--file` instead.

## The RTFM Principle

If you find yourself guessing at workflow rules, using trial-and-error, or
backtracking due to errors, stop and read the relevant documentation before
proceeding.
