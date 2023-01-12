'''
@author: Andile Jaden Mbele
@date: 12 January 2023
'''

import pandas as pd
import os
import sys

def correspond_with_id():
    """
    This method parses a csv file which has a id column likely with duplicates, other columns are for email and username. For each id, it saves the email and username in a new csv file.
    """
    # Read the csv file into a dataframe
    df = pd.read_csv(sys.argv[1], sep=',', header=0, dtype='object')

    # For each unique id in the original dataframe, save the email and username in the new dataframe
    df = df.groupby('id').agg({'email': 'first', 'username': 'first'}).reset_index()
    
    # Drop the duplicates in the new dataframe
    df = df.drop_duplicates(subset='id', keep='first')

    # Print the first 5 rows of the new dataframe
    print(df.head())

    # Print the number of rows in the new dataframe
    print('Number of rows in the new dataframe: ', len(df))

    # Print the number of unique ids in the new dataframe
    print('Number of unique ids in the new dataframe: ', len(df['id'].unique()))

    # Save the new dataframe as a csv file in the same directory as the original csv file
    df.to_csv(os.path.join(os.path.dirname(sys.argv[1]), 'corresponding_' + os.path.basename(sys.argv[1])), index=False)

def main():
    correspond_with_id()

if __name__ == '__main__':
    main()