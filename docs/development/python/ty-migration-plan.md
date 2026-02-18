# Ty adoption migration plan

## Purpose

Adopt `ty` as a peer type checker alongside `mypy`, run both in parallel long
enough to build confidence, and then retire `mypy` once parity is proven.

## Scope

- Python repositories governed by the canonical standards.
- CI hard gates and local validation scripts.
- Developer tooling and dependency management.

## Non-goals

- Changing the type-hinting style rules or typing standards.
- Introducing new runtime dependencies.
- Rewriting unrelated tooling or CI workflows.

## Assumptions

- `mypy` remains the authoritative gate until cutover is explicitly approved.
- `ty` is installed as a dev dependency and invoked via the same tooling
  convention as existing checks (for example, `uv run ty check`).
- The migration uses existing version and dependency gate policies.

## Plan

### Phase 0: Baseline decisions

1. Pin `ty` to the latest available version at adoption time (current target:
   `0.0.13`, released 2026-01-21) and manage it like other dev tools.
2. Use community defaults: `ty check` as the canonical command and
   `[tool.ty]` in `pyproject.toml` for configuration.
3. Define the parity criteria required to remove `mypy` (TBD; data-driven).

### Phase 1: Standards updates

1. Update Python development standards to include `ty` alongside `mypy`.
2. Update local validation guidance to run `ty` in addition to `mypy`.
3. Update CI gate definitions to include `ty` as a hard gate (while `mypy`
   remains in place).
4. Add `ty` to dependency update scope and audit expectations.

### Phase 2: Repository enablement

For each repo:

1. Add `ty` to the dev dependency group.
2. Update local validation scripts to run `ty`.
3. Update CI workflows to run `ty` in parallel with `mypy`.
4. Update project documentation to reflect the new command.
5. Regenerate lockfiles and requirements exports.

### Phase 3: Side-by-side evaluation

1. Run `ty` and `mypy` on every repo and capture outcomes.
2. Log discrepancies (false positives, missing coverage, configuration gaps)
   in repo-specific issues.
3. Track elapsed time and stability of `ty` runs for each repo.

### Phase 4: Remediation and alignment

1. Resolve code issues that are valid for both checkers.
2. Adjust configuration to align `ty` with the established typing standard.
3. Keep `mypy` authoritative until all blockers are closed.

### Phase 5: Cutover and cleanup

1. Remove `mypy` from CI gates and local validation.
2. Remove `mypy` from dev dependencies and requirements exports.
3. Update standards documentation to make `ty` the sole required checker.
4. Close the migration issues and document the completion.

## Acceptance criteria

- `ty` runs cleanly on all in-scope repositories with no new unresolved errors.
- All mismatches between `ty` and `mypy` have documented resolutions.
- `ty` performance and stability are acceptable for CI hard-gate usage.
- Explicit approval to remove `mypy` is recorded before cutover.

## Risks and mitigations

- **Behavioral divergence**: keep `mypy` authoritative until parity is proven.
- **False positives**: track issues per repo and fix or configure explicitly.
- **Tooling instability**: pin the `ty` version and upgrade only through the
  standard dependency update workflow.

## Rollback strategy

If `ty` causes instability, disable it in CI and local validation by reverting
Phase 2 changes. Keep `mypy` as the sole gate until a new decision is made.

## Open questions

- What criteria and duration define "parity" for cutover approval?
