# Database Conventions

## Schema design

- Prefer fully normalized schemas with first-class tables and typed columns.
- JSON/JSONB is acceptable only when the data shape is unstable or evolving
  fast enough that normalization would churn.
- Treat JSON storage as provisional; revisit and normalize once the schema
  stabilizes.

## Table Naming

Table names are singular, not plural.

Rationale:
A table name represents a single row, not a collection.

Examples:

- `user` (not `users`)
- `exercise` (not `exercises`)
- `practice_block` (not `practice_blocks`)

## Model File Organization

File organization follows a multi-dimensional namespace (lifecycle coupling,
conceptual domains, hierarchy) mapped onto a single filesystem. These rules
minimize ambiguity while allowing explicit exceptions.

### Rule 1: One File Per Table

Each database table gets its own model file named after the table.

```python
models/practice.py
models/exercise_instance.py
models/technique.py
```

### Rule 2: Tightly Coupled One-to-One Tables

Tables with enforced 1:1 relationships that are always used together may be
bundled in the same file.

```python
class ExerciseInstance(Base):
    __tablename__ = "exercise_instance"

class ExerciseLog(Base):
    __tablename__ = "exercise_log"
    exercise_instance_id = Column(
        Integer, ForeignKey("exercise_instance.id"), unique=True
    )
```

### Rule 3: Association Tables

Many-to-many association tables are named alphanumerically and placed in the
alphabetically first entity's file.

```python
class ExerciseTechniqueAssociation(Base):
    __tablename__ = "exercise_technique_association"
```

This avoids subjective "importance" judgments and makes location predictable.

### Rule 4: Gray Areas

Any case not covered by Rules 1-3 requires explicit discussion and a recorded
decision. Document the rationale in code comments when non-obvious.

Examples of gray areas:

- polymorphic inheritance using joined-table patterns
- 1:many relationships that are conceptually inseparable
- legacy tables being deprecated together

### Revisiting the Rules

Revisit these rules when:

- a model file exceeds roughly 500 lines
- contributors frequently jump between files that should be co-located
- new contributors report confusion

The test for success: someone unfamiliar with the codebase can find what they
need without deep system knowledge.
