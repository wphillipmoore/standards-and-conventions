# Documentation Branching Model

## Status

Active v0.3

---

## 1. Purpose

Define the branching model for documentation repositories that supports a
staging preview on `develop` and a live published site on `main`.

## 2. Scope

Applies to repositories that contain documentation, templates, or example
snippets only and do not publish deployable artifacts.

## 3. Core invariants

- `develop` and `main` are the two eternal branches.
- `develop` is the default branch and staging target.
- `main` is the promotion target for live/published documentation.
- All changes arrive via short-lived branches merged to `develop`.
- Changes reach `main` only via promotion PR from `develop`.
- Versioning is optional and not required for publication.

## 4. Branch roles

### develop

- default branch for documentation
- integration branch for all changes
- source of the staging/preview documentation site (`dev` version)

### main

- promotion target for reviewed, publish-ready content
- source of the live documentation site (`latest` version)
- receives changes only from `develop` via PR

## 5. Promotion flow

To publish documentation changes to the live site:

1. Merge feature/bugfix branches to `develop` via PR.
2. Verify the staging site (`dev` version) renders correctly.
3. Open a PR from `develop` to `main`.
4. Merge the promotion PR to update the live site.

## 6. Short-lived branches

Use short-lived branches for all changes.

### Issue-linked naming

All feature and bugfix branches must include the repository issue number in
the branch name. The format is:

```text
{type}/{issue}-{short-description}
```

- `{type}`: `feature` or `bugfix`
- `{issue}`: repository issue number
- `{short-description}`: kebab-case summary

Examples:

```text
feature/42-update-branching-standards
bugfix/15-fix-broken-link
```

For cross-repo work driven by a project issue, create sub-issues in each
affected repository and use each repo's issue number in its branch name. See
[GitHub Projects — Cross-repo work pattern](../github-projects.md#cross-repo-work-pattern).

### One branch per issue per repository

At most one open branch may exist per issue per repository at any time.

Before creating a branch, check for an existing branch for the same issue:

```bash
git fetch origin
git branch -r | grep '/42-'
```

If a branch already exists, check it out and resume work on it. Do not create a
second branch. This rule prevents orphaned branches from accumulating when work
is restarted.

### feature/*

Use for:

- new documentation or structure
- refactors, reorganizations, or template updates

Rules:

- branched from `develop`
- merged into `develop`
- deleted after merge

### bugfix/*

Use for:

- corrections, clarifications, or small fixes

Rules:

- branched from `develop`
- merged into `develop`
- deleted after merge

## 7. Validation expectations

Documentation repositories must run markdownlint for documentation validation.
Automated test or release validation is not required. Additional validation is
optional unless a specific repository documents a requirement.

## 8. Forbidden operations

- direct commits to `develop` or `main`
- long-lived branches other than `develop` and `main`
- merging to `main` from any branch other than `develop`
- force-pushing to `develop` or `main`

## 9. Related documents

- Branching and deployment model: [branching-and-deployment.md](branching-and-deployment.md)
