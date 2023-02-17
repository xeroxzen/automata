'''
Problem: Mess CSV file with email rows along with nonsense rows. Clean the rows and retain proper email rows.

Example: ["\u041e\u043a\u0441\u0430\u043d\u0430 \u0411\u043b\u043e\u0445\u0438\u043d\u0430<ksenya1985@inbox.ru>"]

Solution: Use regex to clean the rows and retain proper email rows. For example the above row should be cleaned to ksenya1985@inbox.ru
'''

import pandas as pd
import re
import sys

def clean_email_rows(filename):
    '''
    Use regex to clean the rows and retain proper email rows. For example the above row should be cleaned to ksenya1985@inbox.ru
    '''
    df = pd.read_csv(filename, encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False, keep_default_na=False, low_memory=False)

    # check for multiple columns that may contain email addresses. Example: email, email2, email3, cc_email, from_email, to_email, etc.
    # # df['from_email'] = df['from_email'].str.replace(r'[\[\]]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'["]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\[\]]', '')
    df['to_email'] = df['to_email'].str.replace(r'["]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\[\]]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'["]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    # # df['from_email'] = df['from_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['to_email'] = df['to_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')
    df['cc_email'] = df['cc_email'].str.replace(r'[\u0410-\u042f\u0430-\u044f]', '')

    # remove rows that do not contain email addresses
    # df = df[df['from_email'].str.contains(r'[\w\.-]+@[\w\.-]+', regex=True)]
    df = df[df['to_email'].str.contains(r'[\w\.-]+@[\w\.-]+', regex=True)]
    df = df[df['cc_email'].str.contains(r'[\w\.-]+@[\w\.-]+', regex=True)]

    # remove rows that contain email addresses that are not valid
    # df = df[df['from_email'].str.contains(r'[\w\.-]+@[\w\.-]+', regex=True)]
    df = df[df['to_email'].str.contains(r'[\w\.-]+@[\w\.-]+', regex=True)]
    df = df[df['cc_email'].str.contains(r'[\w\.-]+@[\w\.-]+', regex=True)]

    print(df.head())

    # create a list of all the email addresses
    # # from_email_list = df['from_email'].tolist()
    to_email_list = df['to_email'].tolist()
    cc_email_list = df['cc_email'].tolist()

    # save the list of email addresses to a csv file    
    # with open('from_email_list.csv', 'w') as f:
        # for item in from_email_list:
            # f.write("%s " % item)
    with open('to_email_list.csv', 'w') as f:
        for item in to_email_list:
            f.write("%s " % item)
    with open('cc_email_list.csv', 'w') as f:
        for item in cc_email_list:
            f.write("%s " % item)

    df.to_csv('email_list.csv', index=False)

def main():
    clean_email_rows(sys.argv[1])

if __name__ == '__main__':
    main()