---
name: context-bootstrap
description: Bootstrap context by reading AGENTS and standards include chains and listing every file path read in order. Use when asked to bootstrap/startup context, load AGENTS/standards instructions, or show the ordered list of files read.
---

# Context Bootstrap

## Goal
Read the startup instruction chain and report only the ordered list of file paths read.

## Entry points
1. Read `~/AGENTS.md` if it exists.
2. Read `./AGENTS.md`.

## Include syntax
- Include lines must start with `#include` followed by a path.
- Accepted forms:
  - `#include path`
  - `#include "path"`
  - `#include <path>`
- Paths are treated as literal strings after stripping optional quotes or angle brackets.

## Include resolution (no inference)
- Track files in the order read and do not re-read the same path to avoid loops.
- Resolve includes using the search path below. First match wins; stop on missing includes.
- Absolute paths (including `~`) are read directly with no search.

### Search path (relative includes)
Resolve relative include paths in this order, using the repo root (the cwd at bootstrap) as the base:
1. `./` (repo root)
2. `../standards-and-conventions/`
3. `https://raw.githubusercontent.com/wphillipmoore/standards-and-conventions/develop/`

### Standards repo prefix handling
If a relative include path starts with `../standards-and-conventions/`:
1. Try it locally relative to the repo root.
2. If not found, strip the prefix and retry via the GitHub base URL.

## Output
- After completing all required reads, print the ordered list of file paths (or URLs) read, one per line.
- The list must be the final output before returning control to the user.
- Do not include file contents or reasons in the final list.
