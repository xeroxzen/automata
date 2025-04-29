import pandas as pd
import time
import sys
import os

# Field name mapping
FIELD_MAP = {
    "UID": "id",
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
}

# Columns to include in the final output
OUTPUT_COLUMNS = list(FIELD_MAP.values())

def extract_first_name(n_value):
    parts = n_value.split(";")
    return parts[1].strip() if len(parts) > 1 else n_value.strip()

def clean_contacts(df):
    df = df[df['name'].isin(FIELD_MAP.keys())].copy()
    df['mapped'] = df['name'].map(FIELD_MAP)

    # Forward fill UID to group contact blocks
    df['contact_id'] = df[df['name'] == 'UID']['value']
    df['contact_id'] = df['contact_id'].fillna(method='ffill')

    # Special case handling
    df.loc[df['name'] == 'N', 'value'] = df['value'].apply(extract_first_name)

    # Group by contact_id and aggregate
    grouped = df.groupby(['contact_id', 'mapped'])['value'].agg(lambda x: ';'.join(x)).unstack().reset_index()

    # Rename UID to id
    grouped.rename(columns={'contact_id': 'id'}, inplace=True)

    # Ensure all columns are present
    for col in OUTPUT_COLUMNS:
        if col not in grouped.columns:
            grouped[col] = ''

    return grouped[OUTPUT_COLUMNS]

def main():
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python cleaner_pandas.py /path/to/file.csv")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        print(f"❌ File not found: {input_path}")
        sys.exit(1)

    df = pd.read_csv(input_path)
    cleaned_df = clean_contacts(df)
    output_path = input_path.replace(".csv", "_pandas_cleaned.csv")  
    cleaned_df.to_csv(output_path, index=False)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"🕒 Processing time: {elapsed_time:.2f} seconds")
    print(f"✅ Cleaned CSV saved to: {output_path}")

if __name__ == "__main__":
    main()
