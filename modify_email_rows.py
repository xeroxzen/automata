'''
The Problem: I have a CSV file with multiple columns that may contain email addresses and some jibberish. These column is 'from_email'.

The Solution: Clear anything that is not an email address from the 'from_email' column. Also, remove all extra quotes and square brackets from the email addresses.
'''

import pandas as pd
import re
import sys

def modify_email_rows(filename):
    df = pd.read_csv(filename, on_bad_lines='skip', encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False, keep_default_na=False, low_memory=False)

    df['to_email'] = df['to_email'].apply(lambda x: re.sub('(.*<|>])', '', x))

    # save the modified dataframe to a new csv file
    df.to_csv(filename[:-4] + '_modified.csv', index=False)

    # print the modified dataframe
    print(df.head())


def main():
    modify_email_rows(sys.argv[1])

if __name__ == '__main__':
    main()