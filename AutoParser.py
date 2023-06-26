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

                    # Call your SQL parser script here with the appropriate flag and file paths
                    # Replace 'your_parser_script.py' with the actual filename of your SQL parser script
                    subprocess.call(['python',
                                     'C:\\Users\\andile.mbele\\Desktop\\prescient\\code\\credscripts\\SqlParserPlus.py',
                                     '-s',
                                     sql_file_path, csv_file_path])

        print("SQL files parsed to CSV successfully.")
    except Exception as e:
        print("An error occurred during SQL file parsing:")
        print(e)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please provide the -s flag and the directory path as command-line arguments.")
        sys.exit(1)

    if sys.argv[1] != '-s':
        print("Please use the -s flag to indicate the SQL to CSV extraction operation.")
        sys.exit(1)

    directory_path = sys.argv[2]  # Directory path passed as command-line argument
    parse_sql_files(directory_path)



