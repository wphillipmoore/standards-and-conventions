# Dependency update workflow

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Sources of truth](#sources-of-truth)
- [Workflow](#workflow)
- [Failure handling](#failure-handling)
- [Release-cycle review](#release-cycle-review)
- [Related documents](#related-documents)

## Purpose

Define a repeatable, cross-ecosystem workflow for dependency updates that
prioritizes stability, security, and auditability.

## Scope

These rules apply to all dependencies, including application libraries,
build tooling, CI/CD workflows, and deployment automation.

## Sources of truth

Update dependencies at their source of truth:

- language or platform manifests and lockfiles
- CI/CD workflow definitions
- dependency inventory or configuration files

Regenerate any derived artifacts after updates.

## Workflow

1. Collect update signals from:
   - dependency security alerts (for example, GitHub Security/Dependabot)
   - audit tooling (for example, language-specific vulnerability scanners)
   - planned upgrades tied to release planning
2. Update dependencies at their source of truth.
3. Regenerate derived artifacts.
4. Run the full validation and test suite.
5. Proceed through the standard pull request workflow.

## Failure handling

If an attempted upgrade fails:

1. Determine root cause before pinning.
2. If the dependency itself is the blocker, create a tracking issue.
3. Pin the dependency to the last known good version and document the pin at
   the source of truth with a comment referencing the issue.
4. Update any required anchor records or dependency history documentation.

## Release-cycle review

For MAJOR and MINOR release cycles, review dependency security alerts and
incorporate remediation into the dependency update process.

## Related documents

- Python dependency management: [dependency-management.md](../development/python/dependency-management.md)
- Dependency anchor records: [overview.md](overview.md)
- Pull request workflow: [pull-request-workflow.md](../code-management/pull-request-workflow.md)
