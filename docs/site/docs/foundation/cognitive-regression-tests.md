# Cognitive regression tests

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

Hard failures include:

- Proceeding without applying the repository profile when it materially
  affects workflow (for example, a documentation repository that still
  demands validation or uses the wrong branching model).
- Performing a file edit or git action without emitting the required preflight
  gate.
- Using administrative overrides or privilege escalation (e.g. `--admin`,
  `--force` to protected branches, `--no-verify`) without explicit human
  approval.

## Prompt shortcuts

Use a standalone prompt that invokes the tests, such as:

- `Run cognitive regression tests`
