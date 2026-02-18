# Python Import-Time Side Effects

## Rule

No implicit state or side effects at import time.

## Allowed Exceptions

Framework-standard registration mechanisms are permitted when required by the
framework. Examples include:

- SQLAlchemy ORM model declarations (including `Table` definitions and
  declarative class registration in `Base.metadata`)
- FastAPI router definitions (`APIRouter()` creation and decorator-based route
  registration)

These are allowed only because the frameworks require import-time registration.
All other side effects remain forbidden.

## Forbidden Examples

- Engine or session creation
- Settings loading or environment mutation
- Network calls
- File system writes
- Global mutable state initialization
