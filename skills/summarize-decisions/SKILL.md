---
name: summarize-decisions
description: Summarize discussions using the decisions protocol (wrapper for summarize mode=decisions).
---

# Summarize decisions

## Table of Contents
- [Purpose](#purpose)
- [Workflow](#workflow)
- [Output structure](#output-structure)
- [Resources](#resources)

## Purpose
Provide a decisions-focused summary using the canonical decisions protocol.

## Workflow
- Use the decisions protocol and do not add external facts.
- If the input is ambiguous or incomplete, call it out explicitly.
- Treat implicitly converged decisions as **implicit**.

## Output structure
Required order:
1. Results
2. Reasoning
3. Options Not Chosen

Include optional sections only when present in the input.

## Resources
- `skills/summarize/SKILL.md`
- `docs/foundation/summarize-decisions-protocol.md`
