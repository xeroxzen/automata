"""
@author: Andile Jaden Mbele
@program: AutoParser.py
"""

import os
import subprocess
import sys


def parse_sql_files(directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.sql'):
                    sql_file_path = os.path.join(root, file)
                    csv_file_path = os.path.splitext(sql_file_path)[0] + '.csv'

                    # Call your SQL parser script here with the SQL file path and CSV file path
                    # Replace 'your_parser_script.py' with the actual filename of your SQL parser script
                    subprocess.call(['python', 'C:/Users/andile.mbele/Desktop/prescient/credscripts/SqlParserPlus.py', sql_file_path, csv_file_path])

        print("SQL files parsed to CSV successfully.")
    except Exception as e:
        print("An error occurred during SQL file parsing:")
        print(e)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the directory path as a command-line argument.")
        sys.exit(1)

    directory_path = sys.argv[1]  # Directory path passed as command-line argument
    parse_sql_files(directory_path)


