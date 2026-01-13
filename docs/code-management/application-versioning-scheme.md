# Application Versioning Scheme

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Operating model](#operating-model)
- [Invariants](#invariants)
- [Version format](#version-format)
- [Source of truth](#source-of-truth)
- [Increment rules](#increment-rules)
- [Promotion workflow](#promotion-workflow)
- [Validation and failure modes](#validation-and-failure-modes)
- [Related documents](#related-documents)

## Purpose
Ensure every deployed application artifact has a unique, human-readable version
identifier that is stable, auditable, and compatible with release governance.

## Scope
This scheme applies to applications that run a single active instance in
production and follow linear promotion across environments.

It does not define versioning for shared libraries or multi-active deployment
models.

## Operating model
- Each environment runs exactly one application version at a time.
- Promotion is linear from develop to release to production.
- Version identifiers must be sufficient to answer, "What is running now?"

## Invariants
- Every deployed artifact maps to a unique version string.
- The rightmost component increments on every merge to the develop branch.
- `PATCH` increments when a promotion to the release branch is opened.
- `MAJOR` and `MINOR` changes are explicit human decisions.
- Version numbers are never reused or mutated after deployment.
- The scheme avoids implicit state and hidden counters.

## Version format
Use a four-part numeric version string:

```
MAJOR.MINOR.PATCH.BUILD
```

Rules:
- Each component is a non-negative integer with no leading zeros (except `0`).
- `BUILD` is the rightmost component and auto-increments.
- No suffixes or build metadata are used in the version string.

## Source of truth
- The canonical version string lives in a single build or package manifest.
- All other references must derive from that value; do not duplicate it in code.
- Runtime reads should use package metadata rather than hard-coded strings.

## Increment rules
- `BUILD` increments by exactly 1 on every merge to the develop branch.
- `PATCH` increments by exactly 1 when a promotion to the release branch opens
  and resets `BUILD` to `0`.
- `MAJOR` and `MINOR` changes reset `PATCH` and `BUILD` to `0`.
- Version changes are part of merge pull requests; direct commits to develop
  or release branches are forbidden.
- If the develop branch advances before merge, rebase and reapply the next
  `BUILD` value to avoid collisions.

## Promotion workflow
1. Create a promotion branch from develop and open a pull request to the
   release branch.
2. If the release branch has diverged, merge release into the promotion branch
   and resolve conflicts there.
3. Immediately open a separate pull request back to develop that increments
   `PATCH` and resets `BUILD` to `0`.
4. Merge the promotion pull request only after release validation.
5. Merge the `PATCH` bump pull request before the next develop merge.
6. Promote release to production with no additional version changes.

## Validation and failure modes
CI must fail when:
- The version string does not match `MAJOR.MINOR.PATCH.BUILD`.
- `BUILD` is not exactly one higher than the current develop value for
  merge pull requests.
- `PATCH` bump pull requests do not reset `BUILD` to `0`.
- A version number is reused or regresses.

Violations are fatal exceptions that block merges, releases, and deployments.

## Related documents
- Release and versioning policy: [release-versioning.md](release-versioning.md)
- Library versioning scheme: [library-versioning-scheme.md](library-versioning-scheme.md)
