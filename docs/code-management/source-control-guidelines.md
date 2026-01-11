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
- [6. Locked vs. Flexible Decisions](#6-locked-vs-flexible-decisions)
  - [Locked at v0.1](#locked-at-v01)
  - [Explicitly Flexible](#explicitly-flexible)
- [7. Guiding Principle](#7-guiding-principle)

## Status
Frozen v0.1 snapshot

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

Anti-goal:
Clever automation that cannot be reasonably expressed outside the current CI
provider.

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
