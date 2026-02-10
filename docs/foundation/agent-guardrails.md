# Agent guardrails

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Guardrails](#guardrails)
- [Maintenance](#maintenance)

## Purpose

Provide a short, high-signal list of non-negotiable agent constraints that must
be re-checked before taking action.

## Scope

Use before executing commands or making edits in any repository governed by
these standards.

## Guardrails

- If `uv.lock` exists, all Python commands MUST run as `uv run python3 ...`
  (except installing `uv`). If `uv.lock` is missing, stop and treat the
  repository as misconfigured.
- If a prompt starts with `RTFM`, invoke the `rtfm` skill immediately and
  suspend normal work.
- Standards bootstrap is `AGENTS.md` only; do not run include-resolution
  scripts or use bootstrap skills.
- If on an eternal branch (`develop`, `release`, `main`), create a feature
  branch before any edits or commits.

## Maintenance

Keep this list short. Add items only when repeated failures show a hard
non-negotiable rule needs a dedicated preflight gate.
