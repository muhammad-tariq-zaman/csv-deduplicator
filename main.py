"""CSV deduplicator: drop duplicate rows by key column, keep first."""
import argparse
import csv
import sys


def dedupe(input_path, output_path, key_column):
    seen, kept, removed = set(), [], 0
    with open(input_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if key_column not in (reader.fieldnames or []):
            raise ValueError(f"key column not found: {key_column}")
        for row in reader:
            key = row[key_column]
            if key in seen:
                removed += 1
            else:
                seen.add(key)
                kept.append(row)
        fields = reader.fieldnames
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(kept)
    return {"kept": len(kept), "removed": removed, "output": output_path}


def main(argv=None):
    p = argparse.ArgumentParser(description="Deduplicate a CSV by key column.")
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--key", required=True)
    args = p.parse_args(argv)
    r = dedupe(args.input, args.output, args.key)
    print(f"Kept {r['kept']} row(s), removed {r['removed']} duplicate(s). Wrote {r['output']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
