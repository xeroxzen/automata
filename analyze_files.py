import os
import time
import csv
import sys

def print_csv_contents(directory):
    """
    Print the contents of CSV files in the given directory and its subdirectories,
    excluding files in specified folders.
    """
    excluded_folders = ['complete', 'sql_statements', 'unable_to_parse', 'badones', 'originals']

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        # Exclude specified folders from processing
        dirs[:] = [d for d in dirs if d not in excluded_folders]

        for file in files:
            if "yoast" not in file and "post" not in file and file.endswith('.csv'):
                file_path = os.path.join(root, file)
                print(f"Analyzing contents of {file_path}:")

                # Read and print the contents of the CSV file
                with open(file_path, 'r', encoding='utf-8') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        print(row)
                        time.sleep(1)

                print()  

if __name__ == '__main__':
    # Check if the directory is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
    else:
        directory = sys.argv[1]
        print_csv_contents(directory)
