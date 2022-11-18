"""
A method that takes a csv file as a parameter, and deletes duplicates from the file.
The important duplicates are the ones that have the same name, the same email address, same user id etc.
"""

import pandas as pd
import sys

def delete_duplicate_rows(csv_file):
    """
    $ python3 delete_duplicate_rows.py data.csv
    No duplicates found
    """
    duplicates_to_look_for = ['name', 'email', 'phone_number', 'user_id', 'userid', 'phone']
    df = pd.read_csv(csv_file)
    try:
        for column in duplicates_to_look_for:
            if column in df.columns:
                df.drop_duplicates(subset=column, keep='first', inplace=True)
        df.to_csv(f"{csv_file.split('.')[0]}_removed_duplicates.csv", index=False)
    except KeyError:
        pass
    except Exception as e:
        print(e)    

def main():
    csv_file = sys.argv[1]
    delete_duplicate_rows(csv_file)

if __name__ == '__main__':  
    main()