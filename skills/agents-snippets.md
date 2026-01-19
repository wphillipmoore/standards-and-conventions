# AGENTS.md snippets for shared skills

## Table of Contents
- [Purpose](#purpose)
- [Snippet](#snippet)
- [Notes](#notes)

## Purpose
Provide a reusable snippet that downstream repositories can copy into their
`AGENTS.md` to reference these shared skills.

## Snippet
Replace `<standards-repo-path>` with the local path to the cloned standards
repository.

```
## Shared skills
- summarize: <standards-repo-path>/skills/summarize/SKILL.md
- pr-workflow: <standards-repo-path>/skills/pr-workflow/SKILL.md
- dependency-update: <standards-repo-path>/skills/dependency-update/SKILL.md
- deprecation-triage: <standards-repo-path>/skills/deprecation-triage/SKILL.md
```

## Notes
- Keep this list in sync with `skills/README.md`.
- Do not duplicate skill contents in downstream repositories.
