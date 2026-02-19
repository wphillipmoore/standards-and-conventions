# Agent guardrails

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
- Never use administrative overrides or privilege escalation to bypass CI
  gates, branch protection, or hook enforcement (e.g. `--admin`, `--force`
  to protected branches, `--no-verify`) without explicit human approval.
  The perceived simplicity of a change does not justify bypassing
  safeguards. When CI is pending, use `--auto` and wait.

## Maintenance

Keep this list short. Add items only when repeated failures show a hard
non-negotiable rule needs a dedicated preflight gate.
