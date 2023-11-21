import os
import sys
import pandas as pd

def find_usermeta_files(directory):
    usermeta_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv") and "usermeta" in file:
                usermeta_files.append(os.path.join(root, file))
    return usermeta_files

def analyze_usermeta_files(files):
    column_patterns = {}

    for file in files:
        df = pd.read_csv(file, encoding="utf-8", error_bad_lines=False, warn_bad_lines=False)
        columns_to_ignore = ['shipping', 'billing', 'first_name', 'last_name', 'email', 'twitter', 'facebook', 'google']
        valid_columns = [column for column in df.columns if all(ignore not in column.lower() for ignore in columns_to_ignore)]

        for column in valid_columns:
            if column in column_patterns:
                column_patterns[column].append(file)
            else:
                column_patterns[column] = [file]

    return column_patterns

def generate_report(column_patterns):
    repeated_columns = {key: value for key, value in column_patterns.items() if len(value) > 1}

    if repeated_columns:
        print("Repeated columns in usermeta files:")
        for column, files in repeated_columns.items():
            print(f"Column '{column}' appears in files: {', '.join(files)}")
    else:
        print("No repeating columns found. No pattern identified.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    usermeta_files = find_usermeta_files(directory_path)

    if not usermeta_files:
        print("No usermeta files found.")
    else:
        column_patterns = analyze_usermeta_files(usermeta_files)
        generate_report(column_patterns)
