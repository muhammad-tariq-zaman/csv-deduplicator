# csv-deduplicator

Deduplicate CSV rows by a chosen key column, keeping the first occurrence
and reporting how many rows were removed.

## How to run

```bash
python3 main.py --input tickets.csv --output clean.csv --key ticket_id
```

## Example output (sample from test fixture data)

```text
Kept 2 row(s), removed 1 duplicate(s). Wrote clean.csv
```

Standard library only. No network access.
