import pandas as pd
import tkinter as tk
from tkinter import filedialog

def merge_csv_files(file1, file2, merge_columns=None):
    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        if merge_columns is None:
            root = tk.Tk()
            root.withdraw()

            common_columns = set(df1.columns).intersection(df2.columns)
            common_columns = list(common_columns)

            if not common_columns:
                print("No common columns found for merging.")
                return

            print("Available common columns:", common_columns)
            merge_column1 = input("Enter the first merge column: ")
            merge_column2 = input("Enter the second merge column: ")

            if merge_column1 not in common_columns or merge_column2 not in common_columns:
                print("Invalid column names. Both columns must be present in the common columns.")
                return

            merge_columns = [merge_column1, merge_column2]

        merged_df = pd.merge(df1, df2, left_on=merge_columns[0], right_on=merge_columns[1], how='outer')

        output_filename = "merged_output.csv"
        merged_df.to_csv(output_filename, index=False)

        print(f"Merged data saved to {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

def select_csv_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select a CSV file")
    return file_path

if __name__ == "__main__":
    print("Select the first CSV file:")
    file1 = select_csv_file()
    if not file1:
        print("No file selected. Exiting.")
    else:
        print("Select the second CSV file:")
        file2 = select_csv_file()
        if not file2:
            print("No file selected. Exiting.")
        else:
            merge_csv_files(file1, file2)
