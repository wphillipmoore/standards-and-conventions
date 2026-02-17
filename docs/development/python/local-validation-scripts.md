# Local Validation Scripts (Python)

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [General standard](#general-standard)
- [Python-specific requirements](#python-specific-requirements)
- [CI parity](#ci-parity)
- [Version validation](#version-validation)

## Purpose

Specialize the
[ecosystem-agnostic local validation scripts standard](../../repository/local-validation-scripts.md)
for Python repositories.

## Scope

Applies to Python repositories that define a canonical local validation
command. All requirements from the
[general standard](../../repository/local-validation-scripts.md) apply in
addition to the Python-specific requirements below.

## General standard

This document extends the
[Local Validation Scripts](../../repository/local-validation-scripts.md)
standard. Refer to that document for shared requirements including fail-fast
behavior, prerequisite checks, non-zero exit codes, CI parity basics, and
no-side-effects rules.

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
