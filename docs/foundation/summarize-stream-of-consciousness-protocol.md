# Summarize stream of consciousness protocol

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Definitions](#definitions)
- [Prompt shortcuts](#prompt-shortcuts)
- [Protocol states](#protocol-states)
- [Capture rules](#capture-rules)
- [Post-processing output](#post-processing-output)
- [Failure modes](#failure-modes)

## Purpose
Define a toggleable protocol for capturing unfiltered, unstructured thoughts
and organizing them into a durable summary after capture ends.

## Scope
Use this protocol when raw idea capture is more valuable than immediate
analysis, and the intent is to synthesize later into a structured artifact.

## Definitions
- SOC session: the capture window between `Enter SOC` and `End SOC`.
- Capture record: the ordered list of messages collected during a SOC session.
- Trigger prompts: standalone messages that switch modes.

## Prompt shortcuts
Use standalone prompts that invoke the protocol:
- `Enter SOC` to begin capture.
- `End SOC` to end capture.

## Protocol states
The protocol is a two-state machine:
- Idle: normal interaction and processing.
- SOC capture: record-only mode.

Transitions:
- Idle to SOC capture on `Enter SOC`.
- SOC capture to Idle on `End SOC`.
- `Enter SOC` received during SOC capture is recorded as normal content.
- `End SOC` received while Idle is treated as normal content.
 - The `Enter SOC` transition MUST be acknowledged with a confirmation that
   SOC capture mode is active.

## Capture rules
- Trigger prompts MUST be standalone messages with exact text matching
  `Enter SOC` or `End SOC`.
- During SOC capture, all messages MUST be recorded verbatim and in order.
- During SOC capture, the system MUST NOT summarize, interpret, or act on
  captured content.
- If a response is required during SOC capture, it SHOULD be a minimal,
  non-interpretive acknowledgment.
- Capture records SHOULD include, when available, message order and speaker
  labels. Timestamps MAY be added if they are already available.

## Post-processing output
After `End SOC`, produce a structured summary derived only from the capture
record. Do not introduce new ideas. If inference is unavoidable, label it as
inference.

Required sections in order:
- Summary: 1-3 sentences describing the overall thrust.
- Themes: grouped bullets of related ideas.
- Open questions: unresolved items or ambiguities.

Optional sections (include only when non-empty):
- Decisions
- Action items
- Outliers

## Failure modes
- If a SOC session is not closed with `End SOC`, no summary is produced.
- If capture artifacts are missing or corrupted, the summary MUST explicitly
  note the gaps and proceed only with the available content.
