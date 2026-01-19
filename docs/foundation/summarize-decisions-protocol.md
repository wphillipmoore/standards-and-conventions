# Summarize decisions protocol

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Definitions](#definitions)
- [Prompt shortcuts](#prompt-shortcuts)
- [Input rules](#input-rules)
- [Output structure](#output-structure)
- [Section requirements](#section-requirements)
- [Implicitly converged decisions](#implicitly-converged-decisions)
- [Optional sections](#optional-sections)
- [Style and fidelity rules](#style-and-fidelity-rules)
- [Failure modes](#failure-modes)

## Purpose
Define how to summarize a discussion into durable documentation that preserves
decisions, reasoning, and alternatives.

## Scope
Use this protocol for discussions intended for archival decision records.

## Definitions
- Decision summary: the structured output produced by this protocol.
- Input record: the chat or discussion content provided for summarization.

## Prompt shortcuts
Use a standalone prompt that invokes the protocol, such as:
- `Summarize decisions`
- `Decision summary`

## Input rules
- Summaries MUST be based only on the input record.
- External knowledge, assumptions, or inferred facts MUST NOT be added.
- Missing or ambiguous information MUST be called out explicitly.

## Output structure
The summary MUST follow this order:
1. Results
2. Reasoning
3. Options not chosen

Additional sections MAY follow if they add clarity, but the order above MUST be
preserved.

## Section requirements
Results MUST include:
- Decisions made
- Deliverables or outputs agreed upon
- Action items, with owners or roles if stated
- Open decisions explicitly flagged as unresolved

If no decisions were reached, Results MUST say so.

Reasoning MUST include:
- Key constraints or requirements
- Assumptions that materially affect outcomes
- Tradeoffs discussed and how they were resolved
- Evidence or data cited
- Uncertainties acknowledged

If reasoning is incomplete or implicit, the summary MUST state that.

Options not chosen MUST include:
- Option description
- Reasons it was not chosen
- Status as rejected or deferred
- Revisit triggers or conditions, if stated

If no alternatives were discussed, Options not chosen MUST say so.

## Implicitly converged decisions
Outcomes that are not explicitly declared but are clearly settled MAY be
recorded as decisions only when:
- The outcome is consistently supported by the Reasoning section.
- No competing option remains actively defended.
- Subsequent actions or conclusions depend on the outcome.

Such outcomes MUST be labeled as implicit or implicitly converged. If support
is weak or ambiguous, record them as open questions instead.

## Optional sections
Include only when discussed:
- Risks and failure modes
- Open questions
- Dependencies or external constraints
- Follow-up checkpoints or revisit triggers
- References to artifacts (files, commands, documents)

## Style and fidelity rules
- The summary MUST be concise, structured, and non-narrative.
- The summary MUST NOT introduce new decisions, claims, or rationales.
- Ordering SHOULD mirror the original discussion when sequence matters.
- The summary MUST distinguish facts from opinions or proposals.

## Failure modes
- If the input record is missing or incomplete, the summary MUST note the gaps.
- If results cannot be determined, the summary MUST say so explicitly.
