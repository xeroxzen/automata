import os
import glob
import argparse
import pandas as pd

def merge_csv_files(directory):
    # Step 3: List CSV files in the directory
    csv_files = glob.glob(os.path.join(directory, '*.csv'))

    if not csv_files:
        print("No CSV files found in the specified directory.")
        return

    # Initialize an empty DataFrame to store the merged data
    merged_df = None

    # Step 4: Read CSV files into Pandas DataFrames and merge
    for csv_file in csv_files:
        # Step 5: Merge DataFrames based on a common column (e.g., 'userid')
        current_df = pd.read_csv(csv_file)
        
        if merged_df is None:
            merged_df = current_df
        else:
            # Adjust 'on' parameter according to your common column name variations
            merged_df = merged_df.merge(current_df, on='userid', how='outer')

    # Step 7: Save the merged DataFrame to a new CSV file
    output_filename = os.path.join(directory, 'merged_output.csv')
    merged_df.to_csv(output_filename, index=False)

    print(f"Merged data saved to {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge CSV files in a directory.")
    parser.add_argument("directory", help="Directory containing CSV files to merge.")
    args = parser.parse_args()
    
    merge_csv_files(args.directory)
