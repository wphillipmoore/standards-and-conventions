# Python Naming Conventions

## Purpose

Provide naming rules that optimize for clarity, consistency, and accessibility.

## PEP 8 Baseline

Follow PEP 8 as the default:

- Variables, functions, methods: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private or internal: leading underscore (`_internal_name`)
- Module-level dunder names: `__all__`, `__version__`, and similar

## Variable Naming Rules

These rules are based on Damian Conway's "Perl Best Practices" (2005), adapted
for Python and validated over long-term use.

### 1. Class-to-Variable Mapping

Variables representing a class instance use the `snake_case` version of the
class name.

```python
# Correct
instrument = Instrument(...)
exercise_state = ExerciseState(...)
practice_block = PracticeBlock(...)

# Wrong
inst = Instrument(...)
ex_state = ExerciseState(...)
block = PracticeBlock(...)
```

### 2. Minimum Length: 3+ Characters

One- and two-character variable names are prohibited because they reduce
readability and accessibility.

```python
# Correct
for index in range(10):
    instrument = instruments[index]

for instrument_index, instrument in enumerate(instruments):
    process(instrument)

# Wrong
for i in range(10):
    x = xs[i]

for i, x in enumerate(xs):
    process(x)
```

Exceptions:

- Well-established mathematical variables in limited scope (`x`, `y` for a
  five-line coordinate algorithm).
- Common domain abbreviations used across a codebase may appear as tokens:
  `id`, `db`, `api`, `env`, `app`. Use these only as clear tokens
  (for example, `instrument_id`, `db_session`, `api_router`, `env_name`,
  `app_state`), not as single-character loop variables.
- Enum member names may use short domain codes (for example, `F0`) when those
  codes are established labels.

### 3. Complete English Words

Use complete English words, not abbreviations.

```python
# Correct
exception = ValueError(...)
configuration = load_config()
database_session = get_session()
instrument_index = 0

# Wrong
exc = ValueError(...)
config = load_config()  # Use configuration
db = get_session()      # Use db_session
idx = 0                 # Use index or instrument_index
```

Exception: allowed domain abbreviations (for example, `id`, `db`, `api`) may
appear as tokens in identifiers. Other acronyms are acceptable only when they
are official domain terms (for example, `UTC`) and should not be shortened
further.

### 4. Namespace Collision Handling

When multiple classes share a name, disambiguate with descriptive prefixes.

```python
# Correct
from sqlalchemy.orm import Session as DBSession
from requests import Session as RESTSession

db_session = DBSession()
rest_session = RESTSession()

# Wrong
from sqlalchemy.orm import Session
db = Session()
sess = Session()
```

Collision prefixes are chosen contextually (for example, `DB`, `REST`).

### 5. Boolean Variables

Prefer `is_*`, `has_*`, or `can_*` prefixes when they make the name read more
naturally as a true/false condition:

- `is_*`: state or condition (`is_valid`, `is_empty`, `is_active`)
- `has_*`: possession or presence (`has_permission`, `has_items`, `has_error`)
- `can_*`: capability or permission (`can_delete`, `can_write`, `can_edit`)

```python
# Prefixes improve clarity — use them
is_valid = validate(instrument)
has_permission = check_access(user)
can_delete = user.is_admin or resource.owner == user

if is_valid and has_permission and can_delete:
    delete(resource)
```

Omit the prefix when the name already reads unambiguously as a boolean without
it. Names that are verbs, verb phrases, or adjective phrases often convey
boolean intent on their own:

```python
# Already clear without a prefix
verify_tls = True
map_attributes = True
strict = True
```

Avoid bare nouns or adjectives that could be mistaken for the thing itself
rather than a condition about it:

```python
# Ambiguous without a prefix
valid = validate(instrument)       # Use is_valid
permission = check_access(user)    # Use has_permission
deletable = ...                    # Use can_delete
```

### 6. Collections: Plural vs. Singular

Name collections based on how they are primarily used.

Plural for collective processing:

```python
instruments = query.all()
for instrument in instruments:
    process(instrument)

exercise_ids = [ex.id for ex in exercises]
```

Singular for individual access (lookup tables):

```python
instrument_by_id = {inst.id: inst for inst in query.all()}
instrument = instrument_by_id[42]

exercise_by_name = {...}
exercise = exercise_by_name["Chromatic Scale"]
```

Singular for indexed access:

```python
instrument_lookup = [...]
instrument = instrument_lookup[index]
```

### 7. Consistency Rules

- Syntactic consistency: if one variable uses `adjective_noun`, all similar
  variables use `adjective_noun`.
- Semantic consistency: names convey what data represents, not just its type.
- Cross-codebase consistency: the same concept uses the same name everywhere.

```python
# Correct
def create_instrument(name: str) -> Instrument:
    instrument = Instrument(name=name)
    db_session.add(instrument)
    return instrument

def update_instrument(instrument: Instrument, name: str) -> Instrument:
    instrument.name = name
    db_session.commit()
    return instrument

# Wrong
def create_instrument(name: str) -> Instrument:
    inst = Instrument(name=name)
    db_session.add(inst)
    return inst

def update_instrument(instrument: Instrument, name: str) -> Instrument:
    instrument.name = name
    db_session.commit()
    return instrument
```
