# Local validation scripts

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Requirements](#requirements)
- [CI parity](#ci-parity)
- [Version validation](#version-validation)
- [Failure behavior and output](#failure-behavior-and-output)

## Purpose
Define the required behavior for repository-local validation scripts (for
example, `scripts/dev/validate_local.py`) so local checks reliably match CI
hard gates.

## Scope
Applies to Python repositories that define a canonical local validation
command. Repositories that do not define such a command must document their
alternative process in the pull request workflow.

## Requirements
- Provide a canonical local validation command at `scripts/dev/validate_local.py`.
- Run from the repository root and fail fast if executed elsewhere.
- Invoke Python as `python3` and use the project environment.
- Execute all CI hard-gate checks locally with the same tools and flags.
- Permit additional local-only checks when documented, but never omit CI hard
  gates.
- Avoid side effects beyond validation (no automatic fixes or rewrites).
- Return a non-zero exit code on failure.

## CI parity
The local validation script must mirror CI hard gates, including:
- dependency and lockfile validation
- linting and type checking
- tests with the same marker selection and coverage thresholds
- security or dependency audits required by CI

If CI separates unit and integration jobs, the local script must run both sets
of tests to keep coverage and integration behavior aligned.

## Version validation
If CI enforces version comparison against a base branch, the local script must
support passing a base reference (for example, `--base-ref develop`) and must
document the default behavior (for example, resolving `origin/HEAD`).

## Failure behavior and output
- Print the command being executed before each step.
- Stop at the first failing command and return that exit code.
- Surface missing prerequisites with actionable error messages.
