# Shell Naming Conventions

## Purpose

Provide naming rules that optimize for clarity, consistency, and accessibility.

## Baseline Conventions

Follow these casing conventions as the default:

- Variables: `lowercase_snake_case`
- Functions: `lowercase_snake_case`
- Constants (`readonly` or exported configuration): `UPPER_SNAKE_CASE`
- Script filenames: `lowercase-with-hyphens.sh` (preferred) or
  `lowercase_with_underscores.sh`

## Variable Naming Rules

These rules are based on Damian Conway's "Perl Best Practices" (2005), adapted
for shell scripting and validated over long-term use. Conway's Rule 1
(class-to-variable mapping) has no analog in shell and is omitted entirely.

### 1. Minimum Length: 3+ Characters

One- and two-character variable names are prohibited because they reduce
readability and accessibility.

```bash
# Correct
for index in "${!instruments[@]}"; do
  instrument="${instruments[$index]}"
  process "$instrument"
done

file_count="${#files[@]}"

# Wrong
for i in "${!instruments[@]}"; do
  x="${instruments[$i]}"
  process "$x"
done

n="${#files[@]}"
```

Exceptions:

- Well-established mathematical variables in limited scope (`x`, `y` for a
  five-line coordinate calculation).
- Common domain abbreviations used across a codebase may appear as tokens:
  `id`, `db`, `api`, `env`, `app`. Use these only as clear tokens
  (for example, `instrument_id`, `db_host`, `api_url`, `env_name`,
  `app_state`), not as standalone single-character loop variables.

### 2. Complete English Words

Use complete English words, not abbreviations.

```bash
# Correct
configuration_file="/etc/app/config.yaml"
database_host="localhost"
error_message="Connection refused"
instrument_index=0

# Wrong
cfg="/etc/app/config.yaml"       # Use configuration_file
db_host="localhost"              # Acceptable (db is an allowed token)
err_msg="Connection refused"     # Use error_message
idx=0                            # Use index or instrument_index
```

Exception: allowed domain abbreviations (for example, `id`, `db`, `api`) may
appear as tokens in identifiers. Other acronyms are acceptable only when they
are official domain terms (for example, `UTC`) and should not be shortened
further.

### 3. Namespace Collision Handling

When sourcing multiple libraries or scripts that define the same variable or
function name, disambiguate with descriptive prefixes.

```bash
# Correct
source lib/database.sh
source lib/cache.sh

database_connection_string="postgres://..."
cache_connection_string="redis://..."

database_connect() { ... }
cache_connect() { ... }

# Wrong
source lib/database.sh
source lib/cache.sh

conn1="postgres://..."
conn2="redis://..."

connect() { ... }   # Which connect?
```

Collision prefixes are chosen contextually (for example, `database_`, `cache_`,
`http_`).

### 4. Boolean Variables

Prefer `is_`, `has_`, or `can_` prefixes when they make the name read more
naturally as a true/false condition:

- `is_*`: state or condition (`is_valid`, `is_empty`, `is_active`)
- `has_*`: possession or presence (`has_permission`, `has_items`, `has_error`)
- `can_*`: capability or permission (`can_delete`, `can_write`, `can_edit`)

Shell has no native boolean type. Use integer values (`0` for false, `1` for
true) or string values (`"true"` / `"false"`) consistently within a project.

```bash
# Prefixes improve clarity — use them
is_valid=0
has_permission=1
can_delete=0

if [[ "$has_permission" -eq 1 ]] && [[ "$can_delete" -eq 1 ]]; then
  delete_resource "$resource"
fi
```

Omit the prefix when the name already reads unambiguously as a boolean without
it. Names that are verbs or verb phrases often convey boolean intent on their
own:

```bash
# Already clear without a prefix
verify_tls=1
skip_validation=0
strict=1
```

Avoid bare nouns or adjectives that could be mistaken for the thing itself
rather than a condition about it:

```bash
# Ambiguous without a prefix
valid=0                # Use is_valid
permission=1           # Use has_permission
deletable=0            # Use can_delete
```

### 5. Collections: Plural vs. Singular

Name collections based on how they are primarily used.

Plural for collective processing (arrays):

```bash
files=("config.yaml" "data.json" "schema.sql")
for file in "${files[@]}"; do
  process "$file"
done

instrument_ids=()
for instrument in "${instruments[@]}"; do
  instrument_ids+=("${instrument%%:*}")
done
```

Singular with `_by_` suffix for individual access (associative arrays):

```bash
declare -A instrument_by_id
instrument_by_id["42"]="Guitar"
instrument_by_id["99"]="Piano"

instrument="${instrument_by_id["42"]}"
```

### 6. Consistency Rules

- Syntactic consistency: if one variable uses `adjective_noun`, all similar
  variables use `adjective_noun`.
- Semantic consistency: names convey what data represents, not just its type.
- Cross-codebase consistency: the same concept uses the same name everywhere.

```bash
# Correct
create_instrument() {
  local instrument_name="$1"
  local instrument_file="${INSTRUMENT_DIR}/${instrument_name}.yaml"
  echo "name: ${instrument_name}" > "$instrument_file"
}

update_instrument() {
  local instrument_name="$1"
  local instrument_file="${INSTRUMENT_DIR}/${instrument_name}.yaml"
  sed -i "s/^name:.*/name: ${instrument_name}/" "$instrument_file"
}

# Wrong
create_instrument() {
  local name="$1"
  local inst_file="${INSTRUMENT_DIR}/${name}.yaml"
  echo "name: ${name}" > "$inst_file"
}

update_instrument() {
  local instrument_name="$1"
  local instrument_file="${INSTRUMENT_DIR}/${instrument_name}.yaml"
  sed -i "s/^name:.*/name: ${instrument_name}/" "$instrument_file"
}
```
