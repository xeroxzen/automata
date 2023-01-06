import pandas as pd
import os
import sys

def remove_extra_quotes():
    """
    Remove extra quotes from a key:value pair in a json string. Target a specific column in the csv file and clean it up.
    """

    # Read the csv file passed as an argument
    df = pd.read_csv(sys.argv[1])

    # Find the column that has dictionary data in it
    json_column = df.columns[df.columns.str.contains('info')]

    # Convert the json data in the column to a string
    df[json_column] = df[json_column].astype(str)

    # Remove the extra quotes from the json string
    df[json_column] = df[json_column].replace('"', '')

    # Print the first 5 rows of the dataframe
    print(df)

    # Write the cleaned up dataframe as it is printed in df.head() without the extra quotes to a csv file and save it in the same directory as the original csv file
    df.to_csv(os.path.join(os.path.dirname(sys.argv[1]), 'cleaned_' + os.path.basename(sys.argv[1])), index=False)

if __name__ == '__main__':
    remove_extra_quotes()

