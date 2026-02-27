# Python Coding Standards Overview

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

See [Source Control Guidelines](../../code-management/source-control-guidelines.md#ci-gates)
for hard gate and soft gate definitions.

Required checks for Python repositories are maintained in the
[standard-actions CI gates documentation](https://wphillipmoore.github.io/standard-actions/ci-gates/required-checks/).

## Document Map

- Naming conventions: [naming-conventions.md](naming-conventions.md)
- Import-time side effects: [import-time-side-effects.md](import-time-side-effects.md)
- Type hints: [type-hints.md](type-hints.md)
- Testing and coverage: [testing-and-coverage.md](testing-and-coverage.md)
- Dependency management: [dependency-management.md](dependency-management.md)
- Local validation scripts: [local-validation-scripts.md](local-validation-scripts.md)
- Python version management: [version-management.md](version-management.md)
- Ty migration plan: [ty-migration-plan.md](ty-migration-plan.md)
