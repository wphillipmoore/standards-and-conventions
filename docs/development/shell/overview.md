# Shell Scripting Standards Overview

## Table of Contents

- [Purpose](#purpose)
- [Core Principles](#core-principles)
- [Tooling Expectations](#tooling-expectations)
- [CI Gates](#ci-gates)
- [Document Map](#document-map)

## Purpose

Define consistent shell scripting standards that emphasize safety,
readability, and long-term maintainability across repositories.

## Core Principles

- Defensive defaults are non-negotiable. Every script starts safe.
- Readability overrides cleverness or brevity.
- Prefer bash-specific features when they improve clarity over POSIX
  alternatives, but avoid bashisms that have no readability benefit.
- Exceptions must be explicit, documented, and justified.

## Tooling Expectations

- Shebang: `#!/usr/bin/env bash` (portable, PATH-based resolution).
- Safety header: `set -euo pipefail` required in all scripts immediately
  after the shebang. This enables exit-on-error (`-e`), undefined variable
  errors (`-u`), and pipeline failure propagation (`pipefail`).
- Linting: ShellCheck. Run with default settings unless a project documents
  specific exclusions.
- Formatting: shfmt. Run with default settings unless a project documents
  specific options.
- If a repository uses different tools, document the reason and equivalents.

## CI Gates

Every CI check is classified as a hard gate or soft gate.

Hard gate definition:

- Merge-blocking. A required status check must be configured on the target
  branch. Any failure blocks merge until a new commit passes.

Soft gate definition:

- Warning-only. The check can fail without blocking merge, but failures must be
  surfaced with rationale and follow-up tracking when applicable.

Hard gates (all are required status checks):

- `test-and-validate (current)`
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
