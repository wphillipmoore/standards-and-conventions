# Python Coding Standards Overview

## Table of Contents
- [Purpose](#purpose)
- [Core Principles](#core-principles)
- [Tooling Expectations](#tooling-expectations)
- [CI Gates](#ci-gates)
- [Document Map](#document-map)

## Purpose
Define consistent Python standards that emphasize readability, maintainability,
and long-term survivability across repositories.

## Core Principles
- PEP compliance is the default and highest priority.
- Readability overrides cleverness or brevity.
- Exceptions must be explicit, documented, and justified.

## Tooling Expectations
- Default linting: ruff.
- Default type checking: mypy in strict mode and ty with default settings.
- Mypy remains authoritative until ty cutover is explicitly approved.
- If a repository uses different tools, document the reason and equivalents.
- Invoke Python as `python3` and use a project-specific environment for all
  Python commands. See `docs/development/environment-and-tooling.md`.

## CI Gates
Every CI check is classified as a hard gate or soft gate.

Hard gate definition:
- Merge-blocking. A required status check must be configured on the target
  branch. Any failure blocks merge until a new commit passes.

Soft gate definition:
- Warning-only. The check can fail without blocking merge, but failures must be
  surfaced with rationale and follow-up tracking when applicable.

Hard gates (all are required status checks):
- `test-and-validate (3.14)`
- `integration-tests`
- `dependency-audit`

Soft gates:
- None (default to hard gate until documented).

Branch applicability:
- develop: all hard gates required
- release: all hard gates required
- main: all hard gates required

Docs-only pull requests may skip these jobs when the repository implements the
docs-only CI skip policy.

## Document Map
- Naming conventions: [naming-conventions.md](naming-conventions.md)
- Import-time side effects: [import-time-side-effects.md](import-time-side-effects.md)
- Type hints: [type-hints.md](type-hints.md)
- Testing and coverage: [testing-and-coverage.md](testing-and-coverage.md)
- Dependency management: [dependency-management.md](dependency-management.md)
- Local validation scripts: [local-validation-scripts.md](local-validation-scripts.md)
- Python version management: [version-management.md](version-management.md)
- Ty migration plan: [ty-migration-plan.md](ty-migration-plan.md)
