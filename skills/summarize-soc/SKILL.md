---
name: summarize-soc
description: Capture and summarize stream-of-consciousness input using the SOC protocol (wrapper for summarize mode=soc).
---

# Summarize SOC

## Table of Contents
- [Purpose](#purpose)
- [Workflow](#workflow)
- [Output structure](#output-structure)
- [Resources](#resources)

## Purpose
Provide a stream-of-consciousness capture and summary using the canonical SOC
protocol.

## Workflow
- `Enter SOC` starts capture mode and must be acknowledged.
- During capture, record input verbatim and do not interpret.
- `End SOC` ends capture and triggers the structured summary.
- If capture is never closed, do not summarize.

## Output structure
Required sections:
- Summary
- Themes
- Open Questions

Include optional sections only when present in the input.

## Resources
- `skills/summarize/SKILL.md`
- `docs/foundation/summarize-stream-of-consciousness-protocol.md`
