import os
import sys
import csv
from collections import defaultdict

def find_usermeta_files(directory):
    usermeta_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv") and "usermeta" in file:
                usermeta_files.append(os.path.join(root, file))
    return usermeta_files

def analyze_usermeta_files(files):
    column_patterns = defaultdict(list)

    for file in files:
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)  # Assuming the first row is the header

            if header:
                for i, column in enumerate(header):
                    column_patterns[column].append(i)

    return column_patterns

def generate_report(column_patterns):
    repeated_columns = {key: value for key, value in column_patterns.items() if len(value) > 1}

    if repeated_columns:
        print("Repeated columns in usermeta files:")
        for column, indices in repeated_columns.items():
            print(f"Column '{column}' appears at indices {indices}")
    else:
        print("No repeating columns found. No pattern identified.")

if __name__ == "__main__":
    directory_path = sys.argv[1]

    usermeta_files = find_usermeta_files(directory_path)

    if not usermeta_files:
        print("No usermeta files found.")
    else:
        column_patterns = analyze_usermeta_files(usermeta_files)
        generate_report(column_patterns)
