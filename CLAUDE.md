# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Auto-memory policy

**Do NOT use MEMORY.md.** Never write to MEMORY.md or any file under the
memory directory. All behavioral rules, conventions, and workflow instructions
belong in managed, version-controlled documentation (CLAUDE.md, AGENTS.md,
skills, or docs/). If you want to persist something, tell the human what you
would save and let them decide where it belongs.

## Parallel AI agent development

This repository supports running multiple Claude Code agents in parallel via
git worktrees. The convention keeps parallel agents' working trees isolated
while preserving shared project memory (which Claude Code derives from the
session's starting CWD).

**Canonical spec:**
[`standard-tooling/docs/specs/worktree-convention.md`](https://github.com/wphillipmoore/standard-tooling/blob/develop/docs/specs/worktree-convention.md)
— full rationale, trust model, failure modes, and memory-path implications.
The canonical text lives in `standard-tooling`; this section is the local
on-ramp. (A generalized write-up in this repo is Phase 4 of the rollout
plan and will land as a follow-up.)

### Structure

```text
~/dev/github/standards-and-conventions/     ← sessions ALWAYS start here
  .git/
  CLAUDE.md, docs/, skills/, …              ← main worktree (usually `develop`)
  .worktrees/                               ← container for parallel worktrees
    issue-353-adopt-worktree-convention/    ← worktree on feature/353-...
    …
```

### Rules

1. **Sessions always start at the project root.**
   `cd ~/dev/github/standards-and-conventions && claude` — never from inside
   `.worktrees/<name>/`. This keeps the memory-path slug stable and shared.
2. **Each parallel agent is assigned exactly one worktree.** The session
   prompt names the worktree (see Agent prompt contract below).
   - For Read / Edit / Write tools: use the worktree's absolute path.
   - For Bash commands that touch files: `cd` into the worktree first,
     or use absolute paths.
3. **The main worktree is read-only.** All edits flow through a worktree
   on a feature branch — the logical endpoint of the standing
   "no direct commits to `develop`" policy.
4. **One worktree per issue.** Don't stack in-flight issues. When a
   branch lands, remove the worktree before starting the next.
5. **Naming: `issue-<N>-<short-slug>`.** `<N>` is the GitHub issue
   number; `<short-slug>` is 2–4 kebab-case tokens.

### Agent prompt contract

When launching a parallel-agent session, use this template (fill in the
placeholders):

```text
You are working on issue #<N>: <issue title>.

Your worktree is: /Users/pmoore/dev/github/standards-and-conventions/.worktrees/issue-<N>-<slug>/
Your branch is:   feature/<N>-<slug>

Rules for this session:
- Do all git operations from inside your worktree:
    cd <absolute-worktree-path> && git <command>
- For Read / Edit / Write tools, use the absolute worktree path.
- For Bash commands that touch files, cd into the worktree first
  or use absolute paths.
- Do not edit files at the project root. The main worktree is
  read-only — all changes flow through your worktree on your
  feature branch.
```

All fields are required.

## Project Overview

This is the **canonical standards and conventions repository**. All other repositories reference it as their baseline for development standards, workflows, and AI agent guidance.

**Status**: Active, authoritative

**Repository type**: Documentation-only. Do not add code unless it is an example explicitly required to explain a standard.

## Environment Setup

```bash
git config core.hooksPath .githooks  # Enable git hooks
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

Key highlights for quick reference:

**Pre-flight Checklist**:
- Check current branch: `git status -sb`
- If on `develop`, create `feature/*` branch before making changes
- Enable git hooks: `git config core.hooksPath .githooks`
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
