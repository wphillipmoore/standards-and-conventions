# Release and Versioning Policy

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Release Definition](#2-release-definition)
  - [Application repositories](#application-repositories)
  - [Library repositories](#library-repositories)
  - [Documentation repositories](#documentation-repositories)
- [3. Versioning](#3-versioning)
- [4. Pre-release policy](#4-pre-release-policy)
- [5. Artifact Properties](#5-artifact-properties)
- [6. Relationship to Branches](#6-relationship-to-branches)
- [7. Rollback Strategy](#7-rollback-strategy)
- [8. Forbidden Practices](#8-forbidden-practices)
- [9. Guiding Principle](#9-guiding-principle)

## Status
Active v0.2

---

## 1. Purpose
Define how components are versioned, released, and consumed.

Goals:
- deterministic builds
- reproducible deployments
- clean rollback semantics
- auditability over time

---

## 2. Release Definition
A release is defined as:
- a versioned, immutable artifact
- a matching source tag
- suitable for deployment, distribution, and rollback

Releases are not mutable.

### Application repositories
For application repositories, a release is tied to promotion:
- merge into the `release` or `main` branch
- produce a versioned artifact for deployment
- tag the release base as `vMAJOR.MINOR.PATCH`

### Library repositories
For library repositories, a release is tied to publishing:
- tag a version in source control
- publish the artifact to the package registry when applicable
- tagging alone is sufficient when distribution is via source control

For ecosystems with strict versioning (for example, PyPI), use the ecosystem
format (PEP 440) and never attempt to republish the same version.

### Documentation repositories
Documentation repositories do not require formal releases or version numbers.
Git history and tags (when needed) are the source of truth.

---

## 3. Versioning
- Use the applicable versioning scheme for the artifact type.
- Base versions are assigned explicitly; build numbers are derived at build time
  for applications.
- Version bumps are explicit and reviewed.

Guideline:
- Libraries: use the Library Versioning Scheme or the ecosystem's required
  versioning format.
- Applications: use the Application Versioning Scheme
  (`MAJOR.MINOR.PATCH.BUILD`) with a derived `BUILD` value.

---

## 4. Pre-release policy
- Pre-releases are allowed only when the target ecosystem supports them.
- Pre-release artifacts must use explicit pre-release identifiers.
- Pre-releases are never promoted or mutated into stable releases.

## 5. Artifact Properties
Released artifacts must be:
- immutable
- content-addressable by version
- consumable by the ecosystem's distribution mechanism
- reproducible from source

Artifacts are first-class operational objects.

---

## 6. Relationship to Branches
- Application branches drive deployment automation.
- Library releases are cut from release branches.
- Artifacts provide audit, rollback, and traceability.

Operational truth is anchored in artifacts, not branch pointers.

---

## 7. Rollback Strategy
Rollback is performed by:
- redeploying a previously released version
- never mutating or reusing version numbers

Rollbacks are operational decisions, not code changes.

---

## 8. Forbidden Practices
- mutating released artifacts
- reusing version numbers
- deploying unreleased code
- publishing artifacts that never passed required validation
- promoting pre-releases as stable without a new version

Violations are fatal exceptions that block merges, releases, and deployments.

---

## 9. Guiding Principle
If you cannot precisely name what is running, you do not control it.
