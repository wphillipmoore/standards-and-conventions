# Source Code Management Guidelines

## Status

Active v0.2

---

## 1. AI Assistance (Explicitly Bounded)

Constraints:

- AI-generated code must be reviewed with the same rigor as external
  contributions.
- AI assistance must never become a silent dependency.
- The codebase must remain understandable, auditable, and maintainable without
  AI.

Invariant:
Code correctness, determinism, and maintainability override speed or
convenience.

---

## 2. Version Control Platform

Git is the source control system.

GitHub is the initial central repository host, including GitHub Actions for
CI/CD.

This decision is explicitly provisional, not foundational.

### Lock-In Awareness

GitHub-specific dependencies must be:

- understood
- tracked
- periodically reassessed

The project must retain enough knowledge to evaluate the cost and feasibility
of migration to an alternative host if required.

Migration readiness is not required at v0.1, but migration awareness is.

---

## 3. Repository Strategy

### Core Philosophy

Repositories should be:

- small
- modular
- scoped to a single semantic responsibility

Independent components should live in separate repositories by default.

### Boundary Rule

Repository boundaries follow semantic ownership and lifecycle, not convenience.

This improves:

- independent evolution
- reduced cognitive load
- long-term maintainability
- survivability without original authorship

### Explicit Non-Decision

Monorepo vs. multirepo strategy is not locked at v0.1.

This decision may be revisited once:

- dependency graphs stabilize
- tooling friction is observed
- CI/CD cost and complexity are measurable

---

## 4. Runtime Version Policy

For tier definitions, CI matrix classification, and drop criteria, see the
[Runtime Version Support Policy](../development/runtime-version-support-policy.md).

### Deployment Rule

Production deployments use the current stable runtime version.

Invariant:
Code that cannot survive the next runtime release without heroics is already
technical debt.

---

## 5. CI/CD Constraints

CI/CD pipelines must be:

- deterministic
- stateless
- reproducible locally

Automation should avoid reliance on opaque or irreducibly platform-specific
behavior.

CI configuration must remain:

- readable
- minimal
- replaceable

Prefer a shared actions library for reusable workflow logic and pin action
references by tag or commit SHA.

Anti-goal:
Clever automation that cannot be reasonably expressed outside the current CI
provider.

### CI gates

Every CI check must be classified as either a hard gate or a soft gate.

- Hard gate: blocking. A failing check prevents PR submission and merge.
- Soft gate: warning-only. A failing check does not block merge, but must be
  surfaced in the PR with rationale and any follow-up tracking.

Each repository must explicitly list its checks and their gate type. If a
check is not classified, treat it as a hard gate until documented.

Hard gates must be enforced as required status checks on the target branches
so failing GitHub Actions block PR merges.

Each repository must also document which hard gates apply per branch. Some
hard gates may be develop-only, while others must run on all eternal branches.

#### SonarQube Cloud (soft gate, limited beta)

SonarQube Cloud (SonarCloud) provides cross-language static analysis for code
quality, security vulnerabilities, and maintainability. It is currently deployed
as an **optional, advisory soft gate** in limited beta on the mq-rest-admin
language implementation repos (Python, Go, Java).

SonarCloud's free tier does not support custom quality gates, so the integration
provides informational analysis rather than enforcement. Language-specific
tooling (ruff, mypy, golangci-lint, spotbugs, etc.) remains the primary
enforcement mechanism and the hard gate for code quality.

SonarCloud runs in two patterns per repository:

- **PR analysis** — a `sonarcloud` job in `ci.yml` posts a quality gate comment
  on each pull request.
- **Post-merge baseline** — a dedicated `sonarcloud.yml` workflow triggered on
  `push` to `develop` keeps the SonarCloud project dashboard current.

