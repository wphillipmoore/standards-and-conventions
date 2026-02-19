# Java Coding Standards Overview

## Purpose

Define consistent Java standards that emphasize readability, maintainability,
and long-term survivability across repositories.

## Core Principles

- Google Java Style Guide compliance is the default and highest priority.
- Readability overrides cleverness or brevity.
- Exceptions must be explicit, documented, and justified.

## Tooling Expectations

- Formatting: google-java-format (opinionated, zero configuration).
- Style enforcement: Checkstyle with the Google checks configuration.
- Static analysis: SpotBugs (bytecode-level bug detection) and PMD
  (source-level bug detection).
- Compiler plugin: Error Prone (catches common mistakes at compile time).
- Null safety: NullAway (Error Prone plugin, low-overhead null checks).
- Build system: project-dependent (Maven or Gradle). Document the choice and
  equivalent commands in the repository README.
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
- `integration-tests`
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
