import pandas as pd
import os
import sys
import re

def extract_identifier(filename):
    match = re.search(r'_(\d+)_', filename)
    return match.group(1) if match else "unknown"

def merge_csv(users_file, usermeta_file):
    try:
        # Read CSV files
        users_df = pd.read_csv(users_file)
        usermeta_df = pd.read_csv(usermeta_file)

        # Ensure column names are properly formatted
        users_df.columns = users_df.columns.str.strip().str.lower()
        usermeta_df.columns = usermeta_df.columns.str.strip().str.lower()

        # Merge on id (users) and userid (usermeta)
        merged_df = users_df.merge(usermeta_df, left_on='id', right_on='userid', how='left')

        # Drop userid column as it's a duplicate of id
        merged_df.drop(columns=['userid'], inplace=True)

        # Extract identifiers
        users_id = extract_identifier(users_file)
        usermeta_id = extract_identifier(usermeta_file)

        # Construct output filename
        output_filename = f"bza2_users_{users_id}_and_usermeta_{usermeta_id}_combined.csv"
        output_path = os.path.join(os.path.dirname(users_file), output_filename)

        # Save merged CSV
        merged_df.to_csv(output_path, index=False)
        print(f"Merged file saved as: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_csv.py <users_file> <usermeta_file>")
    else:
        merge_csv(sys.argv[1], sys.argv[2])
