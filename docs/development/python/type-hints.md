# Python Type Hints

## Table of Contents
- [Rule](#rule)
- [Rationale](#rationale)
- [Examples](#examples)

## Rule
All public functions and methods must have complete type hints. Enforce this
with a static type checker in strict mode.

## Rationale
Type hints are documentation, enable static analysis, and catch bugs during
development.

## Examples
```python
# Correct
def create_instrument(name: str, string_count: int) -> Instrument:
    ...

# Wrong
def create_instrument(name, string_count):
    ...
```
