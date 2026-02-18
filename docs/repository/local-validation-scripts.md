# Local Validation Scripts

## Purpose

Define the required behavior for a canonical validation script that runs all
CI hard-gate checks locally as a single command. This prevents agents and
developers from cherry-picking individual validation commands and silently
skipping checks when tools are missing.

## Scope

Applies to all repositories that define a `canonical_local_validation_command`
in their repository profile. Repositories that do not define such a command
must document their alternative process in the pull request workflow.

## Requirements

- Provide a canonical validation script (for example,
  `scripts/dev/validate_local.py` or `scripts/validate.sh`). The path must
  match the `canonical_local_validation_command` in the repository profile.
- Check tool prerequisites before running any checks. Verify all required
  tools are on PATH and exit with a clear, actionable error if any are missing.
- Run from the repository root.
- Execute all CI hard-gate checks locally with the same tools and flags.
- Permit additional local-only checks when documented, but never omit CI hard
  gates.
- Print the command being executed before each step.
- Stop at the first failing command and return that exit code (fail-fast).
- Return a non-zero exit code on any failure.
- Avoid side effects beyond validation (no automatic fixes or rewrites).

## CI parity

The local validation script must mirror CI hard gates, including:

- dependency and lockfile validation
- linting and formatting checks
- type checking (when applicable)
- tests with the same marker selection and coverage thresholds
- security or dependency audits required by CI

If CI separates unit and integration jobs, the local script must run both sets
of tests to keep coverage and integration behavior aligned.

## Per-ecosystem examples

### Python

```bash
# Typical checks in a Python validation script
ruff check .
ruff format --check .
mypy src/
pytest tests/ --cov=src --cov-fail-under=90
pip-audit
```

### Go

```bash
# Typical checks in a Go validation script
go vet ./...
staticcheck ./...
go test -race -coverprofile=coverage.out ./...
govulncheck ./...
```

### Java

```bash
# Typical checks in a Java validation script
mvn checkstyle:check
mvn spotbugs:check
mvn test
mvn dependency-check:check
```

## Ecosystem-specific standards

Ecosystems may define specializations that extend this standard with
language-specific requirements:

- Python: [local-validation-scripts.md](../development/python/local-validation-scripts.md)
