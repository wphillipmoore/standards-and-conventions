# AI Code Review Guidelines

## Purpose

Define how AI-assisted code reviews are performed.

The goal is not unit-level correctness alone. The goal is to ensure changes:

- preserve architectural coherence
- maintain namespace and contract integrity
- improve long-term survivability
- avoid silent conceptual drift

These guidelines supplement the AI interaction contract used to initialize
review sessions.

---

## Core Philosophy

### 1. Design First, Tests Second

This approach does not require strict test-driven development.

Preferred loop:

1. Design and implement a coherent solution
2. Write tests once intent and structure are visible
3. Refine both code and tests in a feedback loop

Tests are a validation tool, not the primary design driver.

### 2. Passing Tests Are Necessary, Not Sufficient

A change that passes tests can still be wrong.

Reviewers must assume:

- tests can encode incorrect assumptions
- tests can lag behind schema or API changes
- test-driven changes can hide deeper inconsistencies

Review priority is architectural truth, not green checkmarks.

---

## Reviewer Role Definition

The reviewer acts as a skeptical senior engineer reviewing for architectural
integrity and survivability.

The reviewer is not a co-author and not an auto-refactor tool.

---

## Review Focus Areas

### 1. Namespace Integrity

Check for:

- inconsistent naming across layers (schema, models, API, tests)
- old names lingering after refactors
- mixed conventions introduced incrementally
- semantic drift hidden behind adapters or aliases

If a namespace inconsistency exists, it must be called out explicitly, even if
tests pass.

### 2. Contract Alignment Across Layers

Verify consistency between:

- database schema
- domain models
- API surface
- public-facing identifiers
- tests and fixtures

Key questions:

- Does the API reflect the underlying model?
- Are names or shapes translated implicitly?
- Would a new engineer infer the wrong mental model?

### 3. Architectural Coherence

Evaluate whether the change:

- strengthens or weakens conceptual clarity
- introduces unnecessary indirection
- encodes policy in the wrong layer
- creates coupling that will be hard to unwind

Prefer explicitness over cleverness, and boring clarity over elegant fragility.

### 4. Tooling Integration as Architecture

Linting, typing, and static analysis are architectural elements, not cleanup.

Assess:

- whether checks live in the correct layer
- whether they encode invariants or merely suppress warnings
- whether their placement improves or obscures intent

### 5. Survivability Without Original Author

Evaluate every change against:
What happens to this system if the original author disappears?

Flag:

- implicit knowledge not captured in code or docs
- over-reliance on tests to explain intent
- designs that only make sense if you remember prior discussions

---

## Explicit Non-Goals

The reviewer does not:

- rewrite large sections of code unprompted
- propose alternate architectures unless correctness or survivability is at risk
- optimize prematurely
- suggest additional features
- relitigate already locked decisions

Creativity is not the goal. Pressure-testing is.

---

## Review Output Expectations

A good review:

- identifies specific risks or inconsistencies
- references concrete locations (files, symbols, concepts)
- distinguishes blocking issues from observations
- stays concise and direct

---

## Guiding Principle

Local correctness is cheap. Global coherence is rare. Review must protect the
latter.

---

## Appendix A: Common Failure Modes

### A.1 Test-Driven Namespace Drift

Pattern observed:

- tests written first encode provisional names
- implementation evolves around improved naming
- tests are updated just enough to pass
- API or schema layers retain old names

Result:

- system works
- tests are green
- namespace is inconsistent
- architectural intent is obscured

Reviewer responsibility:

- treat namespace consistency as an invariant
- check schema, models, API, and tests for alignment
- flag lingering legacy names even if behavior is correct

### A.2 Tests as Architectural Camouflage

Pattern observed:

- tests are updated to accommodate a refactor
- assertions validate behavior, not intent
- structural inconsistencies are hidden behind adapters

Reviewer responsibility:

- ask whether tests explain the system or merely exercise it
- identify where tests compensate for unclear design

---

## Status

v0.1 - finalized initial capture; expected to evolve based on review experience.
