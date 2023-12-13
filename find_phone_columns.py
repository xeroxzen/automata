import os
import csv
import sys

EXCLUDED_DIRECTORIES = ["complete", "sql_statements", "unable_to_parse", "originals", "wrong_length"]
PHONE_COLUMNS = ["phone", "phonenumber", "phone_number", "tel", "telephone"]

def is_csv_file(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension.lower() == ".csv"

def has_phone_column(header):
    return any(col.lower() in map(str.lower, PHONE_COLUMNS) for col in header)

def contains_separator(entry):
    return ',' in entry or ';' in entry

def process_csv_file(file_path):
    matching_entries = []

    with open(file_path, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader, None)

        if header and has_phone_column(header):
            for row in csv_reader:
                phone_column_indices = [i for i, col in enumerate(header) if col.lower() in map(str.lower, PHONE_COLUMNS)]
                for index in phone_column_indices:
                    if index < len(row):
                        phone_entry = row[index]
                        if contains_separator(phone_entry):
                            matching_entries.append(file_path)
                            return matching_entries

    return matching_entries

def find_phone_columns_with_separator(directory):
    matching_files = []

    for root, dirs, files in os.walk(directory):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRECTORIES]

        for file in files:
            if is_csv_file(file):
                file_path = os.path.join(root, file)
                matching_files.extend(process_csv_file(file_path))

    return matching_files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_phone_column.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]

    if not os.path.isdir(target_directory):
        print(f"Error: {target_directory} is not a valid directory.")
        sys.exit(1)

    matching_files = find_phone_columns_with_separator(target_directory)

    if matching_files:
        print("Files with phone-related columns and entries with commas or semicolons found:")
        for file in matching_files:
            print(file)
    else:
        print("No files with phone-related columns or entries with commas or semicolons found.")
