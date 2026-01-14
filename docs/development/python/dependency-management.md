# Python Dependency Management

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Sources of truth](#sources-of-truth)
- [Version specification rules](#version-specification-rules)
- [Upgrade workflow](#upgrade-workflow)
  - [Patch-level](#patch-level)
  - [Minor- or major-level](#minor--or-major-level)
- [In-cycle exception rules](#in-cycle-exception-rules)
- [Handling regressions and non-latest pins](#handling-regressions-and-non-latest-pins)
- [Anchored dependency documentation](#anchored-dependency-documentation)
- [Locked dependency review](#locked-dependency-review)
- [Enforcement](#enforcement)
- [Examples (TODO)](#examples-todo)
- [Related documents](#related-documents)

## Purpose
Define strict, repeatable rules for Python dependency management to reduce
upgrade risk while keeping dependencies current.

## Scope
These rules apply to Python library dependencies managed with `pyproject.toml`,
`poetry.lock`, and requirements exports derived from the lock file.

## Sources of truth
- `pyproject.toml` declares allowed dependency ranges.
- `poetry.lock` pins exact versions compiled from those ranges.
- Requirements files are exported from `poetry.lock` and must never drift from
  it.

## Version specification rules
- Default dependency specs in `pyproject.toml` use `*`.
- Do not anchor to a major or minor series by default (including pre-1.0
  dependencies).
- Use constrained specs only when necessary and document them using the
  anchored dependency workflow.
- Avoid patch-level pinning in `pyproject.toml` unless an explicit exception
  is approved.
- Major version upgrades are explicit, deliberate decisions and require their
  own review procedure (to be defined).

Example default specification:

```
example-lib = "*"
```

## Upgrade workflow

### Patch-level
The first action after incrementing the application `PATCH` version is to
refresh dependencies.

Workflow:
1. Increment `PATCH` per the application versioning scheme.
2. Run `poetry update` to refresh `poetry.lock` within the existing constraints.
3. Export requirements files from `poetry.lock` where required.
4. Run the full validation and test suite (define the canonical command per
   repository).
5. If validation passes, the lockfile versions remain fixed for the rest of the
   `PATCH` cycle unless an exception is approved.

Do not change explicit version constraints in `pyproject.toml` as part of this
cycle-opening update.

### Minor- or major-level
When incrementing the application `MINOR` or `MAJOR` version, perform the patch-level
workflow and also attempt to move toward the latest available dependency
releases when constraints have been tightened.

Workflow:
1. Identify dependencies pinned below the current minor series (for example,
   constrained to `1.1` when `1.2` exists).
2. For each dependency, relax the constraint individually and run the full
   validation and test suite.
3. If multiple dependencies were relaxed successfully, run the full validation
   and test suite with all relaxations combined.
4. Identify dependencies anchored to a major version when a newer major
   release exists (for example, constrained to `<4` when `5.x` is available).
5. For each major upgrade candidate, expand the constraint individually and
   run the full validation and test suite.
6. If multiple major upgrades are viable, run the full validation and test
   suite with all major upgrades combined.

The expected steady state is unconstrained (`*`) unless a documented exception
requires anchoring. If no newer major release exists, there is nothing to test.

If a dependency upgrade fails, determine root cause before deciding to pin or
defer. A regression in the dependency is a valid reason to stay on the prior
major version (for example, pinning `pylint` to the latest `3.x` when `4.0.0`
introduces a blocking bug).

## In-cycle exception rules
Dependencies may change during a `PATCH` cycle only when necessary:
- New functionality requires additional dependencies.
- A dependency bug impacts the application and requires an upgrade or pin.

Each exception must:
- include a written rationale in the pull request
- minimize the scope of the dependency change
- update `poetry.lock` and any exported requirements
- complete the full validation and test suite

## Handling regressions and non-latest pins
When a `poetry update` introduces failures:
- determine root cause before deciding to pin
- do not assume the dependency is at fault
- verify whether the application is compliant with the dependency's documented
  API and behavior

Pinning to a non-latest version is acceptable only when:
- a regression or compatibility break in the dependency is verified, and
  no fix is available within the current cycle, or
- the application depends on behavior removed or corrected upstream and a
  migration is required

If the application is at fault, fix the application and re-run the update
instead of pinning.

Every pin must be accompanied by:
- a written rationale and evidence
- a clear exit condition and planned removal
- a review at the next `PATCH` cycle

## Anchored dependency documentation
When a dependency is anchored below the latest acceptable range, document it in
two places:

1. `pyproject.toml` comment immediately above the dependency specification,
   noting the latest version that failed and pointing to the dependency record.
2. A dependency-specific record in `docs/dependencies/` that captures failure
   evidence and preserves history across attempts.

Update both records every time an upgrade is tested and fails. Do not replace or
delete prior failure evidence.

Example `pyproject.toml` comment:

```
# Anchor: 1.2.5 fails full test suite; see docs/dependencies/example-lib.md
example-lib = ">=1.1,<2.0"
```

Dependency record requirements:
- One file per dependency: `docs/dependencies/<dependency-name>.md`.
- Record the failing version and a concise description of the failure.
- Capture failure evidence (test command, error excerpt, and context).
- Append a new entry for each failed re-test.
- Keep the latest attempted version in the `pyproject.toml` comment.

See [Dependency anchor records](../../dependencies/overview.md) for the
required format.

## Locked dependency review
At the start of each upgrade cycle (`PATCH`, `MINOR`, or `MAJOR`), review any
pinned or tightly constrained dependencies and confirm each pin is still
required. Remove unnecessary pins before completing the cycle-opening update.

## Enforcement
Violations are fatal exceptions that block merges, releases, and deployments.

CI must fail when:
- `poetry.lock` is out of sync with `pyproject.toml`
- a dependency spec is constrained without documented justification
- a dependency anchor lacks the required `pyproject.toml` comment
- a dependency anchor lacks a record in `docs/dependencies/`
- dependency updates occur without the required validation run

## Examples (TODO)
- Default `*` specifications and constrained exceptions.
- Patch-cycle update checklist in practice.
- Justified pinning due to upstream regression.
- Dependency addition for new functionality.

## Related documents
- Application versioning scheme: [application-versioning-scheme.md](../../code-management/application-versioning-scheme.md)
- Pull request workflow: [pull-request-workflow.md](../../code-management/pull-request-workflow.md)
