import os
import sys
import pandas as pd
import time
from tqdm import tqdm
from collections import Counter


low_memory = False

def extract_database_name(file_path):
    """
    Extracts the database name from a CSV file's path, assuming 
    the database name is one directory behind the 'splitup' directory.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        str: The extracted database name.
        
    >>> extract_database_name('data/splitup/my_database/data.csv')
    'my_database'
    >>> extract_database_name('other_folder/splitup/another_db/file.csv')
    'another_db'
    >>> extract_database_name('no_splitup_here/data.csv')
    None
    """

    path_parts = file_path.split(os.sep)  # Split path into components

    # Find the index of the 'splitup' directory
    for i, part in enumerate(path_parts):
        if part == 'splitup':
            if i > 0: 
                return path_parts[i - 1]  # Previous directory is the database name
            else:
                return None  # 'splitup' at the beginning of the path

    return None  # 'splitup' directory not found


def analyze_csv(file_path):
    """
    Analyzes a CSV file and returns relevant information.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary containing the database name, total column count, 
              column names, and None for similarity (calculated later).
              
    >>> analyze_csv('data/splitup/my_database/data.csv')['column_count']
    3  # Assuming the CSV has 3 columns

    """

    try:
       df = pd.read_csv(file_path, dtype='object', encoding='utf-8')
    except ValueError:
         df = pd.read_csv(file_path, low_memory=low_memory)
         df['column4'] = pd.to_numeric(df['column4'], errors='coerce')

    return {
        'database': extract_database_name(file_path),
        'column_count': len(df.columns),
        'column_names': list(df.columns),
        'similarity': None  
    }


def calculate_similarity(df1, df2):
    """
    Calculates the percentage similarity between two DataFrames.
    Assumes DataFrames have the same column names.

    Args:
        df1 (pd.DataFrame): The first DataFrame.
        df2 (pd.DataFrame): The second DataFrame.

    Returns:
        float: The percentage similarity between 0 and 100.
        
    >>> import numpy as np
    >>> df1 = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['A', 'B'])
    >>> df2 = pd.DataFrame(np.array([[1, 2], [5, 6]]), columns=['A', 'B'])
    >>> calculate_similarity(df1, df2)
    50.0
    """

    matching_rows = df1.eq(df2).sum().sum()  # Count matching values
    total_cells = df1.size  # Total number of cells in either DataFrame

    return (matching_rows / total_cells) * 100

def show_progress_bar(iterable, desc="", **kwargs):
    """
    A wrapper around tqdm to display a progress bar.

    Args:
        iterable: An iterable object.
        desc (str): Description to display on the progress bar.
        kwargs: Additional keyword arguments for tqdm.
    """

    return tqdm(iterable, desc=desc, **kwargs)

def process_directory(directory_path):
    """
    Processes CSV files within a directory with an 'output' subdirectory.

    Args:
        directory_path (_type_): _description_
    """
    

def calculate_and_print_results(csv_data):
    """
    Calculates the similarity between CSV files and prints the results.

    Args:
        csv_data (list): A list of dictionaries containing CSV data.
    """

    # Count the number of unique databases
    unique_databases = Counter(csv['database'] for csv in csv_data)
    num_unique_databases = len(unique_databases)

    # Print the number of unique databases
    print(f"\nNumber of unique databases: {num_unique_databases}\n")

    # Iterate over all pairs of CSV files
    for i, csv1 in show_progress_bar(enumerate(csv_data), desc="Comparing CSV files", total=len(csv_data)):
        for j, csv2 in enumerate(csv_data[i + 1:], i + 1):
            # Calculate similarity between the two CSV files
            similarity = calculate_similarity(csv1['df'], csv2['df'])
            csv1['similarity'][csv2['database']] = similarity
            csv2['similarity'][csv1['database']] = similarity

    # Print the results
    for csv in csv_data:
        print(f"Database: {csv['database']}")
        print(f"Total columns: {csv['column_count']}")
        print(f"Column names: {csv['column_names']}")
        print("Similarity:")
        for database, similarity in csv['similarity'].items():
            print(f"  {database}: {similarity:.2f}%")
        print()
        
if __name__ == "__main__":
    # Get the path to the directory containing CSV files
    directory = sys.argv[1]

    # Get all CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    # Analyze each CSV file
    csv_data = []
    for csv_file in show_progress_bar(csv_files, desc="Analyzing CSV files"):
        file_path = os.path.join(directory, csv_file)
        csv_data.append({
            'file': csv_file,
            'df': pd.read_csv(file_path, low_memory=low_memory),
            **analyze_csv(file_path)
        })

    # Calculate and print the results
    calculate_and_print_results(csv_data)
