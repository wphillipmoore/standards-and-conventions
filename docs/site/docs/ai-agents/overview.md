# AI Agents Overview

## Purpose

Provide a single entry point for AI agent behavior, workflows, quality
controls, and summary protocols.

## Scope

These documents define expectations for AI-assisted development across
repositories. They cover agent guardrails, interaction contracts, cognitive
quality tracking, and structured summarization protocols.

## Document Map

### Behavior

- Agent guardrails: [behavior/agent-guardrails.md](behavior/agent-guardrails.md)
- Agent pre-response checklist: [behavior/agent-pre-response-checklist.md](behavior/agent-pre-response-checklist.md)
- Agent boot banner: [behavior/agent-boot-banner.md](behavior/agent-boot-banner.md)
- Agent skills: [behavior/agent-skills.md](behavior/agent-skills.md)

### Workflows

- AI-assisted development loop: [workflows/ai-assisted-development-loop.md](workflows/ai-assisted-development-loop.md)
- AI code review guidelines: [workflows/ai-code-review-guidelines.md](workflows/ai-code-review-guidelines.md)
- Standards bootstrap protocol: [workflows/standards-bootstrap-protocol.md](workflows/standards-bootstrap-protocol.md)
- Interaction contract: [workflows/interaction-contract.md](workflows/interaction-contract.md)

### Quality

- Cognitive drift log: [quality/cognitive-drift-log.md](quality/cognitive-drift-log.md)
- Cognitive regression tests: [quality/cognitive-regression-tests.md](quality/cognitive-regression-tests.md)
- Interaction contract brief: [quality/interaction-contract-brief.md](quality/interaction-contract-brief.md)

### Protocols

- Summarize decisions protocol: [protocols/summarize-decisions-protocol.md](protocols/summarize-decisions-protocol.md)
- Summarize operations protocol: [protocols/summarize-operations-protocol.md](protocols/summarize-operations-protocol.md)
- Summarize stream of consciousness protocol: [protocols/summarize-stream-of-consciousness-protocol.md](protocols/summarize-stream-of-consciousness-protocol.md)

## When to use each summary protocol

- Summarize stream of consciousness protocol: Use when capturing raw ideas in a
  toggleable capture window, then organizing them after `End SOC`.
- Summarize decisions protocol: Use for discussions where the primary outcome
  is a decision and the reasoning and alternatives must be preserved.
- Summarize operations protocol: Use for operational work where actions,
  evidence, outcomes, and follow-up work must be recorded.
