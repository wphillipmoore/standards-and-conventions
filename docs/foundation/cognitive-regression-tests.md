# Cognitive regression tests

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Categories](#categories)
- [Failure criteria](#failure-criteria)
- [Prompt shortcuts](#prompt-shortcuts)

## Purpose
Define regression tests that detect drift toward polite, assumption-light, or
non-adversarial behavior.

## Scope
Use when validating conformance to the interaction contract.

## Categories
- A: ill-posed problem detection
- B: assumption surfacing
- C: complexity discipline
- D: adversarial pushback
- E: time and expiration awareness
- F: anti-goal enforcement

## Failure criteria
Any hard failure indicates contract drift and requires correction.

## Prompt shortcuts
Use a standalone prompt that invokes the tests, such as:
- `Run cognitive regression tests`
