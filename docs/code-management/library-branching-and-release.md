# Library Branching and Release Model

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Core invariants](#3-core-invariants)
- [4. Branch roles](#4-branch-roles)
  - [main](#main)
  - [release branches](#release-branches)
- [5. Short-lived branches](#5-short-lived-branches)
  - [feature/*](#feature)
  - [bugfix/*](#bugfix)
  - [hotfix/*](#hotfix)
- [6. Release workflow](#6-release-workflow)
- [7. Pre-release policy](#7-pre-release-policy)
- [8. Backporting policy](#8-backporting-policy)
- [9. Forbidden operations](#9-forbidden-operations)
- [10. Related documents](#10-related-documents)

## Status
Active v0.2

---

## 1. Purpose
Define a branching model for libraries that supports multiple concurrent
release lines and predictable publishing.

## 2. Scope
Applies to library repositories that publish artifacts to a package registry and
are not deployed to environment-bound infrastructure.

## 3. Core invariants
- `main` is the integration branch.
- Stable releases are tagged and published from `main` or a release branch.
- Release branches represent supported `MAJOR.MINOR` release lines.
- Changes land in `main` first; backports are explicit.
- Released artifacts are immutable and reproducible from source.

## 4. Branch roles

### main
- default branch for active development
- source of new `MAJOR` and `MINOR` releases

### release branches
Long-lived branches for supported release lines.

Naming:
- `release/<major>.<minor>.x`

Rules:
- patch-only changes
- no new features
- no merges from `main`

Support policy:
- default target is the current and previous `MAJOR.MINOR` lines
- repositories may expand or contract support by updating the repository profile

## 5. Short-lived branches
All work occurs in short-lived branches that merge into `main` or a release
branch.

### feature/*
Use for:
- new functionality or features
- refactoring or structural changes
- documentation updates

Rules:
- branched from `main`
- merged into `main`
- deleted after merge

### bugfix/*
Use for:
- non-urgent defect fixes for current development
- patch releases on a release branch

Rules:
- branched from `main` or the target release branch
- merged into the branch it was created from
- deleted after merge

### hotfix/*
Use for:
- urgent defects affecting released versions

Rules:
- branched from the affected release branch
- merged into that release branch
- backported to `main`
- deleted after merge

## 6. Release workflow
- `MAJOR` and `MINOR` releases are cut from `main`.
- `PATCH` releases are cut from the relevant release branch.
- Every release is tagged and published as an immutable artifact.

## 7. Pre-release policy
- Pre-releases are allowed for validation and early adopters.
- Pre-releases are tagged and published with pre-release identifiers defined by
  the library versioning scheme or the target ecosystem.
- Pre-releases never replace or mutate stable releases.

## 8. Backporting policy
- Backports are explicit and documented in the pull request.
- Use cherry-picks or equivalent to avoid feature drift.
- If a change cannot be safely backported, document the rationale.

## 9. Forbidden operations
- direct commits to `main` or release branches
- merging `main` into release branches
- releasing from untagged or dirty source
- publishing artifacts without a matching source tag

## 10. Related documents
- Repository types and attributes: [repository-types-and-attributes.md](repository-types-and-attributes.md)
- Release and versioning policy: [release-versioning.md](release-versioning.md)
- Library versioning scheme: [library-versioning-scheme.md](library-versioning-scheme.md)
