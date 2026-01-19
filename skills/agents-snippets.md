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
- Load all skills from: <standards-repo-path>/skills/**/SKILL.md
- Treat every skill found under that directory as available and active.
```

## Notes
- This avoids per-skill updates in downstream `AGENTS.md` files.
- Do not duplicate skill contents in downstream repositories.
