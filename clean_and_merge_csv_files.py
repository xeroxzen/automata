import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select the directory containing CSV files")
    return directory

def find_common_columns(dataframes):
    # Identify common columns among dataframes
    common_columns = set(dataframes[0].columns)
    for df in dataframes[1:]:
        common_columns &= set(df.columns)
    return list(common_columns)

def clean_and_merge_csv(directory, common_columns):
    # Load and clean CSV files
    dataframes = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            # Clean and preprocess the data if necessary
            dataframes.append(df)
    
    if not dataframes:
        print("No CSV files found in the directory.")
        return
    
    # Find common columns
    if not common_columns:
        common_columns = find_common_columns(dataframes)
    
    if not common_columns:
        print("No common columns found among CSV files.")
        return

    # Merge dataframes based on common columns
    merged_df = pd.concat(dataframes, axis=0, ignore_index=True)

    # Save the merged data to a new CSV file
    merged_filename = os.path.join(directory, "merged_data.csv")
    merged_df.to_csv(merged_filename, index=False)
    print(f"Merged data saved to {merged_filename}")

def main():
    directory = select_directory()
    if not directory:
        print("No directory selected. Exiting.")
        return
    
    common_columns = []

    def set_common_columns():
        nonlocal common_columns
        common_columns = entry.get().split(',')
        root.destroy()

    root = tk.Tk()
    root.title("CSV File Merger")
    tk.Label(root, text="Enter common columns separated by commas (e.g., userid,user_id,customer id):").pack()
    entry = tk.Entry(root)
    entry.pack()
    tk.Button(root, text="Merge", command=set_common_columns).pack()
    root.mainloop()

    clean_and_merge_csv(directory, common_columns)

if __name__ == "__main__":
    main()
