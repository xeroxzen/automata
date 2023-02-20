'''
The Problem: I have a CSV file with multiple columns that may contain email addresses and some jibberish which we don't need.

The Solution: Clear anything that is not an email address from the 'from_email' column. Also, remove all extra quotes and square brackets from the email addresses.
'''

import pandas as pd
import sys

def modify_email_rows(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        df = pd.read_csv(f, on_bad_lines='skip', sep=',', header=0, dtype=str, keep_default_na=False)

    df['to_email'] = df['to_email'].str.extract('<(.+)>')

    # save the modified dataframe to a new csv file
    df.to_csv(filename[:-4] + '_modified.csv', index=False)

    # print the modified dataframe
    print(df.head())


def main():
    modify_email_rows(sys.argv[1])

if __name__ == '__main__':
    main()
