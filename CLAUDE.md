# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Auto-memory policy

**Do NOT use MEMORY.md.** Claude Code's auto-memory feature stores behavioral
rules outside of version control, making them invisible to code review,
inconsistent across repos, and unreliable across sessions. All behavioral rules,
conventions, and workflow instructions belong in managed, version-controlled
documentation (CLAUDE.md, AGENTS.md, skills, or docs/).

If you identify a pattern, convention, or rule worth preserving:

1. **Stop.** Do not write to MEMORY.md.
2. **Discuss with the user** what you want to capture and why.
3. **Together, decide** the correct managed location (CLAUDE.md, a skill file,
   standards docs, or a new issue to track the gap).

This policy exists because MEMORY.md is per-directory and per-machine — it
creates divergent agent behavior across the multi-repo environment this project
operates in. Consistency requires all guidance to live in shared, reviewable
documentation.

## Documentation Strategy

This repository uses two complementary approaches for AI agent guidance:

- **AGENTS.md**: Generic AI agent instructions using include directives to force documentation indexing. Contains canonical standards references, shared skills loading, and user override support.
- **CLAUDE.md** (this file): Claude Code-specific guidance with prescriptive commands, architecture details, and development workflows optimized for `/init`.

### Integration Approach

**For Claude Code** (`/init` command):
1. Read CLAUDE.md (this file) first for optimized quick-start guidance
2. Process include directives to load repository standards
3. Reference AGENTS.md for shared skills and canonical standards location
4. Apply layered standards: canonical → project-specific → user overrides

**For other AI agents** (Codex, generic LLMs):
1. Read AGENTS.md first as the primary entry point
2. Process include directives to load all referenced documentation
3. Load shared skills from `skills/**/SKILL.md`
4. Apply user overrides from `~/AGENTS.md` if present

**Key differences**:
- **CLAUDE.md**: Prescriptive, command-focused, optimized for `/init`
- **AGENTS.md**: Declarative, include-directive-driven, forces full documentation indexing

Both files share the same underlying standards via include directives, ensuring consistency across all AI agents working in this repository.

### Best Practices for Dual-File Approach

**What goes in AGENTS.md**:
- Include directives for documentation indexing
- Canonical standards repository references
- Shared skills loading instructions
- User override mechanisms
- Minimal, declarative content

**What goes in CLAUDE.md**:
- Claude Code-specific quick-start commands
- Detailed architecture and design patterns
- Implementation notes and common workflows
- Integration guidance between the two files
- More verbose, prescriptive content

**What goes in neither (use includes instead)**:
- Repository standards (keep in `docs/repository-standards.md`)
- Canonical standards (keep in `docs/site/docs/standards-and-conventions.md`)
- Project-specific conventions (keep in referenced docs)

**Maintenance strategy**:
- Update standards in source files, not in AGENTS.md or CLAUDE.md
- Use include directives to pull in shared content
- Keep AGENTS.md minimal and CLAUDE.md focused on Claude Code workflows
- Test both entry points when updating documentation structure

<!-- include: docs/site/docs/standards-and-conventions.md -->
<!-- include: docs/repository-standards.md -->

## Always-Loaded Skills

These skills are loaded at session start so they're immediately available without explicit invocation. When a user provides skill attributes inline (e.g., "create a P0 enhancement for X"), skip the corresponding interactive questions and go straight to confirm-and-create.

<!-- include: skills/new-issue/SKILL.md -->

## Project Overview

This is the **canonical standards and conventions repository**. All other repositories reference it as their baseline for development standards, workflows, and AI agent guidance.

**Status**: Active, authoritative

**Repository type**: Documentation-only. Do not add code unless it is an example explicitly required to explain a standard.

## Validation Commands

```bash
# Markdown linting (canonical local validation command)
scripts/lint/markdown-standards.sh

# Repository profile validation
scripts/lint/repo-profile.sh

# Commit message validation
scripts/lint/commit-messages.sh
```

Git hooks enforce branch naming and commit message standards. Enable them:

```bash
git config core.hooksPath scripts/git-hooks
```

## Repository Standards Quick Reference

The include directives above load the full repository standards. Key highlights for quick reference:

**Pre-flight Checklist**:
- Check current branch: `git status -sb`
- If on `develop`, create `feature/*` branch before making changes
- Enable git hooks: `git config core.hooksPath scripts/git-hooks`

**Repository Profile**:
- repository_type: documentation
- versioning_scheme: library
- branching_model: library-release
- release_model: artifact-publishing

**Branching**: `develop` is the default branch (staging). `main` is the promotion target (live site). All work happens on `feature/*` or `bugfix/*` branches merged to `develop` via PR. Changes reach `main` via promotion PR from `develop`.

