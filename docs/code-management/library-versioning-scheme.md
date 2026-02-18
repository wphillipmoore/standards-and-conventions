# Library Versioning Scheme

## Purpose

Define how supporting libraries are versioned, released, and consumed.

## Scope

This scheme applies to internal and external libraries used by applications.
If the target ecosystem mandates a specific versioning format, that format
supersedes the default scheme below (for example, Python packages follow
PEP 440).

## Invariants

- Every released library artifact maps to a unique version string.
- Version numbers are never reused or mutated after release.
- Releases are immutable and reproducible from source.
- Compatibility expectations are explicit and tied to the version number.

## Version format

Default: Semantic Versioning

```text
MAJOR.MINOR.PATCH
```

Rules:

- Each component is a non-negative integer with no leading zeros (except `0`).
- Stable releases do not use suffixes or build metadata.
- Pre-release identifiers are allowed only for pre-release artifacts and must
  never be promoted to stable releases as-is.
- Additional numeric segments or local metadata are allowed only when required
  by the ecosystem or explicitly documented.

## Source of truth

- The canonical version string lives in a single build or package manifest.
- All other references must derive from that value; do not duplicate it in code.
- Runtime reads should use package metadata rather than hard-coded strings.
- For Python packages, the manifest is `pyproject.toml`; avoid local version
  segments or build metadata unless the ecosystem requires them.

## Increment rules

- `MAJOR` increments for breaking API or behavioral changes.
- `MINOR` increments for backward-compatible features or expansions.
- `PATCH` increments for backward-compatible bug fixes.
- Changes that are not backward-compatible must never ship without a `MAJOR`
  increment.
- Pre-1.0 libraries must still follow the same rules; the `0.x` series does not
  waive compatibility discipline.

## Release workflow

1. Assign a version at release time and tag it in source control.
2. Build and publish an immutable artifact for that version.
3. Ensure the released artifact matches the tagged source exactly.
4. Produce release notes that describe compatibility impact.

## Dependency management

- Applications and libraries must consume explicit version ranges that encode
  compatibility expectations.
- Production builds must pin exact versions via lockfiles or equivalent
  mechanisms to ensure reproducibility.
- Upgrades are deliberate changes, not background drift.

## Validation and failure modes

CI must fail when:

- The version string does not match the required format.
- A version number is reused or regresses.
- A release is attempted from untagged or dirty source.
- A breaking change is detected without a `MAJOR` increment.

Violations are fatal exceptions that block publishing and consumption.

## Related documents

- Repository types and attributes: [repository-types-and-attributes.md](repository-types-and-attributes.md)
- Library branching and release model: [library-branching-and-release.md](library-branching-and-release.md)
- Release and versioning policy: [release-versioning.md](release-versioning.md)
- Application versioning scheme: [application-versioning-scheme.md](application-versioning-scheme.md)
