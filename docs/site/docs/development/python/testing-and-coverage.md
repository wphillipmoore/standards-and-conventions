# Python Testing and Coverage

## Core Principle

Maintain code coverage as close to 100 percent as reasonably possible.

## Default Assumption

All code is tested unless explicitly documented otherwise.

## Exceptions

Exclusions must be explicit and documented with:

- the path or scope excluded
- the reason for exclusion
- how the excluded code is validated (if applicable)

## Coverage Target

- Goal: 100 percent code coverage (lines and branches) across production code.
- Tooling: pytest with pytest-cov.
- Measurement:

  ```bash
  pytest --cov=src --cov-report=term-missing --cov-branch
  ```

- Branch coverage must include all code paths, not just line execution.

## Untestable Code Documentation

If code cannot be reliably tested, document it in the code so gaps are visible
during review and maintenance.

Mark untestable branches like this:

```python
def handle_database_connection(config: dict) -> Connection:
    """
    Establish database connection with retry logic.

    Note: The connection timeout branch cannot be reliably tested in unit
    tests due to non-deterministic timing behavior. Integration tests
    cover this scenario.
    """
    try:
        return connect(config)
    except TimeoutError:  # pragma: no cover - timing-dependent
        logger.warning("Connection timeout, retrying...")
        time.sleep(1)
        return connect(config)
```

Valid reasons for untestable code (document which applies):

- Platform-specific behavior that cannot be simulated in test environments
- Timing-dependent race conditions (covered by integration or system tests)
- External service failures that cannot be reliably mocked
- Hardware-dependent operations
- Defensive code for "impossible" states (document why it is impossible)

Documentation format:

```python
# pragma: no cover - <brief reason>, <where it is tested if applicable>
```

Do not include specific line numbers in docstrings or comments explaining
coverage exceptions. Describe the branch or condition conceptually instead.

## Coverage Reporting

```bash
pytest --cov=src --cov-report=term-missing --cov-branch
pytest --cov=src --cov-report=html --cov-branch
```

## Coverage Expectations

- New code must maintain or improve overall coverage for lines and branches.
- Any decrease requires explicit justification and documentation.
- Branch coverage gaps indicate untested code paths and must be reviewed.

## Rationale

High coverage provides:

1. Confidence that code paths are exercised
2. Refactoring safety
3. Documentation through tests
4. Edge case protection
5. Visible accounting for untested gaps

100 percent coverage is necessary but not sufficient; tests must assert
correct behavior.
