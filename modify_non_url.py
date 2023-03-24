'''
@author: Andile Mbele
@program: modify_non_url.py
'''

import pandas as pd
import re
import sys

def modify_url(filename):
    '''
    Verify the URL addresses in the "url" column. Clear anything that is not a valid URL and leave the row url row blank.
    '''
    try:
        df = pd.read_csv(filename, encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False, keep_default_na=False, low_memory=False)

        # check for columns with url addresses. URLs may not necessarily start with http or https. 
        df.loc[~df['website'].str.contains(r'^(https?://)?(www\.)?([a-zA-Z0-9]+\.)+[a-zA-Z]{2,}(/[^\s]*)?$', regex=True), 'website'] = ''

        print(df.head())

        # save to csv
        df.to_csv(filename[:-4] + '_modified.csv', index=False)
    except Exception as e:
        print(e)

def main():
    '''
    Main function.
    '''
    modify_url(sys.argv[1])

if __name__ == '__main__':
    main()
 
    