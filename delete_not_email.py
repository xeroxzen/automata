

"""
@author: Andile Mbele


1. Write a python script that takes a CSV file as input, look through the email column and delete the rows that do not have data that looks like an email address. The script should output a new CSV file with the rows that have valid email addresses. Use regular expressions to validate the email addresses.
2. Use Pandas
"""

import pandas as pd
import re
import sys

def delete_not_email(file):
    df = pd.read_csv(file)
    df = df[df['email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')]
    # save the new csv file with the original name and the word 'after_regex' added to the end
    df.to_csv(file.split('.')[0] + '_after_regex.csv', index=False)

def main():
    delete_not_email(sys.argv[1])

if __name__ == '__main__':
    main()   

