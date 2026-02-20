# Go Development Standards Overview

## Purpose

Define consistent Go standards that emphasize readability, maintainability,
and long-term survivability across repositories.

## Core Principles

- Effective Go and Go Code Review Comments compliance is the default and
  highest priority.
- Readability overrides cleverness or brevity.
- Exceptions must be explicit, documented, and justified.

## Tooling Expectations

- Formatting: gofmt (canonical, zero configuration).
- Linting: golangci-lint (aggregated linter runner).
- Static analysis: go vet (built-in, catches common mistakes).
- Vulnerability scanning: govulncheck.
- Module system: Go modules (go.mod / go.sum).
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

- `test: unit (current)`
- `test: integration`
- `ci: dependency-audit`

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
