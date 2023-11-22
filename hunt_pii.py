"""
@author: Andile Jaden Mbele
"""

import os
import pandas as pd
import re
import sys

# Function to check if a column might contain PII
def is_pii_column(column_name):
    pii_keywords = ['email', 'firstname', 'lastname', 'password', 'ip_address', 'city', 'address', 'phone', 'hashed_password', 'created_at']
    for keyword in pii_keywords:
        if re.search(keyword, column_name, re.IGNORECASE):
            return True
    return False

# Function to analyze a CSV file
def analyze_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Analyzing: {file_path}")

        # Extracting column names
        columns = df.columns.tolist()
        print(f"Column Names: {columns}")

        # Check for PII columns
        pii_columns = [col for col in columns if is_pii_column(col)]
        print(f"PII Columns: {pii_columns}")

        # Identify useless columns
        useless_columns = [col for col in columns if not is_pii_column(col)]
        print(f"Useless Columns: {useless_columns}")

    except pd.errors.EmptyDataError:
        print(f"Empty file: {file_path}")

# Function to traverse directories
def traverse_directories(root_dir):
    output_dirs = []
    for root, dirs, files in os.walk(root_dir):
        if 'output' in dirs and 'originals' not in dirs and 'badones' not in dirs and 'complete' not in dirs and 'sql_statements' not in dirs and 'unable_to_parse' not in dirs and 'wrong_length' not in dirs:
            output_dirs.append(os.path.join(root, 'output'))

    return output_dirs

# Main function
def main(root_dir):
    output_dirs = traverse_directories(root_dir)

    for output_dir in output_dirs:
        csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
        print(f"\n{output_dir}: {len(csv_files)} CSV files found.")

        for csv_file in csv_files:
            file_path = os.path.join(output_dir, csv_file)
            analyze_csv(file_path)

if __name__ == "__main__":
    root_directory = sys.argv[1]
    main(root_directory)
