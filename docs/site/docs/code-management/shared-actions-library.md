# Shared Actions Library

## Purpose

Define standards for a shared GitHub Actions library that provides reusable,
versioned automation across repositories.

## Scope

Applies to all repositories that consume shared automation for CI, validation,
release, or pull request workflows.

## Design principles

- Centralize action logic to reduce drift.
- Keep workflows in product repositories minimal and declarative.
- Prefer composite actions over per-repository scripts.
- Version everything; never consume unpinned defaults.
- Build actions that are usable across application and library repositories.
- Shared actions repositories follow the library branching model.

## Repository structure

A shared actions repository must be organized by responsibility:

```text
actions/
  <action-name>/
    action.yml
    README.md
    scripts/
```

Rules:

- One action per directory.
- Each action documents inputs, outputs, and example usage.
- Scripts stay minimal and are colocated with the action.

## Action design rules

- Actions must be deterministic and idempotent.
- Inputs are explicit; avoid implicit environment inference.
- Failures must be actionable and surface clear error messages.
- Avoid tightly coupling actions to a single repository structure.

## Versioning and pinning

- Version the repository with SemVer tags (for example, `v1`, `v1.2.0`).
- Tags apply to the entire repository; there is no per-action tagging.
- Repositories must reference actions by tag or commit SHA.
- Never reference the default branch.

## Security and permissions

- Actions must declare least-privilege permissions.
- Avoid persistent credentials; prefer short-lived tokens when possible.
- Document any required secrets and their scope.

## Adoption workflow

1. Introduce actions in the shared library.
2. Update standards to reference the shared library.
3. Pilot in one repository and validate parity.
4. Roll out incrementally across repositories.

## Implementation plan

Phase 0: decisions

- Choose repository name, visibility, and default branch (`develop`).
- Select the initial versioning/tagging policy.

Phase 1: bootstrap

- Add `README.md`, `LICENSE`, and `SECURITY.md`.
- Define repository layout under `actions/`.

Phase 2: core actions

- Validation action (tests, lint, type checking, coverage).
- Dependency audit action.
- Auto-merge action with a label-based opt-out.

Phase 3: repository CI

- Lint action metadata and scripts.
- Validate workflow syntax.

Phase 4: standards integration

- Reference the shared actions library in code management standards.
- Document the manual-merge opt-out label.

Phase 5: pilot adoption

- Replace in-repo workflow logic with shared actions in one repository.
- Validate parity with existing CI gates.

Phase 6: rollout

- Apply shared actions to the remaining repositories in waves.
- Keep changes small and reversible.

## Related documents

- Library branching and release model: [library-branching-and-release.md](branching/library-branching-and-release.md)
- Source control guidelines: [source-control-guidelines.md](source-control-guidelines.md)
- Pull request workflow: [pull-request-workflow.md](pull-request-workflow.md)
