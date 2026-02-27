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

See [Source Control Guidelines](../../code-management/source-control-guidelines.md#ci-gates)
for hard gate and soft gate definitions.

Required checks for Go repositories are maintained in the
[standard-actions CI gates documentation](https://wphillipmoore.github.io/standard-actions/ci-gates/required-checks/).

## Document Map

- Naming conventions: [naming-conventions.md](naming-conventions.md)
