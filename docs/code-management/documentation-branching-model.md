# Documentation Branching Model

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Core invariants](#3-core-invariants)
- [4. Branch roles](#4-branch-roles)
  - [main](#main)
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
- `main` is the single eternal branch.
- All changes arrive via short-lived branches.
- There are no release branches or promotion flows.
- Versioning is optional and not required for publication.

## 4. Branch roles

### main
- default branch for documentation
- source of published GitHub content

## 5. Short-lived branches
Use short-lived branches for all changes.

### feature/*
Use for:
- new documentation or structure
- refactors, reorganizations, or template updates

Rules:
- branched from `main`
- merged into `main`
- deleted after merge

### bugfix/*
Use for:
- corrections, clarifications, or small fixes

Rules:
- branched from `main`
- merged into `main`
- deleted after merge

## 6. Validation expectations
Documentation repositories do not require automated test or release validation.
Keep validation optional unless a specific repository documents a requirement.

## 7. Forbidden operations
- direct commits to `main`
- long-lived branches other than `main`
- adding release branches or promotion flows without updating standards

## 8. Related documents
- Repository types and attributes: [repository-types-and-attributes.md](repository-types-and-attributes.md)
- Pull request workflow: [pull-request-workflow.md](pull-request-workflow.md)
