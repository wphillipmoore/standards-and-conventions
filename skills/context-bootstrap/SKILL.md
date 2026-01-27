---
name: context-bootstrap
description: Bootstrap context by reading AGENTS and standards include chains and listing every file path read in order. Use when asked to bootstrap/startup context, load AGENTS/standards instructions, or show the ordered list of files read.
---

# Context Bootstrap

## Goal
Read the startup instruction chain, load each file’s contents as authoritative
context, and output the ordered file paths as they are encountered.

## Intent and constraints (non-negotiable)
- This is a fast, literal read-through. Treat it like reading a short bash script.
- The purpose is to bootstrap session context by consuming the ordered include chain.
- The explicit purpose is to ingest the full contents of each file as authoritative
  context. Skipping content or treating reads as no-ops is a hard failure.
- Rationale: this environment has no private ingestion channel; only command output
  becomes model context. If the contents are not printed, they are not ingested.
- Do not pause for planning, clarification, or optimization. Execute immediately.
- Do not run the script more than once.
- Use the script only to enumerate the ordered paths. After it completes,
  read each file in order to load its contents (no extra probing).
- Do not write or run any additional scripts, here-doc loops, or inline programs
  to process the path list. Use direct `cat <path>` invocations in order.
- Reading means emitting the full file contents to command output (for example, `cat`).
  Silent reads or partial reads (grep, head, tail) are invalid and must not be used.
- Do not emit any meta-commentary or planning lines (for example “Identifying…”, “Clarifying…”, “Planning…”).
- Use the provided script `scripts/context_bootstrap_paths.py` to resolve includes
  and emit an ordered list of paths only. Do not improvise alternate parsing or optimization.
- The file contents are authoritative once read. Apply all instructions unless a
  higher-priority system/developer rule conflicts.
- Failure to read the contents of every listed file is a hard error. Stop and
  report which file(s) were not read.
- The script reads local files only and expands includes recursively.
- `../standards-and-conventions/` must exist locally or the script fails.
- The script output (or missing path) is authoritative.
- If an include is missing, stop and report the missing path.

## Entry points
1. Read `~/AGENTS.md` if it exists.
2. Read `./AGENTS.md`.

## Script usage
Run exactly this command once (no pipes, no extra commands):
`python3 ~/.codex/skills/context-bootstrap/scripts/context_bootstrap_paths.py --repo-root <repo-root>`

Processing rules (exact):
1. Read the script output stream directly and check the script exit code. Do not re-run
   the script or invoke any other commands to filter or reformat the output.
2. If the script exits with code 0, for every line in the script output, read the file
   contents in order by printing the full file (use `cat` or an equivalent that emits
   the entire contents; do not probe, search, or suppress output).
   Use direct `cat <path>` commands; do not create wrapper scripts or loops.
3. After reading each file, output `Loaded: <path>` on its own line in the same order.
4. If the script exits with a nonzero code, output the script’s error line(s) verbatim and stop.
5. Do not add any other lines. No final summary block.

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

### Standards repo prefix handling
If a relative include path starts with `../standards-and-conventions/`:
1. Try it locally relative to the repo root.

## Output
- Output `Loaded: <path>` for each file path as it is encountered.
- Do not include file contents or reasons in the output.
