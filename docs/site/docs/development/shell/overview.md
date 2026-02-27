# Shell Scripting Standards Overview

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

See [Source Control Guidelines](../../code-management/source-control-guidelines.md#ci-gates)
for hard gate and soft gate definitions.

Required checks for shell/infrastructure repositories are maintained in the
[standard-actions CI gates documentation](https://wphillipmoore.github.io/standard-actions/ci-gates/required-checks/).

## Document Map

- Naming conventions: [naming-conventions.md](naming-conventions.md)
