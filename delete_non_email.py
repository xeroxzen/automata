'''
@author: Andile Mbele
@program: delete_non_email.py
'''
import pandas as pd
import re   
import sys

def verify_email(filename):
    '''
    Verify the email addresses in the "email" column. Delete any entry that does not qualify as a valid email address.
    '''
    df = pd.read_csv(filename, encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False, keep_default_na=False, low_memory=False)
    # check for multiple columns that may contain email addresses. Example: email, email2, email3, cc_email, from_email, to_email, etc.
    df = df[df['email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')] 
    print(df.head())

    # save to csv
    df.to_csv(filename, index=False)

def main():
    '''
    Main function.
    '''
    verify_email(sys.argv[1])

if __name__ == '__main__':
    main()