**Docs-only exception**: Since this is a documentation-only repository, the docs-only exception applies to all PRs. Local validation is optional per the docs-only rule.

**Validation**: markdownlint is the canonical local validation tool. It must be on PATH (`markdownlint-cli`).

## File Layout

- `docs/site/` - MkDocs documentation site
  - `docs/site/docs/standards/` - Authoring standards (markdown, architecture)
  - `docs/site/docs/ai-agents/` - AI agent behavior, workflows, quality, and protocols
  - `docs/site/docs/code-management/` - Branching, commits, PRs, versioning, releases
  - `docs/site/docs/repository/` - Repository structure, types, dependencies, and shared tooling
  - `docs/site/docs/development/` - Language-specific development standards (Python, database)
  - `docs/site/docs/research/` - Research reports
- `skills/` - Shared agent skills loaded by downstream repositories
- `scripts/` - Linting, git hook, and dev automation scripts
  - `scripts/dev/` - Shared development scripts (prepare_release, finalize_repo)
- `drafts/` - Work-in-progress content

## Skills

This repository hosts shared skills that downstream repositories load:

- `skills/dependency-update/` - Dependency update workflow
- `skills/deprecation-triage/` - Deprecation warning triage
- `skills/summarize/` - Multi-mode summarization
- `skills/summarize-decisions/` - Decision summarization
- `skills/summarize-operations/` - Operations summarization
- `skills/summarize-soc/` - Stream-of-consciousness capture
- `skills/publish/` - Library and documentation publish workflow
- `skills/pr-workflow/` - Pull request workflow
- `skills/rtfm/` - RTFM forced interruption handling
- `skills/new-issue/` - Guided issue creation with required attribute collection

## Working Rules

- Read the relevant standards before editing or adding documentation.
- Keep guidance generic; remove project-specific names, paths, or tooling.
- Preserve intent and rationale when generalizing standards.
- Update or create Tables of Contents per the Markdown standards.
- Prefer small, focused edits that keep documents easy to scan.

## Multi-Line Messages

When creating multi-line commit messages or pull request bodies, prefer using temporary files instead of shell heredocs in command substitution. This avoids shell escaping issues and preserves exact formatting.

## Documentation Indexing Strategy

This repository uses `<!-- include: path/to/file.md -->` directives to force documentation indexing. When you encounter these directives:

1. **Read the referenced files** to understand the full context
2. **Apply layered standards** in order:
   - Canonical standards (the documents in this repository)
   - Project-specific standards (`docs/repository-standards.md`)
   - User overrides (`~/AGENTS.md` if present)
3. **Load shared skills** from `skills/**/SKILL.md`

## Commit and PR Scripts

**NEVER use raw `git commit`** — always use `scripts/dev/commit.sh`.
**NEVER use raw `gh pr create`** — always use `scripts/dev/submit-pr.sh`.

### Committing

```bash
scripts/dev/commit.sh --type docs --message "update branching standards" --agent claude
scripts/dev/commit.sh --type feat --scope skills --message "add new triage skill" --agent claude
scripts/dev/commit.sh --type fix --message "correct markdown lint config" --body "Aligned with upstream markdownlint-cli2 defaults" --agent claude
```

- `--type` (required): `feat|fix|docs|style|refactor|test|chore|ci|build`
- `--message` (required): commit description
- `--agent` (required): `claude` or `codex` — resolves the correct `Co-Authored-By` identity
- `--scope` (optional): conventional commit scope
- `--body` (optional): detailed commit body

### Submitting PRs

```bash
scripts/dev/submit-pr.sh --issue 42 --summary "Update branching model standards"
scripts/dev/submit-pr.sh --issue 42 --linkage Ref --summary "Clarify AI agent guidelines" --docs-only
scripts/dev/submit-pr.sh --issue 42 --summary "Add deprecation triage skill" --notes "New skill loaded by downstream repos"
```

- `--issue` (required): GitHub issue number (just the number, or cross-repo `owner/repo#42`)
- `--summary` (required): one-line PR summary
- `--linkage` (optional, default: `Fixes`): `Fixes|Closes|Resolves|Ref`
- `--title` (optional): PR title (default: most recent commit subject)
- `--notes` (optional): additional notes
- `--docs-only` (optional): applies docs-only testing exception
- `--dry-run` (optional): print generated PR without executing

## Key References

**This repository IS the canonical standards source.** Unlike downstream repos that reference it externally, standards here are authoritative and local.

**User Overrides**: `~/AGENTS.md` (optional, applied if present and readable)
