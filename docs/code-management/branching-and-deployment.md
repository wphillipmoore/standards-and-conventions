# Branching and Deployment Model

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Core Invariants](#3-core-invariants)
- [4. Deployment Environments](#4-deployment-environments)
- [5. Eternal Branches](#5-eternal-branches)
  - [Pull Request Requirement](#pull-request-requirement)
- [6. Short-Lived Branches](#6-short-lived-branches)
  - [Branch Naming Conventions](#branch-naming-conventions)
  - [feature/*](#feature)
  - [bugfix/*](#bugfix)
  - [hotfix/*](#hotfix)
  - [promotion/*](#promotion)
- [7. Promotion Flow](#7-promotion-flow)
- [8. Forbidden Operations](#8-forbidden-operations)
- [9. Guiding Principle](#9-guiding-principle)

## Status
Active v0.2

---

## 1. Purpose
Define the branching model and deployment semantics for application repositories.

Goals:
- clear, boring, survivable workflows
- deterministic promotion across environments
- minimal cognitive overhead for future contributors
- explicit handling of failure modes

---

## 2. Scope
Applies to application repositories with environment-based deployments and
linear promotion.

Library repositories follow the library branching model and are not governed by
this document. See
[library-branching-and-release.md](library-branching-and-release.md).

Documentation repositories follow the documentation branching model and are not
governed by this document. See
[documentation-branching-model.md](documentation-branching-model.md).

Automation repositories follow the automation branching model and are not
governed by this document. See
[automation-branching-model.md](automation-branching-model.md).

Repository type definitions live in
[repository-types-and-attributes.md](repository-types-and-attributes.md).

## 3. Core Invariants
1. Each long-lived branch maps to exactly one deployment environment.
2. Promotion is monotonic: development to test to production.
3. Humans decide merges; automation performs deployments.
4. Branch names encode intent, not activity.
5. The system must survive without its original author.

---

## 4. Deployment Environments
There are exactly four environments:
- sandbox
- development
- test
- production

Each environment consists of:
- one database
- one API
- one running application version

Sandbox is a pre-PR environment for feature, bugfix, and hotfix branch work. It
is not tied to an eternal branch and is outside the promotion flow; updates are
manual or ad hoc.

Parallel stacks, canaries, or shadow environments are explicitly out of scope
at v0.1.

---

## 5. Eternal Branches
The following branches always exist and are protected:
- develop
- release
- main

| Branch  | Purpose                       | Deployment Target |
|---------|-------------------------------|-------------------|
| develop | Integration and rapid iteration | development     |
| release | Qualification and validation  | test              |
| main    | Production truth              | production        |

### Pull Request Requirement
All eternal branches require pull requests for changes. Direct pushes to
develop, release, or main are forbidden.

- Changes to develop: create a feature/* or bugfix/* branch, then open a PR to
  develop.
- Changes to release: create a PR from a promotion branch to release.
- Changes to main: create a PR from a promotion branch to main.
- Exception: hotfix/* branches follow special forward-merge rules (see
  docs/code-management/hotfix-policy.md).

Each merge into these branches triggers automatic deployment to the
corresponding environment where automation exists.

---

## 6. Short-Lived Branches
All work occurs in short-lived branches.

### Branch Naming Conventions
This prefix list applies to application repositories only.

Only the following branch prefixes are allowed:
- feature/*
- bugfix/*
- hotfix/*
- promotion/*

No other prefixes are permitted. When in doubt, use feature/*.

### feature/*
Use for:
- new functionality or features
- structural changes or refactoring
- documentation updates
- dependency updates
- build system changes
- any work that is not a bug fix

Rules:
- branched from develop
- merged into develop via pull request
- deleted immediately after merge

### bugfix/*
Use for:
- non-urgent defect fixes discovered in development or test environments
- fixes that do not block production

Rules:
- same as feature/*
- branched from develop
- merged into develop via pull request
- deleted immediately after merge

### hotfix/*
Use for:
- production-blocking issues only
- critical defects affecting live users
- security vulnerabilities in production

Rules:
- branched from main
- merged into main via pull request
- immediately forward-merged into release and develop
- deleted immediately after resolution

Creation of a hotfix branch is an explicit admission of upstream process
failure.

### promotion/*
Use for:
- controlled promotion between eternal branches
- release qualification or production promotion

Rules:
- branched from the source eternal branch
- merged only into the target eternal branch
- deleted immediately after merge
- required for normal promotions to release and main

Naming:
- `promotion/release-<version>-<yyyymmddhhmmss>` for develop to release
- `promotion/main-<version>-<yyyymmddhhmmss>` for release to main

---

## 7. Promotion Flow
Normal flow:

feature/* or bugfix/* -> develop -> release -> main

Promotion semantics:
- develop to release: candidate release, aggressive testing
- release to main: production-ready, ship

---

## 8. Forbidden Operations
The following are explicitly disallowed:
- merging feature/* or bugfix/* directly into release or main
- direct commits to eternal branches
- direct pushes to develop, release, or main
- cherry-picking between eternal branches
- deploying to production without passing through release
- long-lived non-eternal branches
- using branch prefixes other than feature/*, bugfix/*, hotfix/*, or promotion/*

---

## 9. Guiding Principle
Boring workflows that never surprise are a competitive advantage.
