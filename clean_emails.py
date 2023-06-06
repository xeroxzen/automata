import pandas as pd
import re
import sys


def clean_emails(filename):
    """
    Verify and clean the email addresses in the "email" column of the CSV file.
    """
    try:
        df = pd.read_csv(filename, encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False,
                         keep_default_na=False, low_memory=False)

        # Verify and clean email addresses using regular expressions
        df.loc[~df['email'].str.contains(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', regex=True), 'email'] = ''

        print(df.head())

        # Save the modified DataFrame to a new CSV file
        df.to_csv(filename[:-4] + '_email_cleaned.csv', index=False)
    except Exception as e:
        print(e)


def main():
    """
    Main function.
    """
    clean_emails(sys.argv[1])


if __name__ == '__main__':
    main()
