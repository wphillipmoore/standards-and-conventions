# Cognitive drift log

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Template](#template)
- [Prompt shortcuts](#prompt-shortcuts)

## Purpose

Provide a minimal log template for recording concerning or hard failures.

## Scope

Use when a response or behavior violates the interaction contract.

## Template

```text
Date:
Context:
Prompt:
Observed failure:
State snapshot (branch, git status, files touched):
Category (A–F):
Severity (Soft / Hard):
Correction applied:
```

## Prompt shortcuts

Use a standalone prompt that invokes the log, such as:

- `Log cognitive drift`

Date: 2026-01-22
Context: Replacing the repository's `skills/context-bootstrap` with the home
directory copy after unexpected changes were detected.
Prompt: "Please import the context-bootstrap skill from my home dir into this
repo for reference, replacing the current one entirely -- again"
Observed failure: Proceeded with the file copy instead of stopping immediately
to ask how to handle unexpected changes.
Category (A–F): F
Severity (Soft / Hard): Hard
Correction applied: Stop on unexpected changes and ask how to proceed before any
further action.

Date: 2026-01-27
Context: Standards-and-conventions repo. User asked to import the
context-bootstrap skill from ~/.codex. This required creating a GitHub issue
before branching or file changes.
Prompt: "Import the context-bootstrap skill from ~/.codex to this repo, as a
reference"
Observed failure: I asked the user for an issue number instead of creating a
new GitHub issue myself. This directly violated the documented rule to create
an issue when none exists before branching or changing files. It also inverted
the intended behavior of context-bootstrap: the standards were loaded, but I
treated them as optional guidance rather than binding workflow steps.
Why this happened (analysis):

- I over-weighted a generic "ask for missing inputs" instinct and treated issue
  creation as blocked without user-provided fields, despite the explicit rule
  to create the issue when missing.
- I failed to operationalize the standard into a concrete action (create issue
  now, mark assumptions) and instead deferred responsibility to the user, which
  is contrary to the documentation-first workflow.
- I did not apply the "Question-Asking Bias" requirement to act first when the
  decision is reversible; creating an issue is reversible and should have been
  done immediately with best-effort assumptions.
- I missed a guardrail opportunity: no explicit self-check that a GitHub issue
  exists before any other workflow steps.
Category (A–F): F
Severity (Soft / Hard): Hard
Correction applied:
- Immediately created issue #90 to track the remediation.
- Added a required guardrail: before any branch or file edits, check for an
  existing issue; if absent, create one immediately using best-effort
  assumptions and clearly mark those assumptions in the issue body.
- Update standards/skill guidance to explicitly forbid asking the user for an
  issue number when the issue does not yet exist unless acceptance criteria are
  materially ambiguous.
- Added this verbose drift log entry to capture root-cause hypotheses and
  prevent recurrence.
