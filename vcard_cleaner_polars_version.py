import sys
import os
import polars as pl
import time

FIELD_MAP = {
    "N": "first_name",
    "FN": "name",
    "TEL": "phone",
    "ADR": "address",
    "EMAIL": "email",
    "ORG": "company",
    "NOTE": "note",
    "CATEGORIES": "category",
    "BDAY": "birth_date",
    "TITLE": "position",
    "URL": "url"
    # "UID" intentionally excluded to avoid conflict
}

def extract_first_name(n_value: str) -> str:
    try:
        parts = n_value.split(";")
        return parts[1] if len(parts) > 1 else ""
    except Exception:
        return ""

def clean_contacts(df: pl.DataFrame) -> pl.DataFrame:
    # Create a consistent contact ID by grouping using UID
    df = df.with_columns([
        pl.when(pl.col("name") == "UID")
          .then(pl.col("value"))
          .otherwise(None)
          .alias("contact_id")
    ])

    # Forward fill the contact_id so each row is associated with the correct person
    df = df.with_columns([
        pl.col("contact_id").forward_fill().alias("_contact_id")
    ]).drop("contact_id")

    # Filter to only fields we care about
    df = df.filter(pl.col("name").is_in(FIELD_MAP.keys()))

    # Map the name column to desired output field names
    df = df.with_columns([
        pl.col("name").map_dict(FIELD_MAP).alias("mapped")
    ])

    # If it's "first_name", extract the correct part from N
    df = df.with_columns([
        pl.when(pl.col("mapped") == "first_name")
          .then(pl.col("value").map_elements(extract_first_name))
          .otherwise(pl.col("value"))
          .alias("cleaned_value")
    ])

    # Pivot data: one row per contact, one column per mapped field
    pivoted = df.select(["_contact_id", "mapped", "cleaned_value"]) \
                .pivot(values="cleaned_value", index="_contact_id", columns="mapped", aggregate_function="first") \
                .rename({"_contact_id": "id"})

    return pivoted

def main():
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python vcard_cleaner_polars_version.py /path/to/input.csv")
        return

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        sys.exit(1)
        
    df = pl.read_csv(input_path)
    cleaned = clean_contacts(df)
    output_path = input_path.replace(".csv", "_polars_cleaned.csv")
    cleaned.write_csv(output_path)
    
    end_time = time.time()
    elapsed_time = end_time - start_time    
    print(f"🕒 Processing time: {elapsed_time:.2f} seconds")
    print(f"Cleaned CSV saved to: {output_path}")

if __name__ == "__main__":
    main()
