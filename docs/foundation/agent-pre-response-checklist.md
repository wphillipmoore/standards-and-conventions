# Agent pre-response checklist

## Purpose

Provide a minimal checklist to detect drift toward assumption-light or
non-adversarial responses.

## Scope

Use before finalizing any response governed by the interaction contract.

## Checklist

- Problem constraints are explicit.
- Assumptions are stated.
- If the prompt starts with `RTFM`, invoke the `rtfm` skill and suspend
  normal work.
- Repository profile is identified and applied (type, branching model,
  validation policy).
- `AGENTS.md` and all referenced standards files are loaded (no bootstrap
  scripts).
- Guardrails re-read before any command or edit
  (`docs/foundation/agent-guardrails.md`).
- Preflight gate emitted before any file edit or git action (branch, issue,
  docs-only scope, validation policy).
- For documentation repositories, markdownlint is required. Do not ask for
  additional validation unless the repository documents it.
- No silent guessing of material facts.
- Weak premises were challenged.
- No unnecessary abstraction introduced.
- Solution survives without its author.
- Answer is not polite-but-wrong.

## Prompt shortcuts

Use a standalone prompt that invokes the checklist, such as:

- `Run agent checklist`
