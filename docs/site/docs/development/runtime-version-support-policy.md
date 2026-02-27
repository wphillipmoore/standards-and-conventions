# Runtime Version Support Policy

## Purpose

Define a tiered runtime version support policy that balances forward progress
with consumer compatibility. This policy provides cross-language guidance for
which runtime versions to test, which CI results block merges, and when to drop
a version.

## Scope

Applies to all repositories that declare a language runtime dependency (Python,
Java, Go, or any other language with discrete runtime releases). This policy
complements language-specific upgrade workflows such as the Python version
management standard; it does not replace them.

## Definitions

- **GA release**: A production-ready version published through the language's
  official release channel.
- **Active bugfix**: A GA release series receiving regular bug fixes and
  security patches from the upstream maintainer.
- **Security-fix-only**: A GA release series receiving only critical security
  patches, with no further bug fixes.
- **EOL (end of life)**: A release series no longer receiving any patches from
  the upstream maintainer.
- **Hard gate**: A CI check that blocks PR merge when it fails.
- **Soft gate**: A CI check that surfaces warnings but does not block PR merge.
  Failures must be documented in the PR with rationale and any follow-up
  tracking.
- **Advisory**: A CI check run for informational purposes only. Failures are
  logged but carry no merge or follow-up obligations.

## Support tiers

Each runtime version in a CI matrix must be assigned to exactly one tier.

### Tier 1 — active bugfix

The primary supported version. This is the version used for development,
deployment, and release artifacts.

- Gate type: hard gate (blocking).
- All tests and validation checks must pass.
- Production deployments use a Tier 1 version.

### Tier 2 — next development release

The upcoming version that has entered GA but has not yet been promoted to the
primary development version.

- Gate type: soft gate (non-blocking).
- Failures are tracked as issues but do not block PRs.
- Purpose: early detection of incompatibilities before the next version becomes
  Tier 1.

### Tier 3 — security-fix-only

A prior version still receiving security patches from the upstream maintainer.
Relevant primarily for libraries that must support consumers on older runtimes.

- Gate type: hard gate while the version remains supportable.
- Dropped when continued support inhibits forward progress (see
  [Drop criteria](#drop-criteria)).

### Tier 4 — EOL

A version that has reached end of life upstream.

- Gate type: advisory (best-effort).
- Failures are logged but never block merges.
- Do not invest effort maintaining compatibility with EOL versions.

## CI matrix mapping

| Tier | CI job label | Gate type | Merge impact |
| --- | --- | --- | --- |
| 1 — active bugfix | `bugfix-<version>` | Hard gate | Blocks merge |
| 2 — next development | `preview-<version>` | Soft gate | Warning only |
| 3 — security-fix-only | `security-<version>` | Hard gate | Blocks merge |
| 4 — EOL | `eol-<version>` | Advisory | No impact |

Every label includes the version because each tier may contain more than one
version simultaneously.

Each repository must document its CI matrix with tier assignments in its
repository standards or CI configuration.

## Application versus library scope

### Applications

Applications target a single runtime version (Tier 1). They do not maintain
backward compatibility with older runtimes.

- CI matrix: Tier 1 only, plus optionally Tier 2 for forward-looking testing.
- Production deployments always use the Tier 1 version.

### Libraries

Libraries test against all Tier 1 versions and conditionally against Tier 3
versions to support consumers on older runtimes.

- CI matrix: Tier 1 (hard gate), Tier 3 if consumers require it (hard gate),
  Tier 2 (soft gate).
- Tier 4 is advisory and included only when the cost is negligible.

## Drop criteria

A runtime version should be considered for removal from the CI matrix when any
of the following conditions apply:

- Supporting the version requires pinning dependencies to older versions that
  block upgrades for other supported versions.
- Maintaining compatibility shims or conditional code paths that degrade
  readability or test coverage.
- Continued support prevents adopting language features or library APIs that
  benefit all other supported versions.
- The upstream maintainer has moved the version to EOL status.

A single criterion is sufficient justification to begin the drop procedure.

## Drop procedure

1. **Open an issue** documenting which version is being dropped and the
   evidence supporting the decision (reference the applicable drop criteria).
2. **Update the CI matrix** to remove the version or reclassify it to Tier 4
   (advisory) as an intermediate step.
3. **Update build configuration** to remove any compatibility shims, conditional
   code paths, or pinned dependencies that existed solely to support the
   dropped version.
4. **Add a release note** entry (or changelog entry, per the repository's
   versioning scheme) stating the minimum supported runtime version.
5. **Update repository documentation** (repository standards, README, or
   equivalent) to reflect the new minimum version.

## Language lifecycle references

These summaries describe how major languages classify their release phases.
Use them to map upstream status to the tier definitions above.

### Python

Python uses three lifecycle phases per minor release:

- **Bugfix** (approximately 18 months after GA): active bugfix releases.
  Maps to Tier 1 or Tier 2.
- **Security** (approximately 3.5 years after bugfix phase ends): security
  patches only. Maps to Tier 3.
- **EOL**: no further patches. Maps to Tier 4.

Reference: Python Developer's Guide, Status of Python Versions.

### Java

Java release lifecycle varies by distribution:

- **LTS releases** (for example, 17, 21): extended support from the
  distribution vendor. Typically maps to Tier 1 or Tier 3 depending on
  the project's adoption timeline.
- **Non-LTS releases**: short support windows (six months). Typically map to
  Tier 2 for forward-looking testing only.

Determine support commitment based on the distribution's published support
schedule, not the OpenJDK upstream alone.

### Go

Go supports the two most recent major releases:

- **Current release**: maps to Tier 1.
- **Previous release**: maps to Tier 3 (still receiving security patches).
- **Older releases**: maps to Tier 4 (EOL).

Reference: Go Release Policy.

### Rust

Rust uses a six-week release cadence. Only the latest stable release receives
patches; there is no extended security-fix window for prior releases.

- **Current stable release**: maps to Tier 1.
- **Previous two releases (N-1, N-2)**: maps to Tier 3. Rust does not patch
  these, but they remain recent enough for library consumers. This project
  uses an N-2 policy (~18 weeks of coverage), matching Go's two-release
  approach.
- **Older releases**: maps to Tier 4 (EOL).

Reference: Rust Release Process (Rust Forge).

## Related documents

- Python version management:
  [version-management.md](python/version-management.md)
- Deprecation warning policy:
  [deprecation-warnings.md](deprecation-warnings.md)
- Source code management guidelines:
  [source-control-guidelines.md](../code-management/source-control-guidelines.md)
