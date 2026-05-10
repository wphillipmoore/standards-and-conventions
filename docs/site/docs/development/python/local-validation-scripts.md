# Local Validation Scripts (Python)

## Purpose

Define local validation script requirements for Python repositories.

## Scope

Applies to Python repositories that define a canonical local validation
command.

## Python-specific requirements

- Provide a canonical local validation command at `scripts/dev/validate_local.py`.
- Invoke Python as `python3` and use the project environment.

## CI parity

In addition to the general CI parity requirements, Python validation scripts
must include:

- linting and type checking with all required checkers (including mypy and ty
  when configured)

## Version validation

If CI enforces version comparison against a base branch, the local script must
support passing a base reference (for example, `--base-ref develop`) and must
document the default behavior (for example, resolving `origin/HEAD`).
