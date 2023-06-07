"""
@author: Andile Jaden Mbele
@program: AutoParser.py
"""

import os
import subprocess


def parse_sql_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.sql'):
                sql_file_path = os.path.join(root, file)
                csv_file_path = os.path.splitext(sql_file_path)[0] + '.csv'

                # Call your SQL parser script here with the SQL file path and CSV file path
                # Replace 'your_parser_script.py' with the actual filename of your SQL parser script
                subprocess.call(['python', '~/Desktop/prescient/code/credscripts/SqlParserPlus.py', sql_file_path,
                                 csv_file_path])

    print("SQL files parsed to CSV successfully.")


if __name__ == '__main__':
    directory_path = '/path/to/nested_directories'  # Replace with the directory containing nested folders with SQL files
    parse_sql_files(directory_path)
