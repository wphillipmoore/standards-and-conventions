# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

<!-- include: docs/site/docs/standards-and-conventions.md -->
<!-- include: docs/repository-standards.md -->

<!-- include: skills/project-issue/SKILL.md -->
<!-- include: skills/branch-workflow/SKILL.md -->

## Project Overview

This is the **canonical standards and conventions repository**. All other repositories reference it as their baseline for development standards, workflows, and AI agent guidance.

**Status**: Active, authoritative

**Repository type**: Documentation-only. Do not add code unless it is an example explicitly required to explain a standard.

## Environment Setup

```bash
git config core.hooksPath ../standard-tooling/scripts/lib/git-hooks  # Enable git hooks
```

Standard-tooling CLI tools (`st-commit`, `st-validate-local`, etc.) are
pre-installed in the dev container images. No local setup required.

## Validation Commands

```bash
markdown-standards    # Markdown linting (canonical local validation command)
repo-profile          # Repository profile validation
```

## Development Environment

The `standard-tooling` package provides CLI tools (`st-commit`, `st-submit-pr`,
`st-finalize-repo`, etc.) used for commits, PRs, and post-merge cleanup. These
are pre-installed in all dev container images (`dev-python`, `dev-java`, etc.)
and are available on PATH automatically.

## Repository Standards Quick Reference

The include directives above load the full repository standards. Key highlights for quick reference:

**Pre-flight Checklist**:
- Check current branch: `git status -sb`
- If on `develop`, create `feature/*` branch before making changes
- Enable git hooks: `git config core.hooksPath ../standard-tooling/scripts/lib/git-hooks`
- Verify `st-*` tools are on PATH: `command -v st-commit`

**Repository Profile**:
- repository_type: documentation
- versioning_scheme: library
- branching_model: library-release
- release_model: artifact-publishing

**Branching**: `develop` is the default branch (staging). `main` is the promotion target (live site). All work happens on `feature/*` or `bugfix/*` branches merged to `develop` via PR. Changes reach `main` via promotion PR from `develop`.

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
- `scripts/dev/` - Development and validation scripts
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
- `skills/project-issue/` - Guided project issue creation with required attribute collection
- `skills/branch-workflow/` - Issue-linked branch creation with existing branch detection

## Working Rules

- Read the relevant standards before editing or adding documentation.
- Keep guidance generic; remove project-specific names, paths, or tooling.
- Preserve intent and rationale when generalizing standards.
- Update or create Tables of Contents per the Markdown standards.
- Prefer small, focused edits that keep documents easy to scan.
