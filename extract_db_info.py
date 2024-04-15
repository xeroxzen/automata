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

def main(root_directory):
    """
    Main function to coordinate analysis.

    Args:
        root_directory (str): The root directory to start searching for CSV files.
    """

    csv_data = []

    # Traverse directories and analyze CSV files
    for root, dirs, files in os.walk(root_directory):
        print(f"Analyzing directory: {root}")
        if 'output' in dirs: # Checking if output is among the subdirectories
            output_dir = os.path.join(root, 'output')
            for file in show_progress_bar(files, desc=f"Analyzing directory: {root}"):
                if file.endswith('.csv'):
                    file_path = os.path.join(output_dir, file)
                    csv_data.append(analyze_csv(file_path))
            

    # Calculate similarities
    database_groups = {}
    for item in csv_data:
        database_name = item['database']
        if database_name not in database_groups:
            database_groups[database_name] = []
        database_groups[database_name].append(item)

    for database, items in show_progress_bar(database_groups.items(), desc="Calculating similarities"):
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                df1 = pd.read_csv(os.path.join(root_directory, items[i]['database'], 'output', items[i]['filepath']))
                df2 = pd.read_csv(os.path.join(root_directory, items[j]['database'], 'output', items[j]['filepath']))
                similarity = calculate_similarity(df1, df2)
                items[i]['similarity'] = similarity
                items[j]['similarity'] = similarity

    # Print or store the results (modify this as needed)
    print(csv_data)
    
    # Print Results
    print("*** Analysis Results ***")  

    # Total Column Counts per 'output' Directory
    for root, dirs, files in os.walk(root_directory):
        if 'output' in dirs:
            output_dir = os.path.join(root, 'output')
            total_columns = sum(item['column_count'] for item in csv_data if item['database'] == os.path.basename(root))
            print(f"Directory '{output_dir}': Total Columns = {total_columns}")

    # Most Common Columns 
    all_columns = [col for item in csv_data for col in item['column_names']]
    most_common = Counter(all_columns).most_common()
    print("\nMost Common Columns:")
    for col, count in most_common:  
        print(f"- {col} ({count} occurrences)")

    # Percentage Matches (assuming within the same database)
    print("\nSimilarity Matches (within Databases):")
    for item in csv_data:
        if item['similarity'] is not None:
            print(f"{item['filepath']}: {item['similarity']}%")

# ----------------------------------------------- 
# How to use:

root_directory = sys.argv[1]

# 2. Run the script
main(root_directory)
