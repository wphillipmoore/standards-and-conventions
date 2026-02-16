---
name: publish
description: Drive the end-to-end publish workflow for library and documentation repositories, including post-publish dependency updates.
---

# Publish

## Table of Contents

- [Overview](#overview)
- [Preflight](#preflight)
- [Version override](#version-override)
- [Library-release mode](#library-release-mode)
  - [Phase 1 — Prepare release](#phase-1--prepare-release)
  - [Phase 2 — Review and merge](#phase-2--review-and-merge)
  - [Phase 3 — Confirm publish](#phase-3--confirm-publish)
  - [Phase 4 — Confirm version bump](#phase-4--confirm-version-bump)
  - [Phase 5 — Next-cycle dependency updates](#phase-5--next-cycle-dependency-updates)
- [Docs-only mode](#docs-only-mode)
  - [Phase 1 — Confirm deployment](#phase-1--confirm-deployment)
  - [Phase 2 — Toolchain dependency updates](#phase-2--toolchain-dependency-updates)
- [Dependency update categories](#dependency-update-categories)
- [Resources](#resources)

## Overview

Orchestrate the full publish lifecycle for a repository and initialize the next
development cycle. The key value is in the post-publish phase: after cutting a
release, develop is the safest place to absorb dependency updates across all
categories. This skill covers both the publish confirmation steps and the
subsequent dependency refresh.

Two modes are available, determined by `repository_type` in the repository
profile:

- **library-release** — For library repositories that publish versioned
  artifacts.
- **docs-only** — For documentation repositories that deploy via CI.

This skill is not applicable to application repositories.

**Arguments** (library-release mode only):

- `/publish` — Publish the current version in develop (default; patch).
- `/publish minor` — Bump to the next minor version before publishing.
- `/publish major` — Bump to the next major version before publishing.

## Preflight

- Read the repository profile to determine `repository_type`.
- If the type is `library`, follow **library-release mode**.
- If the type is `documentation`, follow **docs-only mode**.
- If the type is anything else, stop and inform the user that this skill does
  not apply.
- Confirm you are on the `develop` branch with a clean working tree.
- Identify the canonical validation command from the repository profile.

## Version override

This section applies only to library-release mode when `minor` or `major` is
specified. Skip it for the default patch case.

The automated post-publish bump always increments the patch version, so develop
normally carries the next patch. When accumulated changes justify a minor or
major release, the version must be bumped on develop before the release is
prepared.

1. Read the current version from the project manifest on `develop`.
2. Compute the target version by incrementing the minor or major component
   (resetting lower components to zero).
3. Update the version at the source of truth in the project manifest.
4. Commit the version bump to `develop` with a message following the
   commit standards (e.g., `chore: bump version to <target>`).
5. Proceed to Phase 1 with the updated version.

## Library-release mode

### Phase 1 — Prepare release

1. Run the `prepare_release` script on `develop`.
2. The script creates a `release/<version>` branch, generates the changelog,
   pushes the branch, creates a PR to `main`, and enables auto-merge.
3. Confirm the release branch and PR were created successfully.

### Phase 2 — Review and merge

1. Wait for CI to validate the release branch.
2. Confirm the PR merges into `main` via regular merge (not squash).
3. Confirm the release branch is deleted after merge.

### Phase 3 — Confirm publish

Verify all publish artifacts are present:

- Git tag `v<version>` on `main`.
- Develop tag `develop-v<version>` for changelog boundaries.
- GitHub Release created.
- Package artifact published to the registry.
- GitHub Pages documentation deployed for the new version.

### Phase 4 — Confirm version bump

1. Wait for the automated `chore/bump-version-<next>` PR to `develop`.
2. Confirm the bump PR auto-merges.
3. Update local `develop` to incorporate the merge.

### Phase 5 — Next-cycle dependency updates

1. Create a `chore/next-cycle-deps-<version>` branch from `develop`.
2. Update all applicable dependency categories (see
   [Dependency update categories](#dependency-update-categories)).
3. Run full validation.
4. Submit via `pr-workflow`.

## Docs-only mode

### Phase 1 — Confirm deployment

1. Verify the docs CI workflow ran on `develop`.
2. Confirm the site deployed successfully via mike.

### Phase 2 — Toolchain dependency updates

1. Create a `chore/toolchain-deps` branch from `develop`.
2. Update all applicable toolchain dependency categories (see
   [Dependency update categories](#dependency-update-categories)).
3. Run full validation.
4. Submit via `pr-workflow`.

## Dependency update categories

Each category follows the same pattern: update at the source of truth,
regenerate derived artifacts, run full validation. Failures follow the
`dependency-update` skill's failure handling procedure.

**Library dependencies** (library repos only):

- Direct dependencies in the project manifest.
- Lockfile regeneration.
- Review anchored dependencies for release eligibility: check each anchor
  record's exit criteria and re-test where upstream fixes may have landed.
  Follow the dependency anchor records standard and the tracking issues
  linked from each record.

**Toolchain dependencies** (all repos):

- CI action version pins.
- Runtime version pins (per the runtime version support policy tier model).
- Documentation toolchain (mkdocs-material, mike, mkdocstrings).
- Linters, formatters, and type checkers (ruff, mypy, ty, markdownlint-cli).
- Test frameworks and coverage tools (pytest, coverage).
- Build tools (hatch, setuptools, uv).

## Resources

- `docs/code-management/library-branching-and-release.md`
- `docs/code-management/documentation-branching-model.md`
- `docs/code-management/release-versioning.md`
- `docs/code-management/library-versioning-scheme.md`
- `docs/dependencies/dependency-update-workflow.md`
- `docs/dependencies/overview.md`
- `docs/development/runtime-version-support-policy.md`
- `docs/development/documentation-toolchain.md`
- `docs/development/python/dependency-management.md`
- `skills/dependency-update/SKILL.md`
- `skills/pr-workflow/SKILL.md`
