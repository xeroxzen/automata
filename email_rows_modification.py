'''
The Problem: I have a CSV file with multiple columns that may contain email addresses and some jibberish. These columns are 'from_email', 'to_email', 'cc_email'.

The Solution: Using regex clear anything that is not an email address from the 'from_email', 'to_email', 'cc_email' columns. Also, remove all extra quotes and square brackets from the email addresses. Maintain the original CSV file and create a new CSV file with the modified email addresses. Maintain all rows so  they correspond to the emailid column.
'''

import pandas as pd
import re   
import sys

def modify_email_rows(filename):
    '''
    Using regex clear anything that is not an email address from the 'from_email', 'to_email', 'cc_email' columns. Also, remove all extra quotes and square brackets from the email addresses. Maintain the original CSV file and create a new CSV file with the modified email addresses. Maintain all rows so  they correspond to the emailid column.
    '''
    df = pd.read_csv(filename, encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False, keep_default_na=False, low_memory=False)
    # check for multiple columns that may contain email addresses. Example: email, email2, email3, cc_email, from_email, to_email, etc.
    # df['from_email'] = df['from_email'].str.replace(r'[\[\]]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'["]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\[\]]', '')
    df['to_email'] = df['to_email'].str.replace(r'["]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\[\]]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'["]', '')
    # df = df[df['from_email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')]
    df = df[df['to_email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')]
    df = df[df['cc_email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')]
    print(df.head())

    # save to csv in a new file with the same name as the original file, but with '_modified' appended to the end of the filename
    df.to_csv(filename[:-4] + '_modified.csv', index=False)

def main():
    modify_email_rows(sys.argv[1])

if __name__ == '__main__':
    main()