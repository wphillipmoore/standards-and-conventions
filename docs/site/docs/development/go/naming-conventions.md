# Go Naming Conventions

## Purpose

Provide naming rules that optimize for clarity, consistency, and accessibility.

## Effective Go Baseline

Follow Effective Go and Go Code Review Comments as the default:

- Exported identifiers: `PascalCase`
- Unexported identifiers: `camelCase`
- Constants: `PascalCase` or `camelCase` per export status. Go does not use
  `UPPER_SNAKE_CASE`.
- Packages: all lowercase, single word preferred, no underscores
- Interfaces: single-method interfaces use `-er` suffix (`Reader`, `Writer`)
- Acronyms: all caps (`URL`, `HTTP`, `ID`, not `Url`, `Http`, `Id`)
- Receivers: short (one or two letters), consistent across all methods on the
  type

## Casing Convention Note

The variable naming rules below are adapted from Damian Conway's "Perl Best
Practices" (2005). Conway's original rules assume `snake_case` for all
identifiers. Go's ecosystem convention uses `MixedCaps` (`PascalCase` for
exported, `camelCase` for unexported) for all identifiers. Where Conway
specifies casing, Go's `MixedCaps` convention takes precedence without
exception. Conway's underlying principles (descriptive names, minimum length,
complete words, grammatical consistency) are fully adopted.

## Variable Naming Rules

These rules are based on Damian Conway's "Perl Best Practices" (2005), adapted
for Go and validated over long-term use.

### 1. Struct-to-Variable Mapping

Variables representing a struct instance use the `camelCase` version of the
struct name.

```go
// Correct
instrument := Instrument{}
exerciseState := ExerciseState{}
practiceBlock := PracticeBlock{}

// Wrong
inst := Instrument{}
exState := ExerciseState{}
block := PracticeBlock{}
```

### 2. Minimum Length: 3+ Characters

One- and two-character variable names are prohibited because they reduce
readability and accessibility.

```go
// Correct
for index := 0; index < 10; index++ {
    instrument := instruments[index]
    process(instrument)
}

count := len(instruments)
for instrumentIndex := 0; instrumentIndex < count; instrumentIndex++ {
    process(instruments[instrumentIndex])
}

// Wrong
for i := 0; i < 10; i++ {
    x := xs[i]
    process(x)
}
```

Exceptions:

- Go-idiomatic short variables in tight scope (five lines or fewer): `i` in
  single-level loops, `ok` from map/type-assertion checks, and `err` from
  error returns. These are deeply entrenched Go idioms that every Go developer
  reads fluently. Outside tight scope, use descriptive names (`index`,
  `exists`, `connectionError`).
- Well-established mathematical variables in limited scope (`x`, `y` for a
  five-line coordinate algorithm).
- Common domain abbreviations used across a codebase may appear as tokens:
  `id`, `db`, `api`, `env`, `app`. Use these only as clear tokens
  (for example, `instrumentID`, `dbSession`, `apiRouter`, `envName`,
  `appState`), not as single-character loop variables.

### 3. Complete English Words

Use complete English words, not abbreviations.

```go
// Correct
err := doSomething()
configuration := loadConfiguration()
databaseSession := getSession()
instrumentIndex := 0

// Wrong
exc := doSomething()
config := loadConfiguration()  // Use configuration
db := getSession()             // Use databaseSession
idx := 0                       // Use index or instrumentIndex
```

Exception: allowed domain abbreviations (for example, `id`, `db`, `api`) may
appear as tokens in identifiers. Other acronyms are acceptable only when they
are official domain terms (for example, `UTC`) and should not be shortened
further.

### 4. Namespace Collision Handling

When multiple packages export the same name, disambiguate with import aliases.

```go
// Correct
import (
    dbsql "database/sql"
    pgxpool "github.com/jackc/pgx/v5/pgxpool"
)

dbConnection, err := dbsql.Open("postgres", connectionString)
pool, err := pgxpool.New(ctx, connectionString)

// Wrong
import (
    "database/sql"
)

db, err := sql.Open("postgres", connectionString)
sess := getSession()
```

Alias prefixes are chosen contextually (for example, `db`, `http`, `rest`).

### 5. Boolean Variables

Prefer `is*`, `has*`, or `can*` prefixes when they make the name read more
naturally as a true/false condition:

- `is*`: state or condition (`isValid`, `isEmpty`, `isActive`)
- `has*`: possession or presence (`hasPermission`, `hasItems`, `hasError`)
- `can*`: capability or permission (`canDelete`, `canWrite`, `canEdit`)

```go
// Prefixes improve clarity — use them
isValid := validate(instrument)
hasPermission := checkAccess(user)
canDelete := user.IsAdmin() || resource.Owner == user

if isValid && hasPermission && canDelete {
    delete(resource)
}
```

Omit the prefix when the name already reads unambiguously as a boolean
without it. Names that are verbs, verb phrases, or adjective phrases often
convey boolean intent on their own:

```go
// Already clear without a prefix
verifyTLS := true
mapAttributes := true
strict := true
```

Avoid bare nouns or adjectives that could be mistaken for the thing itself
rather than a condition about it:

```go
// Ambiguous without a prefix
valid := validate(instrument)       // Use isValid
permission := checkAccess(user)     // Use hasPermission
deletable := user.IsAdmin()         // Use canDelete
```

### 6. Collections: Plural vs. Singular

Name collections based on how they are primarily used.

Plural for collective processing (slices):

```go
instruments := query.All()
for _, instrument := range instruments {
    process(instrument)
}

exerciseIDs := make([]int64, 0, len(exercises))
for _, exercise := range exercises {
    exerciseIDs = append(exerciseIDs, exercise.ID)
}
```

Singular with `By` suffix for individual access (maps):

```go
instrumentByID := make(map[int64]Instrument)
for _, instrument := range instruments {
    instrumentByID[instrument.ID] = instrument
}
instrument := instrumentByID[42]

exerciseByName := make(map[string]Exercise)
exercise := exerciseByName["Chromatic Scale"]
```

### 7. Consistency Rules

- Syntactic consistency: if one variable uses `adjectiveNoun`, all similar
  variables use `adjectiveNoun`.
- Semantic consistency: names convey what data represents, not just its type.
- Cross-codebase consistency: the same concept uses the same name everywhere.

```go
// Correct
func createInstrument(name string) Instrument {
    instrument := Instrument{Name: name}
    dbSession.Create(&instrument)
    return instrument
}

func updateInstrument(instrument Instrument, name string) Instrument {
    instrument.Name = name
    dbSession.Save(&instrument)
    return instrument
}

// Wrong
func createInstrument(name string) Instrument {
    inst := Instrument{Name: name}
    dbSession.Create(&inst)
    return inst
}

func updateInstrument(instrument Instrument, name string) Instrument {
    instrument.Name = name
    dbSession.Save(&instrument)
    return instrument
}
```
