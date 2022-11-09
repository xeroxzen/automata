"""
@author: Andile Jaden Mbele
@date: 9 November 2022
"""

# Write a script that prints the headers/columns of a CSV file. The script takes a parameter of the file directory
# Use Pandas

import pandas as pd
import sys

def get_table_columns(path):
    '''
    $ python3 get_table_columns.py /path/to/file.csv
    ['id', 'name', 
    '''

    df = pd.read_csv(path)
    count = 1
    for each in df.columns:
        print(count, each)
        count +1

def main():
    get_table_columns(sys.argv[1])

if __name__ == '__main__':
    main()