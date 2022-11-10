"""
@author: Andile Jaden Mbele
"""

# Write a script that prints the headers/columns of a CSV file. The script should take the path to the CSV file as an argument.
# Use Pandas

import sys
import pandas as pd

def get_table_columns(path):
    '''
    $ python get_table_columns.py /path/to/file.csv
    ['id', 'name', '
    '''
    df = pd.read_csv(path)
    count = 1
    for each in df.columns:
        print(count, each)
        count += 1

def main():
    get_table_columns(sys.argv[1])

if __name__ == '__main__':
    main()