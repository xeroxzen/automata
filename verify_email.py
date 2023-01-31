'''
@author: Andile Mbele
@program: verify_email.py
'''

import csv
import re
import sys

def verify_email(filename):
    '''
    Verify the email addresses in the "email" column. Delete any entry that does not qualify as a valid email address.
    '''
    with open(filename, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', row['email']):
                print(row['email'])
            else:
                print(f'Invalid email address: {row["email"]}')

def main():
    '''
    Main function.
    '''
    verify_email(sys.argv[1])

if __name__ == '__main__':
    main()