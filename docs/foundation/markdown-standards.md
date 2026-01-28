# Markdown Standards

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [File Naming and Placement](#file-naming-and-placement)
- [Structure and Headings](#structure-and-headings)
- [Table of Contents Rules](#table-of-contents-rules)
- [Formatting Conventions](#formatting-conventions)
- [Links and References](#links-and-references)
- [Code Blocks](#code-blocks)
- [Validation](#validation)
- [Maintenance](#maintenance)

## Purpose
Define consistent Markdown conventions for clarity, durability, and easy
navigation across all documentation in this repository.

## Scope
These standards apply to all documentation Markdown files in this repository.
AI tooling instruction files (such as `AGENTS.md`) are exempt unless they
explicitly state otherwise.

## File Naming and Placement
- Place documentation files under `docs/` unless a top-level file is required.
- Use descriptive, stable filenames in `kebab-case.md`.
- Avoid renaming files without a compelling reason.

## Structure and Headings
- Use a single H1 title (`#`) at the top of the file.
- Use ATX headings (`##`, `###`) only; do not use Setext headings.
- Keep heading titles short, specific, and in sentence case.
- Avoid skipping heading levels (no `####` under `##`).

## Table of Contents Rules
- Include a `## Table of Contents` section near the top of every document.
- Place it after the title and any brief preface block.
- List all `##` and `###` headings in order, excluding the Table of Contents.
- Use a bullet list with two-space indentation for `###` entries.
- Use GitHub-style anchor links.

## Formatting Conventions
- Use blank lines around headings and lists.
- Prefer short paragraphs and bullets over dense blocks of text.
- Use bold only for short emphasis; avoid bolding entire sentences.
- Use italics sparingly for terms or titles, not emphasis.
- Avoid emojis unless explicitly required.

## Links and References
- Prefer relative links for repository content.
- Keep link text descriptive; avoid "click here."
- When referencing file paths in prose, use backticks.

## Code Blocks
- Use fenced code blocks with a language tag when possible.
- Keep code examples minimal and focused on the rule being explained.
- Do not include output that is environment-specific unless required.

## Validation
- All repositories must run markdownlint for documentation validation.
- Markdownlint is the minimum baseline. Repositories may add additional checks.
- Code repositories must document language-specific and repo-specific validation
  commands in their repository standards.

## Maintenance
- Update the Table of Contents when headings change.
- Keep documents current; stale guidance should be revised or removed.
