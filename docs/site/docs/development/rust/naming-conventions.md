# Rust Naming Conventions

## Purpose

Provide naming rules that optimize for clarity, consistency, and accessibility.

## Rust Conventions Baseline

Follow the Rust API Guidelines (RFC 430) and standard library conventions as the
default:

- Functions and methods: `snake_case`
- Local variables: `snake_case`
- Types (structs, enums, traits): `PascalCase`
- Constants and statics: `UPPER_SNAKE_CASE`
- Modules and crates: `snake_case`
- Type parameters: single uppercase letter (`T`, `E`, `K`, `V`) or short
  `PascalCase` when more descriptive (`Conn`, `Req`)
- Lifetimes: short lowercase (`'a`, `'b`), or descriptive when clarity demands
  it (`'conn`, `'request`)
- Acronyms in `PascalCase` contexts: capitalize only the first letter
  (`HttpClient`, not `HTTPClient`; `JsonParser`, not `JSONParser`)
- Trait naming: prefer nouns or adjectives (`Display`, `Iterator`, `Clone`).
  Use `-able` or `-er` suffixes when natural (`Readable`, `Encoder`).

## Casing Convention Note

The variable naming rules below are adapted from Damian Conway's "Perl Best
Practices" (2005). Conway's original rules assume `snake_case` for all
identifiers. Rust's ecosystem convention also uses `snake_case` for variables
and functions, making the adaptation direct. Conway's underlying principles
(descriptive names, minimum length, complete words, grammatical consistency)
are fully adopted.

## Variable Naming Rules

These rules are based on Damian Conway's "Perl Best Practices" (2005), adapted
for Rust and validated over long-term use.

### 1. Struct-to-Variable Mapping

Variables representing a struct instance use the `snake_case` version of the
struct name.

```rust
// Correct
let instrument = Instrument::new();
let exercise_state = ExerciseState::default();
let practice_block = PracticeBlock::new();

// Wrong
let inst = Instrument::new();
let ex_state = ExerciseState::default();
let block = PracticeBlock::new();
```

### 2. Minimum Length: 3+ Characters

One- and two-character variable names are prohibited because they reduce
readability and accessibility.

```rust
// Correct
for index in 0..10 {
    let instrument = &instruments[index];
    process(instrument);
}

let count = instruments.len();
for instrument_index in 0..count {
    process(&instruments[instrument_index]);
}

// Wrong
for i in 0..10 {
    let x = &xs[i];
    process(x);
}
```

Exceptions:

- Rust-idiomatic short variables in tight scope (five lines or fewer): `ok` and
  `err` in `Result` handling, `i` in single-level loops, `_` for ignored values.
  These are deeply entrenched Rust idioms that every Rust developer reads
  fluently. Outside tight scope, use descriptive names (`index`, `connection_error`).
- Well-established mathematical variables in limited scope (`x`, `y` for a
  five-line coordinate algorithm).
- Common domain abbreviations used across a codebase may appear as tokens:
  `id`, `db`, `api`, `env`, `app`. Use these only as clear tokens
  (for example, `instrument_id`, `db_session`, `api_router`, `env_name`,
  `app_state`), not as single-character loop variables.

### 3. Complete English Words

Use complete English words, not abbreviations.

```rust
// Correct
let err = do_something();
let configuration = load_configuration();
let database_session = get_session();
let instrument_index = 0;

// Wrong
let exc = do_something();
let config = load_configuration();  // Use configuration
let db = get_session();             // Use database_session
let idx = 0;                        // Use index or instrument_index
```

Exception: allowed domain abbreviations (for example, `id`, `db`, `api`) may
appear as tokens in identifiers. Other acronyms are acceptable only when they
are official domain terms (for example, `UTC`) and should not be shortened
further.

### 4. Namespace Collision Handling

When multiple crates or modules export the same name, disambiguate with `use`
aliases.

```rust
// Correct
use std::io::Error as IoError;
use serde_json::Error as JsonError;

fn handle_io(error: IoError) { /* ... */ }
fn handle_json(error: JsonError) { /* ... */ }

// Wrong
use std::io::Error;

fn handle(error: Error) { /* ... */ }
```

Alias prefixes are chosen contextually (for example, `Io`, `Json`, `Http`).

### 5. Boolean Variables

Prefer `is_*`, `has_*`, or `can_*` prefixes when they make the name read more
naturally as a true/false condition:

- `is_*`: state or condition (`is_valid`, `is_empty`, `is_active`)
- `has_*`: possession or presence (`has_permission`, `has_items`, `has_error`)
- `can_*`: capability or permission (`can_delete`, `can_write`, `can_edit`)

```rust
// Prefixes improve clarity — use them
let is_valid = validate(&instrument);
let has_permission = check_access(&user);
let can_delete = user.is_admin() || resource.owner == user;

if is_valid && has_permission && can_delete {
    delete(&resource);
}
```

Omit the prefix when the name already reads unambiguously as a boolean
without it. Names that are verbs, verb phrases, or adjective phrases often
convey boolean intent on their own:

```rust
// Already clear without a prefix
let verify_tls = true;
let map_attributes = true;
let strict = true;
```

Avoid bare nouns or adjectives that could be mistaken for the thing itself
rather than a condition about it:

```rust
// Ambiguous without a prefix
let valid = validate(&instrument);       // Use is_valid
let permission = check_access(&user);    // Use has_permission
let deletable = user.is_admin();         // Use can_delete
```

### 6. Collections: Plural vs. Singular

Name collections based on how they are primarily used.

Plural for collective processing (vectors, slices):

```rust
let instruments = query.all();
for instrument in &instruments {
    process(instrument);
}

let exercise_ids: Vec<i64> = exercises
    .iter()
    .map(|exercise| exercise.id)
    .collect();
```

Singular with `by_` suffix for individual access (hash maps):

```rust
let mut instrument_by_id: HashMap<i64, Instrument> = HashMap::new();
for instrument in &instruments {
    instrument_by_id.insert(instrument.id, instrument.clone());
}
let instrument = &instrument_by_id[&42];

let exercise_by_name: HashMap<String, Exercise> = HashMap::new();
let exercise = &exercise_by_name["Chromatic Scale"];
```

### 7. Consistency Rules

- Syntactic consistency: if one variable uses `adjective_noun`, all similar
  variables use `adjective_noun`.
- Semantic consistency: names convey what data represents, not just its type.
- Cross-codebase consistency: the same concept uses the same name everywhere.

```rust
// Correct
fn create_instrument(name: &str) -> Instrument {
    let instrument = Instrument { name: name.to_string() };
    db_session.create(&instrument);
    instrument
}

fn update_instrument(instrument: &mut Instrument, name: &str) -> &Instrument {
    instrument.name = name.to_string();
    db_session.save(instrument);
    instrument
}

// Wrong
fn create_instrument(name: &str) -> Instrument {
    let inst = Instrument { name: name.to_string() };
    db_session.create(&inst);
    inst
}

fn update_instrument(instrument: &mut Instrument, name: &str) -> &Instrument {
    instrument.name = name.to_string();
    db_session.save(instrument);
    instrument
}
```
