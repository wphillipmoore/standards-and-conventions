# Application Versioning Scheme

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
- The base version (`MAJOR.MINOR.PATCH`) is stored in a manifest and changes
  only via pull request.
- `BUILD` is derived at build time; build numbers are never committed to git.
- `PATCH` increments when a promotion to the release branch is opened to start
  a new development cycle.
- `MAJOR` and `MINOR` changes are explicit human decisions.
- Version numbers are never reused or mutated after deployment.
- The scheme avoids implicit state and hidden counters in source control.

## Version format

Use a four-part numeric version string:

```text
MAJOR.MINOR.PATCH.BUILD
```

Rules:

- Each component is a non-negative integer with no leading zeros (except `0`).
- `BUILD` is the rightmost component and is computed at build time.
- No suffixes or build metadata are used in the version string.

## Source of truth

- The canonical base version (`MAJOR.MINOR.PATCH`) lives in a single build or
  package manifest.
- The full runtime version string (`MAJOR.MINOR.PATCH.BUILD`) is derived at
  build time.
- All other references must derive from the base version or computed runtime
  version; do not duplicate it in code.

## Increment rules

- `PATCH` increments by exactly 1 when a promotion to the release branch opens
  and starts a new development cycle.
- `MAJOR` and `MINOR` changes reset `PATCH` to `0` and restart the build
  sequence through derivation.
- Version changes are part of merge pull requests; direct commits to develop
  or release branches are forbidden.
- Feature and bugfix pull requests do not change the base version unless they
  are explicitly designated as version-bump work.

## Build derivation

`BUILD` is derived from git history and does not live in source control.

Recommended algorithm:

1. Read the base version from the manifest (`MAJOR.MINOR.PATCH`).
2. Find the commit that introduced that base version.
3. Set `BUILD` to the number of commits since that commit on the current
   branch.

Release tagging:

- Tag release bases as `vMAJOR.MINOR.PATCH` when promoting to the release
  branch.
- CI pipelines should fetch full history (`fetch-depth: 0`) so the build
  derivation is deterministic.

If the base version commit cannot be found (for example, shallow history),
fail the build rather than guessing.

## Promotion workflow

1. Create a promotion branch from develop and open a pull request to the
   release branch.
2. If the release branch has diverged, merge release into the promotion branch
   and resolve conflicts there.
3. Immediately open a separate pull request back to develop that increments
   `PATCH` to start the next development cycle.
4. Merge the promotion pull request only after release validation.
5. Merge the `PATCH` bump pull request before the next develop merge.
6. Promote release to production with no additional version changes.

## Validation and failure modes

CI must fail when:

- The base version string does not match `MAJOR.MINOR.PATCH`.
- The derived build number cannot be computed deterministically.
- `PATCH` bump pull requests do not increment `PATCH` by exactly 1.
- A version number is reused or regresses.

Violations are fatal exceptions that block merges, releases, and deployments.

## Related documents

- Branching and deployment: [branching-and-deployment.md](../branching/branching-and-deployment.md)
