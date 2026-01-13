# Python Dependency Management

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Sources of truth](#sources-of-truth)
- [Version specification rules](#version-specification-rules)
- [Patch-cycle upgrade workflow](#patch-cycle-upgrade-workflow)
- [In-cycle exception rules](#in-cycle-exception-rules)
- [Handling regressions and non-latest pins](#handling-regressions-and-non-latest-pins)
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
- Use the least restrictive spec that still anchors to the current major
  version of each dependency.
- Do not use `*` as a default constraint.
- Avoid patch-level pinning in `pyproject.toml` unless an explicit exception
  is approved.
- For pre-1.0 dependencies, treat minor versions as breaking and constrain to
  the current minor series.
- Major version upgrades are explicit, deliberate decisions and require their
  own review procedure (to be defined).

Example pattern for major anchoring (syntax may vary by tooling):

```
>=2.4,<3.0
```

## Patch-cycle upgrade workflow
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

## Locked dependency review
At the start of each new `PATCH` cycle, review any pinned or tightly constrained
dependencies and confirm each pin is still required. Remove unnecessary pins
before completing the cycle-opening update.

## Enforcement
Violations are fatal exceptions that block merges, releases, and deployments.

CI must fail when:
- `poetry.lock` is out of sync with `pyproject.toml`
- a dependency spec uses `*`
- a dependency is pinned without documented justification
- dependency updates occur without the required validation run

## Examples (TODO)
- Major-anchored version specifications.
- Patch-cycle update checklist in practice.
- Justified pinning due to upstream regression.
- Dependency addition for new functionality.

## Related documents
- Application versioning scheme: [application-versioning-scheme.md](../../code-management/application-versioning-scheme.md)
- Pull request workflow: [pull-request-workflow.md](../../code-management/pull-request-workflow.md)
