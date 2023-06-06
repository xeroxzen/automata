import os
import time
import csv
import sys


def print_csv_contents(directory):
    """
    Print the contents of CSV files in the given directory.
    """
    # Find all CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    # Iterate over each CSV file
    for file in csv_files:
        file_path = os.path.join(directory, file)
        print(f"Printing contents of {file}:")

        # Read and print the contents of the CSV file
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
                time.sleep(2)  # Delay for 2 seconds between each line

        print()  # Print an empty line between files


if __name__ == '__main__':
    # Check if the directory is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
    else:
        directory = sys.argv[1]
        print_csv_contents(directory)