SonarCloud is not a required status check on any branch. It must not block PR
merges. The composite action is defined in the
[standard-actions](https://github.com/wphillipmoore/standard-actions) shared
actions library at `actions/quality/sonarcloud`.

#### Qlty Cloud (soft gate, limited beta)

Qlty Cloud (formerly Code Climate) provides coverage tracking, trend analysis,
and PR coverage comments. It is currently deployed as an **optional, advisory
soft gate** in limited beta on the mq-rest-admin language implementation repos
(Python, Go, Java).

Qlty Cloud's free tier provides 500 analysis minutes per month for open-source
projects. Language-specific tooling remains the primary enforcement mechanism for
coverage thresholds.

Qlty Cloud runs in two patterns per repository:

- **PR analysis** — a `codeclimate` job in `ci.yml` uploads coverage and posts a
  coverage comment on each pull request.
- **Post-merge baseline** — a dedicated `codeclimate.yml` workflow triggered on
  `push` to `develop` keeps the Qlty Cloud dashboard current.

Qlty Cloud uses OIDC authentication — no tokens or secrets are required. The
calling workflow must include `id-token: write` in its permissions block.

Qlty Cloud is not a required status check on any branch. It must not block PR
merges. The composite action is defined in the
[standard-actions](https://github.com/wphillipmoore/standard-actions) shared
actions library at `actions/quality/codeclimate`.

### Docs-only CI skip policy

Repositories must define a docs-only allowlist (for example, `docs/**`,
`README.md`, and `CHANGELOG.md`). `.github/**` is not docs-only.

CI workflows must include a docs-only detection job that computes
`docs_only=true|false` based on the PR diff against the allowlist and exposes it
as a workflow output.

When `docs_only` is `true`, skip test and version-validation jobs by gating
them with the docs-only output. Dependency audits should still run by default;
if a repository chooses to skip them, it must document the exception.

Markdownlint and any docs-only validation commands must still run.

### Local enforcement hooks

Use local Git hooks to fail closed on branch protection and naming rules that
should never be violated.

Store hooks in-repo at `scripts/git-hooks/` and set `core.hooksPath` locally:

```bash
git config core.hooksPath scripts/git-hooks
```

Hooks must print a clear, actionable error and exit non-zero on violations.

#### pre-commit hook

The `pre-commit` hook enforces two rules in order:

1. **Protected branch block** — commits to `develop`, `release`, and `main`
   are rejected unconditionally (detached HEAD is also blocked).
2. **Branch prefix validation** — the hook reads `branching_model` from
   `docs/repository-standards.md` and allows only the prefixes defined for
   that model:

| `branching_model` | Allowed prefixes |
| --- | --- |
| `docs-promotion` | `feature/*`, `bugfix/*` |
| `application-promotion` | `feature/*`, `bugfix/*`, `hotfix/*`, `promotion/*` |
| `library-release` | `feature/*`, `bugfix/*`, `hotfix/*`, `release/*` |

If `branching_model` is missing, the hook warns and falls back to the most
restrictive set (`feature/*`, `bugfix/*`). If `branching_model` is
unrecognized, the hook exits with a hard error.

The canonical implementation is `scripts/git-hooks/pre-commit`.

#### commit-msg hook

The `commit-msg` hook runs two validations:

1. **Commit message lint** (`scripts/lint/commit-message.sh`) — enforces
   Conventional Commits format.
2. **Co-author trailer validation** (`scripts/lint/co-author.sh`) — if any
   `Co-Authored-By:` trailers are present, each must match an approved
   identity listed in `docs/repository-standards.md`. Human-only commits
   (no trailers) pass unconditionally.

The canonical implementation is `scripts/git-hooks/commit-msg`.

---

## 6. GitHub Repository Settings

The following settings are required defaults for all repositories hosted on
GitHub.

### Automatically delete head branches

**Setting**: Enabled

Under **Settings → General → Pull Requests**, enable **Automatically delete
head branches**.

This ensures merged branches are removed immediately after merge across all
merge paths — web UI, API, and CLI — providing a safety net that complements
the `--delete-branch` flag used during CLI-based PR submission and the manual
cleanup performed during PR finalization.

PR finalization steps and CLI commands should still request branch deletion
explicitly. The repository-level setting acts as defense in depth, not a
replacement for explicit cleanup.

### GitHub repository rulesets

All repositories must use GitHub rulesets for branch and tag protection.
Rulesets replace legacy branch protection rules. Legacy branch protection must
not be used on any repository.

**Enforce-admins-ON**: Every ruleset must have an empty `bypass_actors` list.
This means ruleset enforcement applies to all users including repository
administrators. There is no escape hatch for admins.

**Library repositories** require three rulesets:

1. **Branch protection** (targets: `main`, `develop`)
   - Prevent branch deletion
   - Prevent force push
   - Require pull requests (0 approvals, dismiss stale reviews)

2. **CI gates** (targets: `main`, `develop`)
   - Require status checks to pass before merging (`strict` mode)
   - Required checks are repo-specific and must match the CI job names defined
     in the repository's workflow files

3. **Tag protection** (targets: `v*`)
   - Prevent tag deletion
   - Prevent force-updating tags
   - Prevent modifying existing tags
   - No creation restriction (the publish workflow creates tags)

**Documentation repositories** require two rulesets:

1. **Branch protection** (targets: eternal branches only)
   - Same rules as library repositories

2. **CI gates** (targets: eternal branches only)
   - Required checks are repo-specific

Rulesets are managed via the GitHub API or the repository settings UI. When
creating or updating rulesets, verify the configuration by checking an open PR
on the target repository to confirm the expected required checks appear.

---

## 7. Locked vs. Flexible Decisions

### Locked at v0.1

- Git as the source control system
- GitHub as the initial hosting provider
- GitHub Actions for CI/CD
- Runtime validation on the current stable version

### Explicitly Flexible

- Repository granularity and structure
- CI/CD provider choice
- Deployment orchestration details
- Degree and style of AI-assisted development

---

## 8. Guiding Principle

All source code management decisions are evaluated against a single overriding
criterion:

The system must survive without its original author.

Tooling, structure, and process choices are judged by their contribution to
long-term clarity, auditability, and evolutionary capacity.
