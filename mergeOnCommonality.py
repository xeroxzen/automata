import pandas as pd
import os
import sys


def merge_csv_files(input_directory):
    """Merges two or more CSV files based on a common column.

    Args:
        *args: A list of CSV file paths.
        on: The common column to merge on.

    Returns:
        A merged Pandas DataFrame.
    """

    # Step 1: Identify csv files in the dir
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Alert if files less than 2 files in the directory
    if len(csv_files) < 2:
        print("Not enough CSV files to merge.")
        return
    
    # Step 2: Read the first csv file to determine columns in there
    
