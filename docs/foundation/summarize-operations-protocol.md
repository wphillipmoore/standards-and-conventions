# Summarize operations protocol

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Definitions](#definitions)
- [Prompt shortcuts](#prompt-shortcuts)
- [Input rules](#input-rules)
- [Output location and naming](#output-location-and-naming)
- [Output structure](#output-structure)
- [Section requirements](#section-requirements)
- [Evidence capture rules](#evidence-capture-rules)
- [Timestamp requirements](#timestamp-requirements)
- [Optional sections](#optional-sections)
- [Style and fidelity rules](#style-and-fidelity-rules)
- [Failure modes](#failure-modes)

## Purpose

Define how to summarize operational work into durable documentation that
preserves actions, outcomes, problems, and follow-up work.

## Scope

Use this protocol for chats that perform operational procedures or system
changes.

## Definitions

- Operations summary: the structured output produced by this protocol.
- Input record: the chat or discussion content provided for summarization.
- Operational action: an action that changes system state or verifies it.

## Prompt shortcuts

Use a standalone prompt that invokes the protocol, such as:

- `Summarize operations`
- `Ops summary`

## Input rules

- Summaries MUST be based only on the input record.
- External knowledge, assumptions, or inferred facts MUST NOT be added.
- Missing or ambiguous information MUST be called out explicitly.
- Secrets, credentials, and sensitive data MUST NOT be reproduced. If present,
  the summary MUST note that sensitive data was redacted.

## Output location and naming

When a repository or storage context exists, write the summary to the
designated operations summary location and name the file with a UTC timestamp
and short, lowercase, ASCII, kebab-case slug.

If no storage context exists, provide the summary directly in the response and
note that no file was written.

## Output structure

The summary MUST follow this order:

1. Actions taken
2. Outcomes and status
3. Problems encountered and solved
4. Problems unresolved
5. Changes and artifacts
6. Follow-up work and new issues

Additional sections MAY follow if they add clarity, but the order above MUST be
preserved.

## Section requirements

Actions taken MUST:

- List actions in the order performed.
- Use clear, atomic statements in past tense.
- Include timestamps when available.
- Capture target systems, tools or commands used, and relevant parameter or
  configuration changes.

If no actions were taken, the summary MUST say so.

Outcomes and status MUST:

- State whether each action succeeded, failed, or is unknown.
- Cite evidence from the input record (logs, tests, command output) when
  available.
- Describe resulting system state when it can be determined.

If success or failure is unclear, the summary MUST say it is unknown.

Problems encountered and solved MUST include:

- Symptoms or error messages
- Root cause, if identified
- Fix applied

If none were encountered or solved, the summary MUST say so.

Problems unresolved is REQUIRED even if empty. It MUST include:

- Current symptoms or failure mode
- Impact or risk, if known
- Attempts that failed
- Blockers or missing information

If no unresolved problems remain, the summary MUST say so explicitly.

Changes and artifacts MUST include:

- Created, modified, or deleted resources
- Configuration changes
- Files or repositories changed
- Scripts run or commands executed when they materially change state

If no changes were made, the summary MUST say so.

Follow-up work and new issues MUST include:

- Remaining steps or tasks
- New issues discovered
- Owners or roles if stated
- Urgency or deadlines if stated

If none exist, the summary MUST say so.

## Evidence capture rules

Operational summaries MUST include evidence for command-driven actions.
At minimum, include:

- The exact commands executed (flags and arguments included)
- The relevant output that demonstrates success or failure

Because output can be large, summaries MUST:

- Include the smallest output snippet that proves the outcome.
- Omit repetitive or verbose output unless it is the only evidence.
- State when output is truncated and why.
- State explicitly when no output was captured.

Commands and outputs MUST NOT include secrets or credentials. If sensitive
output exists, the summary MUST note that it was redacted.

## Timestamp requirements

Summaries MUST capture available timestamps for:

- Actions or grouped actions
- Key outcomes or errors
- Time zone or offset if known

If only relative timing is available, include it and note the lack of absolute
time. If no timestamps are provided, the summary MUST say so.

## Optional sections

Include only when discussed:

- Verification or monitoring steps
- Rollback or recovery notes
- Risks and failure modes
- Dependencies or access requirements
- References to artifacts (files, commands, tickets)

## Style and fidelity rules

- The summary MUST be concise, structured, and non-narrative.
- The summary MUST NOT introduce new actions, outcomes, or causes.
- Ordering SHOULD mirror the original sequence when it matters.
- The summary MUST distinguish facts from hypotheses or proposals.
- Unresolved problems MUST be highlighted explicitly.

## Failure modes

- If the input record is missing or incomplete, the summary MUST note the gaps.
- If key outcomes cannot be determined, the summary MUST say so explicitly.
