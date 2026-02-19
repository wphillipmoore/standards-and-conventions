# Library Branching and Release Model

## Status

Active v0.3

---

## 1. Purpose

Define a branching model for libraries that supports predictable publishing
through a stable release branch with automated version bumping.

## 2. Scope

Applies to library repositories that publish reusable artifacts (via a package
registry or tagged automation) and are not deployed to environment-bound
infrastructure.

## 3. Core invariants

- `develop` is the integration branch and the default branch.
- `main` is the stable release branch; pushes to `main` trigger publishing.
- `develop` always has a version one patch ahead of `main`.
- Release branches are short-lived; they exist only to create a PR to `main`.
- Changes land in `develop` first; promotions are explicit via release branches.
- Released artifacts are immutable and reproducible from source.

## 4. Branch roles

### main

- stable release branch
- pushes to `main` trigger the publish workflow (tag, publish, release)
- protected: changes arrive only via merged PRs from release branches
- after publish, `main` is merged back into `develop` via an automated version
  bump PR

### develop

- default branch for active development
- entry point for all code changes
- version is always one patch ahead of `main` (e.g., if `main` is `0.2.0`,
  `develop` is `0.2.1`)

### release branches

Short-lived branches for promoting a version from `develop` to `main`.

Naming:

- `release/<version>` (e.g., `release/0.2.0`)

Rules:

- branched from `develop`
- merged into `main` via PR (regular merge, not squash)
- deleted after merge
- no new features; release preparation only (changelog, version finalization)

## 5. Short-lived branches

All work occurs in short-lived branches that merge into `develop`.

### feature/*

Use for:

- new functionality or features
- refactoring or structural changes
- documentation updates

Rules:

- branched from `develop`
- merged into `develop`
- deleted after merge

### bugfix/*

Use for:

- non-urgent defect fixes for current development

Rules:

- branched from `develop`
- merged into `develop`
- deleted after merge

### hotfix/*

Use for:

- urgent defects affecting the released version on `main`

Rules:

- branched from `main`
- merged into `main` via PR
- the subsequent publish and version bump PR propagates the fix to `develop`
- deleted after merge

### chore/*

Use for:

- automated or manual maintenance tasks (version bumps, dependency updates)

Rules:

- branched from `develop` (or from the automation target)
- merged into the originating branch
- deleted after merge

## 6. Release workflow

1. **Prepare**: Run the `prepare_release` script on `develop`. This creates a
   `release/<version>` branch, generates the changelog (if configured), pushes
   the branch, creates a PR to `main`, and enables auto-merge.
2. **Review**: CI validates the release branch. Branch protection rules on
   `main` must pass before merge.
3. **Merge**: The PR merges into `main` (regular merge commit, not squash).
4. **Publish**: The publish workflow triggers on push to `main`:
   - Extracts the version from the project manifest.
   - Checks for duplicate tags (skips if already tagged).
   - Builds and publishes the artifact to the package registry.
   - Creates a git tag `v<version>` on `main`.
   - Tags `develop` with `develop-v<version>` for changelog boundaries.
   - Creates a GitHub Release.
5. **Bump**: The publish workflow computes the next patch version, creates a
   `chore/bump-version-<next>` branch from `develop`, merges `main` into it,
   updates the version, and creates an auto-merge PR to `develop`.

## 7. Post-publish automation

After a successful publish, the workflow maintains the version invariant:

- Merges `main` back into `develop` (via the bump branch) so that `develop`
  picks up the release tag, changelog, and any release-branch artifacts.
- Bumps the patch version (e.g., `0.2.0` → `0.2.1`) so `develop` is always
  ahead of `main`.
- The bump PR auto-merges. If the next release should be a minor or major bump,
  the team can adjust the version before the PR merges or in a follow-up commit.

## 8. Pre-release policy

- Pre-releases are not published unless there is an exceptional need.
- If published, pre-releases use identifiers defined by the target ecosystem.
- Pre-releases never replace or mutate stable releases.

## 9. Backporting policy

- Backports are explicit and documented in the pull request.
- Use cherry-picks or equivalent to avoid feature drift.
- If a change cannot be safely backported, document the rationale.

## 10. Forbidden operations

- direct commits to `develop`
- direct commits to `main`
- force-pushing to `main` or `develop`
- squash-merging release branches into `main` (use regular merge)
- releasing from untagged or dirty source
- publishing artifacts without a matching source tag

## 11. Related documents

- Repository types and attributes: [repository-types-and-attributes.md](../../repository/repository-types-and-attributes.md)
- Release and versioning policy: [release-versioning.md](../versioning/release-versioning.md)
- Library versioning scheme: [library-versioning-scheme.md](../versioning/library-versioning-scheme.md)
