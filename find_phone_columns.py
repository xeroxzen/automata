import os
import csv
import sys

EXCLUDED_DIRECTORIES = ["complete", "sql_statements", "unable_to_parse", "originals", "wrong_length"]

def find_phone_column(directory):
    matching_files = []

    for root, dirs, files in os.walk(directory):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRECTORIES]

        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)

                with open(file_path, 'r'l encoding="utf-8") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    header = next(csv_reader, None)

                    if header and any(col.lower() in map(str.lower, ["phone", "phonenumber", "phone_number", "tel", "telephone"]) for col in header):
                        for row in csv_reader:
                            phone_column_indices = [i for i, col in enumerate(header) if col.lower() in map(str.lower, ["phone", "phonenumber", "phone_number", "tel", "telephone"])]
                            for index in phone_column_indices:
                                if index < len(row):
                                    phone_entry = row[index]
                                    if ',' in phone_entry or ';' in phone_entry:
                                        matching_files.append(file_path)
                                        break

    return matching_files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_phone_column.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]

    if not os.path.isdir(target_directory):
        print(f"Error: {target_directory} is not a valid directory.")
        sys.exit(1)

    matching_files = find_phone_column(target_directory)

    if matching_files:
        print("Files with phone-related columns and entries with commas or semicolons found:")
        for file in matching_files:
            print(file)
    else:
        print("No files with phone-related columns or entries with commas or semicolons found.")
