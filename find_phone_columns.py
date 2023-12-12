import os
import csv
import sys

def find_phone_column(directory):
    matching_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)

                with open(file_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    header = next(csv_reader, None)

                    if header and any(col.lower() in map(str.lower, ["phone", "phonenumber", "phone_number", "tel", "telephone"]) for col in header):
                        matching_files.append(file_path)

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
        print("Files with phone-related columns found:")
        for file in matching_files:
            print(file)
    else:
        print("No files with phone-related columns found.")
