import os
import sys
import pandas as pd

def merge_csv_files(directory):
    # Get list of files in the directory
    files = os.listdir(directory)
    
    # Filter files that match the pattern
    csv_files = [file for file in files if 'db_limeNEW_tokens' in file and file.endswith('.csv')]
    
    if not csv_files:
        print("No matching CSV files found.")
        return
    
    # Read each CSV file and merge them into a single DataFrame
    dfs = []
    for file in csv_files:
        file_path = os.path.join(directory, file)
        df = pd.read_csv(file_path)
        dfs.append(df)
    
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Write merged DataFrame to a new CSV file
    output_file = os.path.join(directory, 'merged_db_limeNEW_tokens.csv')
    merged_df.to_csv(output_file, index=False)
    
    print("Merged CSV file saved to:", output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_csv.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    if not os.path.isdir(directory):
        print("Directory not found.")
        sys.exit(1)
    
    merge_csv_files(directory)
