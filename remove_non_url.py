'''
@author: Andile Mbele
@program: remove_non_url.py
'''

import pandas as pd
import re
import sys

def verify_url(filename):
    '''
    Verify the URL addresses in the "url" column. Delete any entry that does not qualify as a valid URL.
    '''
    try:
        df = pd.read_csv(filename, encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False, keep_default_na=False, low_memory=False)
        # check for multiple columns that may contain email addresses. Example: email, email2, email3, cc_email, from_email, to_email, etc.
        df = df[df['extra'].str.contains(r'^(https?://)?(www\.)?[a-zA-Z0-9]+(\.[a-zA-Z]{2,})(/.*)?$', regex=True)]
        print(df.head())

        # save to csv
        df.to_csv(filename[:-4] + '_modified.csv', index=False)
    except Exception as e:
        print(e)

def main():
    '''
    Main function.
    '''
    verify_url(sys.argv[1])

if __name__ == '__main__':
    main()