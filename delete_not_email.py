"""
@author: Andile Mbele
@program: delete_not_email.py
"""

import pandas as pd
import re
import sys


def delete_not_email(file):
    df = pd.read_csv(file)
    df = df[df['email'].str.contains(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')]
    # save the new csv file where the original is with the original name and the word 'after_regex' added to the end
    df.to_csv(file + '_after_regex.csv')
    # df.to_csv(file.split('.')[0] + '_after_regex.csv', index=False)


def main():
    delete_not_email(sys.argv[1])


if __name__ == '__main__':
    main()
