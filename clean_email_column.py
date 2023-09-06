import pandas as pd
import sys


def clean_csv_column(csv_file):
    """Cleans the s_extra column in a csv file and leaves only a clean email in the rows.

    Args:
      csv_file: The path to the csv file to clean.

    Returns:
      A pandas DataFrame with the cleaned s_extra column.
    """

    df = pd.read_csv(csv_file)

    # Extract the email from the s_extra column.
    df['email'] = df['s_extra'].str.split('|').str[2]

    # Clean the email addresses.
    df['email'] = df['email'].str.replace('@hotmail.com', '@gmail.com')

    # Convert the email to an integer.
    df['email_int'] = df['email'].apply(int)

    # Remove the s_extra column.
    df = df.drop('s_extra', axis=1)

    # Keep only emails with at least 5 characters.
    df = df[df['email_int'] >= 5]

    return df


if __name__ == '__main__':
    csv_file = sys.argv[1]
    df = clean_csv_column(csv_file)
    df.to_csv(csv_file, index=False)
