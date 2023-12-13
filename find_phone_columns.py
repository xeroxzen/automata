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
    modified_rows = []

    with open(file_path, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader, None)

        if header and has_phone_column(header):
            new_header = header.copy()
            for col in header:
                if col.lower() in map(str.lower, PHONE_COLUMNS):
                    new_header.append(f"{col}_second")

            modified_rows.append(new_header)

            for row in csv_reader:
                modified_row = row.copy()
                for index, col in enumerate(header):
                    if col.lower() in map(str.lower, PHONE_COLUMNS):
                        phone_entry = row[index]
                        if contains_separator(phone_entry):
                            entries = phone_entry.split(',' if ',' in phone_entry else ';')
                            modified_row[index] = entries[0].strip()
                            modified_row.append(entries[1].strip())
                modified_rows.append(modified_row)

    return modified_rows

def modify_phone_columns_with_separator(directory):
    modified_files = {}

    for root, dirs, files in os.walk(directory):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRECTORIES]

        for file in files:
            if is_csv_file(file):
                file_path = os.path.join(root, file)
                modified_files[file_path] = process_csv_file(file_path)

    return modified_files

def save_modified_files(modified_files):
    for file_path, modified_rows in modified_files.items():
        output_file_path = os.path.splitext(file_path)[0] + "_modified.csv"
        with open(output_file_path, 'w', encoding="utf-8", newline='') as output_csv_file:
            csv_writer = csv.writer(output_csv_file)
            csv_writer.writerows(modified_rows)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python modify_phone_columns.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]

    if not os.path.isdir(target_directory):
        print(f"Error: {target_directory} is not a valid directory.")
        sys.exit(1)

    modified_files = modify_phone_columns_with_separator(target_directory)

    if modified_files:
        save_modified_files(modified_files)
        print("Files modified successfully. Modified files saved with '_modified' suffix.")
    else:
        print("No files with phone-related columns or entries with commas or semicolons found.")
