"""The Problem: I have a CSV file with multiple columns that may contain email addresses and some gibberish which we
don't need.

The Solution: Clear anything that is not an email address from the 'from_email' column. Also, remove all extra quotes
and square brackets from the email addresses."""

import re
import sys

import pandas as pd


def modify_email_rows(filename):
    df = pd.read_csv(filename, on_bad_lines='skip', encoding='utf-8', sep=',', header=0, index_col=False, dtype=str,
                     na_filter=False, keep_default_na=False, low_memory=False)

    df['to_email'] = df['to_email'].apply(lambda x: re.sub('(.*<|>])', '', x))
    # remove extra quotes and square brackets from the email addresses  
    df['cc_email'] = df['cc_email'].apply(lambda x: re.sub('(.*<|>])', '', x))

    # save the modified dataframe to a new csv file. 
    df.to_csv(filename[:-4] + '_modified.csv', index=False)

    # print the modified dataframe
    print(df.head())


def main():
    modify_email_rows(sys.argv[1])


if __name__ == '__main__':
    main()
