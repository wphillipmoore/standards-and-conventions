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

See [Source Control Guidelines](../../code-management/source-control-guidelines.md#ci-gates)
for hard gate and soft gate definitions.

Required checks for Java repositories are maintained in the
[standard-actions CI gates documentation](https://wphillipmoore.github.io/standard-actions/ci-gates/required-checks/).

## Document Map

- Naming conventions: [naming-conventions.md](naming-conventions.md)
