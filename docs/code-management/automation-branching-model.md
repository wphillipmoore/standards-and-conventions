# Automation Branching Model

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Core invariants](#3-core-invariants)
- [4. Branch roles](#4-branch-roles)
  - [develop](#develop)
  - [main](#main)
  - [release branches](#release-branches)
- [5. Short-lived branches](#5-short-lived-branches)
  - [feature/*](#feature)
  - [bugfix/*](#bugfix)
  - [hotfix/*](#hotfix)
- [6. Release workflow](#6-release-workflow)
- [7. Forbidden operations](#7-forbidden-operations)
- [8. Related documents](#8-related-documents)

## Status
Active v0.2

---

## 1. Purpose
Define a branching model for tooling and automation repositories that preserves
stable releases while keeping development flow simple.

## 2. Scope
Applies to automation repositories, including shared GitHub Actions, scripts,
and tooling libraries that are consumed across repositories.

## 3. Core invariants
- `develop` is the integration branch for all changes.
- `main` represents stable, released automation.
- Releases are tagged and immutable.
- Release branches exist only when multiple versions must be supported.

## 4. Branch roles

### develop
- default branch for active development
- entry point for all code changes

### main
- stable release branch
- merges only from `develop` or release branches
- source of tagged releases

### release branches
Long-lived branches for supported release lines when needed.

Naming:
- `release/<major>.<minor>.x`

Rules:
- patch-only changes
- no new features
- no merges from `develop` or `main`

## 5. Short-lived branches
All work occurs in short-lived branches that merge into `develop` or a release
branch.

### feature/*
Use for:
- new automation capabilities
- refactors or structural changes
- documentation updates

Rules:
- branched from `develop`
- merged into `develop`
- deleted after merge

### bugfix/*
Use for:
- non-urgent defect fixes
- patch changes on a release branch

Rules:
- branched from `develop` or the target release branch
- merged into the branch it was created from
- deleted after merge

### hotfix/*
Use for:
- urgent defects affecting released automation

Rules:
- branched from the affected release branch or `main`
- merged into that branch
- backported to `develop`
- deleted after merge

## 6. Release workflow
- Merge `develop` into `main` for stable releases.
- Tag releases on `main`.
- For patch releases on older lines, release from the relevant release branch
  and merge back to `main`.

## 7. Forbidden operations
- direct commits to `develop`, `main`, or release branches
- merging `develop` into release branches
- releasing from untagged or dirty source

## 8. Related documents
- Repository types and attributes: [repository-types-and-attributes.md](repository-types-and-attributes.md)
- Shared actions library: [shared-actions-library.md](shared-actions-library.md)
- Release and versioning policy: [release-versioning.md](release-versioning.md)
