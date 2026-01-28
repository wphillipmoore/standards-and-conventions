# Source Code Management Guidelines

## Table of Contents
- [Status](#status)
- [1. AI Assistance (Explicitly Bounded)](#1-ai-assistance-explicitly-bounded)
- [2. Version Control Platform](#2-version-control-platform)
  - [Lock-In Awareness](#lock-in-awareness)
- [3. Repository Strategy](#3-repository-strategy)
  - [Core Philosophy](#core-philosophy)
  - [Boundary Rule](#boundary-rule)
  - [Explicit Non-Decision](#explicit-non-decision)
- [4. Runtime Version Policy](#4-runtime-version-policy)
  - [Supported Versions](#supported-versions)
  - [CI Requirements](#ci-requirements)
  - [Deployment Rule](#deployment-rule)
- [5. CI/CD Constraints](#5-cicd-constraints)
  - [CI gates](#ci-gates)
  - [Docs-only CI skip policy](#docs-only-ci-skip-policy)
  - [Local enforcement hooks](#local-enforcement-hooks)
- [6. Locked vs. Flexible Decisions](#6-locked-vs-flexible-decisions)
  - [Locked at v0.1](#locked-at-v01)
  - [Explicitly Flexible](#explicitly-flexible)
- [7. Guiding Principle](#7-guiding-principle)

## Status
Active v0.2

---

## 1. AI Assistance (Explicitly Bounded)
Constraints:
- AI-generated code must be reviewed with the same rigor as external
  contributions.
- AI assistance must never become a silent dependency.
- The codebase must remain understandable, auditable, and maintainable without
  AI.

Invariant:
Code correctness, determinism, and maintainability override speed or
convenience.

---

## 2. Version Control Platform
Git is the source control system.

GitHub is the initial central repository host, including GitHub Actions for
CI/CD.

This decision is explicitly provisional, not foundational.

### Lock-In Awareness
GitHub-specific dependencies must be:
- understood
- tracked
- periodically reassessed

The project must retain enough knowledge to evaluate the cost and feasibility
of migration to an alternative host if required.

Migration readiness is not required at v0.1, but migration awareness is.

---

## 3. Repository Strategy

### Core Philosophy
Repositories should be:
- small
- modular
- scoped to a single semantic responsibility

Independent components should live in separate repositories by default.

### Boundary Rule
Repository boundaries follow semantic ownership and lifecycle, not convenience.

This improves:
- independent evolution
- reduced cognitive load
- long-term maintainability
- survivability without original authorship

### Explicit Non-Decision
Monorepo vs. multirepo strategy is not locked at v0.1.

This decision may be revisited once:
- dependency graphs stabilize
- tooling friction is observed
- CI/CD cost and complexity are measurable

---

## 4. Runtime Version Policy

### Supported Versions
- The current stable language runtime version is the default target.
- Additional versions must be explicitly listed and justified.

### CI Requirements
CI pipelines must validate against the current stable runtime version.

### Deployment Rule
Production deployments use the current stable runtime version.

Invariant:
Code that cannot survive the next runtime release without heroics is already
technical debt.

---

## 5. CI/CD Constraints
CI/CD pipelines must be:
- deterministic
- stateless
- reproducible locally

Automation should avoid reliance on opaque or irreducibly platform-specific
behavior.

CI configuration must remain:
- readable
- minimal
- replaceable

Prefer a shared actions library for reusable workflow logic and pin action
references by tag or commit SHA.

Anti-goal:
Clever automation that cannot be reasonably expressed outside the current CI
provider.

### CI gates
Every CI check must be classified as either a hard gate or a soft gate.

- Hard gate: blocking. A failing check prevents PR submission and merge.
- Soft gate: warning-only. A failing check does not block merge, but must be
  surfaced in the PR with rationale and any follow-up tracking.

Each repository must explicitly list its checks and their gate type. If a
check is not classified, treat it as a hard gate until documented.

Hard gates must be enforced as required status checks on the target branches
so failing GitHub Actions block PR merges.

Each repository must also document which hard gates apply per branch. Some
hard gates may be develop-only, while others must run on all eternal branches.

### Docs-only CI skip policy
Repositories must define a docs-only allowlist (for example, `docs/**`,
`README.md`, and `CHANGELOG.md`). `.github/**` is not docs-only.

CI workflows must include a docs-only detection job that computes
`docs_only=true|false` based on the PR diff against the allowlist and exposes it
as a workflow output.

When `docs_only` is `true`, skip test and version-validation jobs by gating
them with the docs-only output. Dependency audits should still run by default;
if a repository chooses to skip them, it must document the exception.

Markdownlint and any docs-only validation commands must still run.

### Local enforcement hooks
Use local Git hooks to fail closed on branch protection rules that should
never be violated.

Minimum requirement:
- Install a `pre-commit` hook that blocks commits on protected branches
  (`develop`, `release`, `main`, and `release/*`).
- Store hooks in-repo (for example, `scripts/git-hooks/`) and set
  `core.hooksPath` locally so the hooks are enabled.
- Hooks must print a clear, actionable error and exit non-zero on violations.

Example hook (store as `scripts/git-hooks/pre-commit` and mark executable):
```bash
#!/usr/bin/env bash
set -euo pipefail

branch="$(git rev-parse --abbrev-ref HEAD)"

case "$branch" in
  develop|release|main|release/*)
    echo "ERROR: direct commits to protected branches are forbidden ($branch)." >&2
    echo "Create a short-lived branch (feature/* or bugfix/*) and open a PR." >&2
    exit 1
    ;;
esac
```

---

## 6. Locked vs. Flexible Decisions

### Locked at v0.1
- Git as the source control system
- GitHub as the initial hosting provider
- GitHub Actions for CI/CD
- Runtime validation on the current stable version

### Explicitly Flexible
- Repository granularity and structure
- CI/CD provider choice
- Deployment orchestration details
- Degree and style of AI-assisted development

---

## 7. Guiding Principle
All source code management decisions are evaluated against a single overriding
criterion:

The system must survive without its original author.

Tooling, structure, and process choices are judged by their contribution to
long-term clarity, auditability, and evolutionary capacity.
