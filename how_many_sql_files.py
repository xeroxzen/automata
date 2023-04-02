"""
@Author: Google Jr
@program: How many SQL files?
"""

import os
import sys


def count_sql_files(directory):
    """
    A simple Python script to count the number of SQL files in a directory and subdirectories.
    """
    count = 0
    for dire in directory:
        try:
            os.chdir(dire)
            for root, dirs, files in os.walk(dire):
                for file in files:
                    if file.endswith('.sql'):
                        count += 1
            return count
        except:
            print('Unexpected error.')

    print('Number of SQL files: {}'.format(count))


def main():
    """
    Main function.
    """
    directory = sys.argv[1:]
    print(count_sql_files(directory))


if __name__ == '__main__':
    main()
