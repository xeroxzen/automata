# In a directory with csv files, this method returns a list of csv files that have customer_id

import pandas as pd
import glob


def customer_id_col():
    '''
    In a directory with csv files, this method returns a list of csv files that have customer_id
    '''
    # Get the list of csv files in the directory
    csv_files = glob.glob('*.csv')
    # Initialize a list to store the csv files that have customer_id
    customer_id_csv_files = []
    # For each csv file in the directory
    for csv_file in csv_files:
        # Read the csv file into a dataframe
        df = pd.read_csv(csv_file, sep=',', header=0, dtype='object')
        # If the dataframe has customer_id column
        if 'customer_id' in df.columns:
            # Append the csv file to the list
            customer_id_csv_files.append(csv_file)
    # Return the list of csv files that have customer_id
    return customer_id_csv_files


def matching_columns():
    """
    This method compares the columns of two csv files and returns the matching columns
    """
    # Get the list of csv files that have customer_id
    customer_id_csv_files = customer_id_col()
    # Initialize a list to store the matching columns
    matched_columns = []
    # For each csv file in the list
    for csv_file in customer_id_csv_files:
        # Read the csv file into a dataframe
        df = pd.read_csv(csv_file, sep=',', header=0, dtype='object')
        # If the dataframe has customer_id column
        if 'customer_id' in df.columns:
            # Append the customer_id column to the list
            matched_columns.append('customer_id')

    # Return the list of matching columns
    return matched_columns


def main():
    print(matching_columns())


if __name__ == '__main__':
    main()
