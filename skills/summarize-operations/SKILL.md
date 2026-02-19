---
name: summarize-operations
description: Summarize operational work using the operations protocol (wrapper for summarize mode=operations).
---

# Summarize operations

## Table of Contents
- [Purpose](#purpose)
- [Workflow](#workflow)
- [Output structure](#output-structure)
- [Resources](#resources)

## Purpose
Provide an operations-focused summary using the canonical operations protocol.

## Workflow
- Use the operations protocol and do not add external facts.
- Capture evidence for command-driven actions when available.
- Include timestamps when available; state when none were provided.
- Redact sensitive data and note the redaction.

## Output structure
Required order:
1. Actions Taken
2. Outcomes and Status
3. Problems Encountered and Solved
4. Problems Unresolved
5. Changes and Artifacts
6. Follow-up Work and New Issues

## Resources
- `skills/summarize/SKILL.md`
- `docs/ai-agents/protocols/summarize-operations-protocol.md`
