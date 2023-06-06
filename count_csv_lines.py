import os
import sys
import csv

IGNORE_FOLDERS = ['originals', 'Bad Ones', 'Wrong Length']
LINE_THRESHOLD = 10000

def count_lines_in_csv_files(directory):
    for root, dirs, files in os.walk(directory):
        # Exclude ignored folders
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                line_count = 0

                with open(file_path, 'r', encoding="utf-8") as csv_file:
                    reader = csv.reader(csv_file)
                    line_count = sum(1 for _ in reader)

                if line_count > LINE_THRESHOLD:
                    print(f"File '{file}' has {line_count} lines (above {LINE_THRESHOLD})")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    count_lines_in_csv_files(directory)
