import pandas as pd
import re
import sys


def verify_phone(filename):
    """
    Verify the phone numbers in the "phone" column. Delete any entry that does not qualify as a valid phone number.
    """
    df = pd.read_csv(filename, encoding='utf-8', sep=',', header=0, index_col=False, dtype=str, na_filter=False,
                     keep_default_na=False, low_memory=False)
    # phone number must be between 7 and 15 digits
    df = df[df['phone'].str.contains(r'^[0-9]{7,15}$')]

    print(df.head())

    # save to csv
    df.to_csv(filename, index=False)


def main():
    """
    Main function.
    """
    verify_phone(sys.argv[1])


if __name__ == '__main__':
    main()
