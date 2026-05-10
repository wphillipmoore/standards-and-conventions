# Branching and Deployment Model

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
this document.

Documentation repositories follow the documentation branching model and are not
governed by this document. See
[documentation-branching-model.md](documentation-branching-model.md).

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

| Branch  | Purpose                         | Deployment Target |
|---------|---------------------------------|-------------------|
| develop | Integration and rapid iteration | development       |
| release | Qualification and validation    | test              |
| main    | Production truth                | production        |

### Pull Request Requirement

All eternal branches require pull requests for changes. Direct pushes to
develop, release, or main are forbidden.

- Changes to develop: create a `feature/*` or `bugfix/*` branch, then open a PR
  to develop.
- Changes to release: create a PR from a promotion branch to release.
- Changes to main: create a PR from a promotion branch to main.
- Exception: hotfix/* branches follow special forward-merge rules (see
  docs/code-management/branching/hotfix-policy.md).

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

### Issue-linked naming

All feature, bugfix, and hotfix branches must include the repository issue
number in the branch name. The format is:

```text
{type}/{issue}-{short-description}
```

- `{type}`: `feature`, `bugfix`, or `hotfix`
- `{issue}`: repository issue number
- `{short-description}`: kebab-case summary

Examples:

```text
feature/42-add-caching
bugfix/17-fix-retry-timeout
hotfix/3-critical-auth-failure
```

Release branches are exempt from this requirement (automated by the publish
workflow, no issue association).

For cross-repo work driven by a project issue, create sub-issues in each
affected repository and use each repo's issue number in its branch name. See
[GitHub Projects — Cross-repo work pattern](../github-projects.md#cross-repo-work-pattern).

### One branch per issue per repository

At most one open branch may exist per issue per repository at any time.

Before creating a branch, check for an existing branch for the same issue:

```bash
git fetch origin
git branch -r | grep '/42-'
```

If a branch already exists, check it out and resume work on it. Do not create a
second branch. This rule prevents orphaned branches from accumulating when work
is restarted.

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

feature/*or bugfix/* -> develop -> release -> main

Promotion semantics:

- develop to release: candidate release, aggressive testing
- release to main: production-ready, ship

---

## 8. Forbidden Operations

The following are explicitly disallowed:

- merging feature/*or bugfix/* directly into release or main
- direct commits to eternal branches
- direct pushes to develop, release, or main
- cherry-picking between eternal branches
- deploying to production without passing through release
- long-lived non-eternal branches
- using branch prefixes other than feature/*, bugfix/*, hotfix/*, or promotion/*

---

## 9. Guiding Principle

Boring workflows that never surprise are a competitive advantage.
