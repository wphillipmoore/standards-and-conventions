# Python Version Management

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Core principles](#core-principles)
- [Sources of truth](#sources-of-truth)
- [Upgrade workflow](#upgrade-workflow)
  - [Patch-level](#patch-level)
  - [Minor- or major-level](#minor--or-major-level)
  - [Minor release preview (dual-CI)](#minor-release-preview-dual-ci)
  - [Cutover criteria](#cutover-criteria)
  - [Stability tracking](#stability-tracking)
- [Host decoupling and parity](#host-decoupling-and-parity)
  - [Parity requirements](#parity-requirements)
  - [Decoupling strategies](#decoupling-strategies)
- [Enforcement](#enforcement)
- [Examples (TODO)](#examples-todo)
- [Related documents](#related-documents)

## Purpose

Define a repeatable Python version strategy that keeps runtime behavior stable
within a development cycle while enabling controlled upgrades.

## Scope

These rules apply to the Python runtime version used in development, CI, and
production deployments.

## Core principles

- Use a fixed Python patch version (`x.y.z`) for an entire development cycle.
- Align development, CI, and production runtimes to the same version.
- Evaluate Python patch upgrades at the same time as dependency upgrades.
- Treat the Python runtime as a dependency with higher upgrade cost and risk.
- Document any non-latest Python pin using the anchored dependency process.

## Sources of truth

- The canonical Python version is declared once in repository configuration.
- All other references (CI config, container image tags, tooling configs) must
  derive from the canonical value.

## Upgrade workflow

### Patch-level

During the patch-cycle dependency update:

1. Check for a newer Python patch release in the current minor series.
2. If available, update the runtime to the new patch version.
3. Run the full validation and test suite.
4. If validation passes, fix the runtime to the new patch for the remainder of
   the cycle.

If the patch upgrade fails, determine root cause before pinning. If the failure
is attributable to the runtime, anchor to the prior patch and document the
failure evidence.

### Minor- or major-level

When incrementing the application `MINOR` or `MAJOR` version:

1. Perform the patch-level workflow.
2. Evaluate whether upgrading the Python minor or major version is required or
   beneficial for the next cycle.
3. If a runtime upgrade is attempted, test each candidate version individually
   before combining with other changes.

### Minor release preview (dual-CI)

When the next Python minor series transitions from pre-release to bugfix
(stable) status:

1. At the start of the next development cycle, add the next minor version to
   the CI matrix.
2. Label CI jobs using the runtime version support policy convention:
   `bugfix-<version>`, `preview-<version>`, and (when applicable)
   `security-<version>`.
3. Keep `bugfix-<version>` jobs as the only hard gate. The
   `preview-<version>` check is advisory and must not block merges.
4. Record any failures in the preview check and track them as issues, but do
   not block PRs unless a bugfix-tier job fails.

### Cutover criteria

Promote the preview version to bugfix tier only after it has been stable in
CI for at least two full development cycles.

At the start of the next development cycle after meeting the stability
threshold:

1. Update the canonical Python version to the new minor series.
2. Make the new minor the required (hard-gate) CI runtime and relabel it as
   `bugfix-<version>`.
3. Relabel the prior bugfix minor as `security-<version>` and keep it
   advisory to preserve rollback capability.
4. Keep `security-<version>` advisory until humans explicitly decide to drop
   it. Do not auto-remove based on elapsed cycles alone.

### Stability tracking

Once dual-CI begins, record stability status at the start of each development
cycle. Capture:

- cycle start date
- bugfix-tier minor version
- preview-tier minor version (candidate for promotion)
- security-tier minor version (if retained)
- CI status summary and any open issues blocking promotion

Store the stability log in a repository-local doc (for example,
`docs/development/python/version-stability-log.md`) and keep it updated until
the cutover is complete.

## Host decoupling and parity

### Parity requirements

- Prefer running development and test workflows in an environment that matches
  the deployment operating system and runtime.
- Avoid relying on the host OS Python for anything beyond ad-hoc commands.
- Ensure CI validates the same runtime version used for development and
  production.

### Decoupling strategies

Evaluate one or more of the following approaches:

- Containerized development environments that mirror production runtime
  versions and base operating system.
- Standardized dev shells or wrapper scripts that run tests and tooling inside
  the controlled runtime.
- Remote or hosted development environments running the deployment OS.
- Toolchain managers that install and isolate Python without modifying the
  system runtime.

## Enforcement

Violations are fatal exceptions that block merges, releases, and deployments.

CI must fail when:

- The Python version drifts across development, CI, and production.
- The runtime version is modified mid-cycle without the upgrade workflow.
- A non-latest runtime pin lacks anchored dependency documentation.

## Examples (TODO)

- Patch upgrade with a runtime regression and anchor record.
- Minor or major runtime upgrade checklist.
- Containerized development workflow that matches production.

## Related documents

- Runtime version support policy:
  [runtime-version-support-policy.md](../runtime-version-support-policy.md)
- Python dependency management: [dependency-management.md](dependency-management.md)
- Dependency anchor records: [dependency anchor records](../../dependencies/overview.md)
