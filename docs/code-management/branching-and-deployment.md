# Branching and Deployment Model

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Core Invariants](#2-core-invariants)
- [3. Deployment Environments](#3-deployment-environments)
- [4. Eternal Branches](#4-eternal-branches)
  - [Pull Request Requirement](#pull-request-requirement)
- [5. Short-Lived Branches](#5-short-lived-branches)
  - [Branch Naming Conventions](#branch-naming-conventions)
  - [feature/*](#feature)
  - [bugfix/*](#bugfix)
  - [hotfix/*](#hotfix)
- [6. Promotion Flow](#6-promotion-flow)
- [7. Forbidden Operations](#7-forbidden-operations)
- [8. Guiding Principle](#8-guiding-principle)

## Status
Frozen v0.1 snapshot

---

## 1. Purpose
Define the branching model and deployment semantics for repositories.

Goals:
- clear, boring, survivable workflows
- deterministic promotion across environments
- minimal cognitive overhead for future contributors
- explicit handling of failure modes

---

## 2. Core Invariants
1. Each long-lived branch maps to exactly one deployment environment.
2. Promotion is monotonic: development to test to production.
3. Humans decide merges; automation performs deployments.
4. Branch names encode intent, not activity.
5. The system must survive without its original author.

---

## 3. Deployment Environments
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

## 4. Eternal Branches
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
- Changes to release: create a PR from develop to release.
- Changes to main: create a PR from release to main.
- Exception: hotfix/* branches follow special forward-merge rules (see
  docs/code-management/hotfix-policy.md).

Each merge into these branches triggers automatic deployment to the
corresponding environment where automation exists.

---

## 5. Short-Lived Branches
All work occurs in short-lived branches.

### Branch Naming Conventions
Only the following branch prefixes are allowed:
- feature/*
- bugfix/*
- hotfix/*

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

---

## 6. Promotion Flow
Normal flow:

feature/* or bugfix/* -> develop -> release -> main

Promotion semantics:
- develop to release: candidate release, aggressive testing
- release to main: production-ready, ship

---

## 7. Forbidden Operations
The following are explicitly disallowed:
- merging feature/* or bugfix/* directly into release or main
- direct commits to eternal branches
- direct pushes to develop, release, or main
- cherry-picking between eternal branches
- deploying to production without passing through release
- long-lived non-eternal branches
- using branch prefixes other than feature/*, bugfix/*, or hotfix/*

---

## 8. Guiding Principle
Boring workflows that never surprise are a competitive advantage.
