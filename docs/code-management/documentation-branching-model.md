# Documentation Branching Model

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Core invariants](#3-core-invariants)
- [4. Branch roles](#4-branch-roles)
  - [develop](#develop)
- [5. Short-lived branches](#5-short-lived-branches)
  - [feature/*](#feature)
  - [bugfix/*](#bugfix)
- [6. Validation expectations](#6-validation-expectations)
- [7. Forbidden operations](#7-forbidden-operations)
- [8. Related documents](#8-related-documents)

## Status
Active v0.2

---

## 1. Purpose
Define a minimal branching model for documentation repositories that keeps the
workflow simple and durable.

## 2. Scope
Applies to repositories that contain documentation, templates, or example
snippets only and do not publish deployable artifacts.

## 3. Core invariants
- `develop` is the single eternal branch.
- `main` is not used for documentation repositories.
- All changes arrive via short-lived branches.
- There are no release branches or promotion flows.
- Versioning is optional and not required for publication.

## 4. Branch roles

### develop
- default branch for documentation
- source of published GitHub content
- integration and release branch when a single branch is used

## 5. Short-lived branches
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

## 6. Validation expectations
Documentation repositories must run markdownlint for documentation validation.
Automated test or release validation is not required. Additional validation is
optional unless a specific repository documents a requirement.

## 7. Forbidden operations
- direct commits to `develop`
- long-lived branches other than `develop`
- adding release branches or promotion flows without updating standards

## 8. Related documents
- Repository types and attributes: [repository-types-and-attributes.md](repository-types-and-attributes.md)
- Pull request workflow: [pull-request-workflow.md](pull-request-workflow.md)
