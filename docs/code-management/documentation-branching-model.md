# Documentation Branching Model

## Table of Contents

- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Core invariants](#3-core-invariants)
- [4. Branch roles](#4-branch-roles)
  - [develop](#develop)
  - [main](#main)
- [5. Promotion flow](#5-promotion-flow)
- [6. Short-lived branches](#6-short-lived-branches)
  - [feature/*](#feature)
  - [bugfix/*](#bugfix)
- [7. Validation expectations](#7-validation-expectations)
- [8. Forbidden operations](#8-forbidden-operations)
- [9. Related documents](#9-related-documents)

## Status

Active v0.3

---

## 1. Purpose

Define the branching model for documentation repositories that supports a
staging preview on `develop` and a live published site on `main`.

## 2. Scope

Applies to repositories that contain documentation, templates, or example
snippets only and do not publish deployable artifacts.

## 3. Core invariants

- `develop` and `main` are the two eternal branches.
- `develop` is the default branch and staging target.
- `main` is the promotion target for live/published documentation.
- All changes arrive via short-lived branches merged to `develop`.
- Changes reach `main` only via promotion PR from `develop`.
- Versioning is optional and not required for publication.

## 4. Branch roles

### develop

- default branch for documentation
- integration branch for all changes
- source of the staging/preview documentation site (`dev` version)

### main

- promotion target for reviewed, publish-ready content
- source of the live documentation site (`latest` version)
- receives changes only from `develop` via PR

## 5. Promotion flow

To publish documentation changes to the live site:

1. Merge feature/bugfix branches to `develop` via PR.
2. Verify the staging site (`dev` version) renders correctly.
3. Open a PR from `develop` to `main`.
4. Merge the promotion PR to update the live site.

## 6. Short-lived branches

Use short-lived branches for all changes.

### feature/*

Use for:

- new documentation or structure
- refactors, reorganizations, or template updates

Rules:

- branched from `develop`
- merged into `develop`
- deleted after merge

### bugfix/*

Use for:

- corrections, clarifications, or small fixes

Rules:

- branched from `develop`
- merged into `develop`
- deleted after merge

## 7. Validation expectations

Documentation repositories must run markdownlint for documentation validation.
Automated test or release validation is not required. Additional validation is
optional unless a specific repository documents a requirement.

## 8. Forbidden operations

- direct commits to `develop` or `main`
- long-lived branches other than `develop` and `main`
- merging to `main` from any branch other than `develop`
- force-pushing to `develop` or `main`

## 9. Related documents

- Repository types and attributes: [repository-types-and-attributes.md](repository-types-and-attributes.md)
- Pull request workflow: [pull-request-workflow.md](pull-request-workflow.md)
- Documentation toolchain: [../development/documentation-toolchain.md](../development/documentation-toolchain.md)
