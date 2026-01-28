# Agent pre-response checklist

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Checklist](#checklist)
- [Prompt shortcuts](#prompt-shortcuts)

## Purpose
Provide a minimal checklist to detect drift toward assumption-light or
non-adversarial responses.

## Scope
Use before finalizing any response governed by the interaction contract.

## Checklist
- Problem constraints are explicit.
- Assumptions are stated.
- If the prompt starts with `RTFM`, switch to the RTFM protocol and suspend
  normal work.
- Repository profile is identified and applied (type, branching model, validation policy).
- Preflight gate emitted before any file edit or git action (branch, issue, docs-only scope, validation policy).
- No silent guessing of material facts.
- Weak premises were challenged.
- No unnecessary abstraction introduced.
- Solution survives without its author.
- Answer is not polite-but-wrong.

## Prompt shortcuts
Use a standalone prompt that invokes the checklist, such as:
- `Run agent checklist`
