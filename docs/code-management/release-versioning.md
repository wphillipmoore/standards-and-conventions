# Release and Versioning Policy

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Release Definition](#2-release-definition)
- [3. Versioning](#3-versioning)
- [4. Artifact Properties](#4-artifact-properties)
- [5. Relationship to Branches](#5-relationship-to-branches)
- [6. Rollback Strategy](#6-rollback-strategy)
- [7. Forbidden Practices](#7-forbidden-practices)
- [8. Guiding Principle](#8-guiding-principle)

## Status
Frozen v0.1 snapshot

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
- a merge into the release or main branch
- producing a versioned, immutable artifact
- suitable for deployment and rollback

Releases are not mutable.

---

## 3. Versioning
- Semantic Versioning (MAJOR.MINOR.PATCH) is used.
- Version numbers are assigned at release time.
- Version bumps are explicit and reviewed.

Guideline:
- MAJOR: breaking changes
- MINOR: backward-compatible features
- PATCH: bug fixes

---

## 4. Artifact Properties
Released artifacts must be:
- immutable
- content-addressable by version
- installable by the ecosystem's package manager
- reproducible from source

Artifacts are first-class operational objects.

---

## 5. Relationship to Branches
- Branches drive deployment automation.
- Artifacts provide audit, rollback, and traceability.

Production runs what main points to, but operational truth is anchored in
artifacts.

---

## 6. Rollback Strategy
Rollback is performed by:
- redeploying a previously released version
- never mutating or reusing version numbers

Rollbacks are operational decisions, not code changes.

---

## 7. Forbidden Practices
- mutating released artifacts
- reusing version numbers
- deploying unreleased code
- publishing artifacts that never ran in test

---

## 8. Guiding Principle
If you cannot precisely name what is running, you do not control it.
