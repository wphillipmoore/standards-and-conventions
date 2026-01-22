# Agent skills

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Repository-local skills](#repository-local-skills)
- [Shared skills library](#shared-skills-library)
- [Registration and loading](#registration-and-loading)

## Purpose
Define how skills are stored, imported, and referenced so repositories avoid
external runtime dependencies while still benefiting from shared workflows.

## Scope
Applies to any repository that uses skills to guide agent behavior or
automation.

## Repository-local skills
- Store repo-specific skills under `skills/` at the repository root.
- Treat `skills/` as the source of truth for skill content used in that repo.
- If a skill is required for repo workflows, document it in `AGENTS.md`.

## Shared skills library
- The `standards-and-conventions` repository hosts shared skills under
  `skills/` as a reference library.
- To avoid external dependencies, copy shared skills into the target
  repository’s `skills/` directory before use.
- Do not rely on symlinks or external paths for required skills.

## Registration and loading
- Skills are not auto-registered by documentation alone.
- If a skill does not appear in the active skill list, restart the agent
  session after adding it.
- Repositories should assume that skill availability may require a session
  reload and document that expectation in `AGENTS.md`.
