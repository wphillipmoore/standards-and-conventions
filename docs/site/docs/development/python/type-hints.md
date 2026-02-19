# Python Type Hints

## Rule

All public functions and methods must have complete type hints. Enforce this
with static type checkers: mypy in strict mode and ty with default settings.

## Rationale

Type hints are documentation, enable static analysis, and catch bugs during
development.

## Type checker parity protocol

Both `mypy` and `ty` are hard CI gates. Failing either one blocks the pull
request.

When the tools disagree, follow this protocol:

1. Run both checkers locally with the canonical commands and capture the exact
   outputs.
2. Confirm configuration parity (strictness, ignores, per-module overrides,
   file selection) across `mypy` and `ty`.
3. If the failure is `mypy`-only, treat it as a blocker and resolve it. If the
   `mypy` error is intentionally suppressed, mirror the suppression or
   document the rationale for `ty`.
4. If the failure is `ty`-only, treat it as a blocker and resolve it. If `ty`
   is flagging a real issue, fix the code; if it is a false positive, document
   the discrepancy and adjust configuration where possible.
5. Record the mismatch in a GitHub issue with the outputs from both tools and
   the resolution path.

## Examples

```python
# Correct
def create_instrument(name: str, string_count: int) -> Instrument:
    ...

# Wrong
def create_instrument(name, string_count):
    ...
```
