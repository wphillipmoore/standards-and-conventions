# Python Coding Standards Overview

## Table of Contents
- [Purpose](#purpose)
- [Core Principles](#core-principles)
- [Tooling Expectations](#tooling-expectations)
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
- Default type checking: mypy in strict mode.
- If a repository uses different tools, document the reason and equivalents.

## Document Map
- Naming conventions: [naming-conventions.md](naming-conventions.md)
- Import-time side effects: [import-time-side-effects.md](import-time-side-effects.md)
- Type hints: [type-hints.md](type-hints.md)
- Testing and coverage: [testing-and-coverage.md](testing-and-coverage.md)
- Dependency management: [dependency-management.md](dependency-management.md)
