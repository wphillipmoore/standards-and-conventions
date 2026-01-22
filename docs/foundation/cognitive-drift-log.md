# Cognitive drift log

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Template](#template)
- [Prompt shortcuts](#prompt-shortcuts)

## Purpose
Provide a minimal log template for recording concerning or hard failures.

## Scope
Use when a response or behavior violates the interaction contract.

## Template
```
Date:
Context:
Prompt:
Observed failure:
Category (A–F):
Severity (Soft / Hard):
Correction applied:
```

## Prompt shortcuts
Use a standalone prompt that invokes the log, such as:
- `Log cognitive drift`

Date: 2026-01-22
Context: Replacing the repository's `skills/context-bootstrap` with the home directory copy after unexpected changes were detected.
Prompt: "Please import the context-bootstrap skill from my home dir into this repo for reference, replacing the current one entirely -- again"
Observed failure: Proceeded with the file copy instead of stopping immediately to ask how to handle unexpected changes.
Category (A–F): F
Severity (Soft / Hard): Hard
Correction applied: Stop on unexpected changes and ask how to proceed before any further action.
