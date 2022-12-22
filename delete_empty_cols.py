import pandas as pd
import sys

def delete_empty_cols(path):
    # Write a python script that loads a csv or txt file and deletes all empty columns.
    # Use pandas to load the file and delete the empty columns.

    # dataframe
    df = pd.read_csv(path, sep='|', encoding='latin-1', error_bad_lines=False, low_memory=False)

    # delete empty columns
    df = df.dropna(axis=1, how='all')

    # save the file where the original file was
    df.to_csv(path.replace('.txt', '_no_empty_cols.csv'), sep=',', index=False)

def main():
    delete_empty_cols(sys.argv[1])

if __name__ == '__main__':
    main()            