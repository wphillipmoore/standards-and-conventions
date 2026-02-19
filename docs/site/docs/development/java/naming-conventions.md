# Java Naming Conventions

## Purpose

Provide naming rules that optimize for clarity, consistency, and accessibility.

## Google Java Style Guide Baseline

Follow the Google Java Style Guide as the default:

- Classes, interfaces, enums, records, annotations: `PascalCase`
- Methods, variables, parameters: `camelCase`
- Constants (`static final` immutable values): `UPPER_SNAKE_CASE`
- Packages: all lowercase, no underscores
- Type parameters: single uppercase letter (`T`, `E`, `K`, `V`) or
  `PascalCase` with a `T` suffix (`RequestT`, `ResponseT`)
- Private or internal fields: no prefix (no `m` prefix, no leading underscore)

## Casing Convention Note

The variable naming rules below are adapted from Damian Conway's "Perl Best
Practices" (2005). Conway's original rules assume `snake_case` for all
identifiers. Java's 30+ year ecosystem convention uses `camelCase` for
variables, methods, and parameters. Where Conway specifies casing, Java's
`camelCase` convention takes precedence without exception. Conway's underlying
principles (descriptive names, minimum length, complete words, grammatical
consistency) are fully adopted.

## Variable Naming Rules

These rules are based on Damian Conway's "Perl Best Practices" (2005), adapted
for Java and validated over long-term use.

### 1. Class-to-Variable Mapping

Variables representing a class instance use the `camelCase` version of the
class name.

```java
// Correct
Instrument instrument = new Instrument();
ExerciseState exerciseState = new ExerciseState();
PracticeBlock practiceBlock = new PracticeBlock();

// Wrong
Instrument inst = new Instrument();
ExerciseState exState = new ExerciseState();
PracticeBlock block = new PracticeBlock();
```

### 2. Minimum Length: 3+ Characters

One- and two-character variable names are prohibited because they reduce
readability and accessibility.

```java
// Correct
for (int index = 0; index < 10; index++) {
    Instrument instrument = instruments.get(index);
}

int count = instruments.size();
for (int instrumentIndex = 0; instrumentIndex < count; instrumentIndex++) {
    process(instruments.get(instrumentIndex));
}

// Wrong
for (int i = 0; i < 10; i++) {
    Instrument x = xs.get(i);
}
```

Exceptions:

- Well-established mathematical variables in limited scope (`x`, `y` for a
  five-line coordinate algorithm).
- Common domain abbreviations used across a codebase may appear as tokens:
  `id`, `db`, `api`, `env`, `app`. Use these only as clear tokens
  (for example, `instrumentId`, `dbSession`, `apiRouter`, `envName`,
  `appState`), not as single-character loop variables.
- Enum member names may use short domain codes (for example, `F0`) when those
  codes are established labels.

### 3. Complete English Words

Use complete English words, not abbreviations.

```java
// Correct
RuntimeException exception = new RuntimeException();
Configuration configuration = loadConfiguration();
Session databaseSession = getSession();
int instrumentIndex = 0;

// Wrong
RuntimeException exc = new RuntimeException();
Configuration config = loadConfiguration();  // Use configuration
Session db = getSession();                   // Use databaseSession
int idx = 0;                                 // Use index or instrumentIndex
```

Exception: allowed domain abbreviations (for example, `id`, `db`, `api`) may
appear as tokens in identifiers. Other acronyms are acceptable only when they
are official domain terms (for example, `UTC`) and should not be shortened
further.

### 4. Namespace Collision Handling

When multiple classes share a name, disambiguate with descriptive prefixes.

```java
// Correct
import org.hibernate.Session;
import javax.servlet.http.HttpSession;

Session dbSession = sessionFactory.openSession();
HttpSession httpSession = request.getSession();

// Wrong
import org.hibernate.Session;

Session sess = sessionFactory.openSession();
Object session2 = request.getSession();
```

Collision prefixes are chosen contextually (for example, `db`, `http`, `rest`).

### 5. Boolean Variables

Prefer `is*`, `has*`, or `can*` prefixes when they make the name read more
naturally as a true/false condition. This aligns with JavaBeans conventions
for boolean property accessors.

- `is*`: state or condition (`isValid`, `isEmpty`, `isActive`)
- `has*`: possession or presence (`hasPermission`, `hasItems`, `hasError`)
- `can*`: capability or permission (`canDelete`, `canWrite`, `canEdit`)

```java
// Prefixes improve clarity — use them
boolean isValid = validate(instrument);
boolean hasPermission = checkAccess(user);
boolean canDelete = user.isAdmin() || resource.getOwner().equals(user);

if (isValid && hasPermission && canDelete) {
    delete(resource);
}
```

Omit the prefix when the name already reads unambiguously as a boolean
without it. Names that are verbs, verb phrases, or adjective phrases often
convey boolean intent on their own:

```java
// Already clear without a prefix
boolean verifyTls = true;
boolean mapAttributes = true;
boolean strict = true;
```

Avoid bare nouns or adjectives that could be mistaken for the thing itself
rather than a condition about it:

```java
// Ambiguous without a prefix
boolean valid = validate(instrument);       // Use isValid
boolean permission = checkAccess(user);     // Use hasPermission
boolean deletable = user.isAdmin();         // Use canDelete
```

### 6. Collections: Plural vs. Singular

Name collections based on how they are primarily used.

Plural for collective processing:

```java
List<Instrument> instruments = query.getResultList();
for (Instrument instrument : instruments) {
    process(instrument);
}

List<Long> exerciseIds = exercises.stream()
    .map(Exercise::getId)
    .collect(Collectors.toList());
```

Singular for individual access (lookup tables):

```java
Map<Long, Instrument> instrumentById = instruments.stream()
    .collect(Collectors.toMap(Instrument::getId, Function.identity()));
Instrument instrument = instrumentById.get(42L);

Map<String, Exercise> exerciseByName = new HashMap<>();
Exercise exercise = exerciseByName.get("Chromatic Scale");
```

### 7. Consistency Rules

- Syntactic consistency: if one variable uses `adjectiveNoun`, all similar
  variables use `adjectiveNoun`.
- Semantic consistency: names convey what data represents, not just its type.
- Cross-codebase consistency: the same concept uses the same name everywhere.

```java
// Correct
public Instrument createInstrument(String name) {
    Instrument instrument = new Instrument(name);
    dbSession.persist(instrument);
    return instrument;
}

public Instrument updateInstrument(Instrument instrument, String name) {
    instrument.setName(name);
    dbSession.flush();
    return instrument;
}

// Wrong
public Instrument createInstrument(String name) {
    Instrument inst = new Instrument(name);
    dbSession.persist(inst);
    return inst;
}

public Instrument updateInstrument(Instrument instrument, String name) {
    instrument.setName(name);
    dbSession.flush();
    return instrument;
}
```
