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

        # Check for first_name/firstname and last_name/lastname, merge into fullname
        first_name_col = next((col for col in merged_df.columns if col in ['first_name', 'firstname']), None)
        last_name_col = next((col for col in merged_df.columns if col in ['last_name', 'lastname']), None)

        if first_name_col and last_name_col:
            merged_df['fullname'] = merged_df[first_name_col] + ' ' + merged_df[last_name_col]
            merged_df.drop(columns=[first_name_col, last_name_col], inplace=True)

        # Extract identifiers
        users_id = extract_identifier(users_file)
        usermeta_id = extract_identifier(usermeta_file)

        # Construct output filename
        output_filename = f"users_{users_id}_and_usermeta_{usermeta_id}_combined.csv"
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
