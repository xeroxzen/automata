import pandas as pd
import sys
import os

def merge_csv_files(directory):
  """
  Merges all CSV files in a directory based on similar columns.

  Args:
      directory: The directory containing the CSV files.
  """
  # Get a list of all CSV files in the directory
  csv_files = [f for f in os.listdir(directory) if f.endswith(".csv")]

  # Initialize an empty DataFrame to store the merged data
  merged_df = pd.DataFrame()

  # Iterate through each CSV file
  for filename in csv_files:
    # Read the CSV file
    df = pd.read_csv(os.path.join(directory, filename))

     # Get the intersection of columns between "on" list and actual columns in the file
    common_cols = list(set(merged_df.columns) & set(df.columns) & set(["id", "email", "tel", "created","age", "gender", "fullname", "area", "uniq_id"]))

    if not common_cols:
        print(f"Skipping file {filename} due to no common columns.")
        continue
    
    # Merge the DataFrame with the accumulated data, keeping all rows (inner join)
    merged_df = pd.merge(merged_df, df, how="inner", on=common_cols)

  # Save the merged DataFrame to a new CSV file with "_combined.csv" appended
  merged_df.to_csv(os.path.join(directory, "merged_data_combined.csv"), index=False)

# Get the directory path from the command line argument
directory = sys.argv[1]

# Run the merge function
merge_csv_files(directory)

print("CSV files merged successfully!")
