# Shared Tooling Sync

## Purpose

Shared scripts (lint, git hooks, dev tooling) are copied across all
repositories. This design ensures tagged releases are fully self-contained
for build reproducibility. The tradeoff is that copies can drift when a
script is fixed in one repo but the fix is not propagated.

The shared tooling sync mechanism solves this by establishing a single
canonical source (`standard-tooling`) and a sync script that detects and
fixes drift.

## Architecture

```text
standard-tooling (canonical source)
  └── scripts/
       ├── lint/          ← canonical lint scripts
       ├── git-hooks/     ← canonical git hooks
       └── dev/           ← canonical dev scripts (incl. sync-tooling.sh)

standard-actions
  ├── scripts/            ← synced from standard-tooling
  └── actions/standards-compliance/scripts/  ← also synced (--actions-compat)

standards-and-conventions
  └── scripts/            ← synced from standard-tooling

mq-rest-admin-{go,java,python}
  └── scripts/            ← synced from standard-tooling
```

Copies are the right model. Tagged releases must be self-contained so that
any supported release line can be built without external dependencies. The
sync mechanism keeps the develop branch up to date while preserving
self-containment on release branches.

## Managed scripts

### Git hooks (local-only)

| Script | Purpose |
| --- | --- |
| `scripts/git-hooks/commit-msg` | Conventional Commits + co-author validation |
| `scripts/git-hooks/pre-commit` | Branch naming enforcement |

### Lint scripts (hooks + CI)

| Script | Purpose |
| --- | --- |
| `scripts/lint/co-author.sh` | Co-author trailer validation |
| `scripts/lint/commit-message.sh` | Single commit message validation |
| `scripts/lint/commit-messages.sh` | Commit range validation (CI) |
| `scripts/lint/markdown-standards.sh` | Markdownlint + structural checks |
| `scripts/lint/pr-issue-linkage.sh` | PR body issue linkage validation |
| `scripts/lint/repo-profile.sh` | Repository profile validation |

### Dev scripts

| Script | Purpose |
| --- | --- |
| `scripts/dev/sync-tooling.sh` | The sync mechanism itself |
| `scripts/dev/prepare_release.py` | Automated release preparation |
| `scripts/dev/finalize_repo.sh` | Post-merge cleanup |

## Sync mechanism

Each consuming repo has a copy of `scripts/dev/sync-tooling.sh`. The script
compares local copies against the canonical versions in `standard-tooling`
and can auto-fix drift.

### Check mode (default)

```bash
scripts/dev/sync-tooling.sh --check
```

Compares each managed file against the canonical version. Exits non-zero if
any file is stale or missing. Used by the CI staleness gate.

### Fix mode

```bash
scripts/dev/sync-tooling.sh --fix
```

Overwrites local copies with canonical versions, preserving file
permissions. If `sync-tooling.sh` itself is stale, it updates itself first
and re-executes.

### Pinning to a tag

```bash
scripts/dev/sync-tooling.sh --fix --ref v1.0.0
```

By default the script syncs against the latest tag in `standard-tooling`.
Use `--ref` to pin to a specific version.

### Actions compatibility

```bash
scripts/dev/sync-tooling.sh --fix --actions-compat
```

For `standard-actions` only. Additionally syncs lint scripts to
`actions/standards-compliance/scripts/`.

## Staleness gate

The `standards-compliance` action in `standard-actions` includes a staleness
gate step that runs on PRs targeting `develop`. The step:

1. Checks if `scripts/dev/sync-tooling.sh` exists in the consuming repo
2. If present, runs `sync-tooling.sh --check`
3. If any managed files are stale, the gate fails

The gate is opt-in: repositories without `sync-tooling.sh` skip silently.
This enables incremental rollout.

The gate only runs on develop-targeted PRs. Release branches and hotfix
branches are not affected, preserving release stability.

## Handling staleness gate failures

When the staleness gate fails on a PR:

1. Run `scripts/dev/sync-tooling.sh --fix` locally
2. Review the changes (the updated files will appear in `git diff`)
3. Commit the updated scripts
4. Push to the PR branch

The gate will pass on the next CI run.

## Updating the canonical source

To fix or improve a shared script:

1. Make the change in `standard-tooling` on a feature branch
2. PR to develop, merge
3. Tag a new version (e.g., `v1.1.0`)
4. In each consuming repo, run `scripts/dev/sync-tooling.sh --fix`
5. The staleness gate will enforce the update on the next PR to develop

Do not fix shared scripts directly in consuming repos. Changes made in
consuming repos will be overwritten by the next sync.

## Adding a new managed script

1. Add the script to `standard-tooling`
2. Add its path to the `MANAGED_FILES` array in `sync-tooling.sh`
3. Tag a new version of `standard-tooling`
4. Run `sync-tooling.sh --fix` in each consuming repo

## Bootstrapping a new repository

1. Copy `scripts/dev/sync-tooling.sh` from `standard-tooling`
2. Run `scripts/dev/sync-tooling.sh --fix --ref v1.0.0`
3. Commit the synced scripts
4. The staleness gate is automatically active on the next PR to develop
