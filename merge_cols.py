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

            print("Select the columns to merge on (e.g., 'id' 'userid'):")
            user_input = input("Enter the columns separated by space: ").strip()
            selected_columns = user_input.split()

            # Check if selected columns exist in common columns
            if not all(col in common_columns for col in selected_columns):
                print("Invalid column selection. Exiting.")
                return

            merge_columns = selected_columns

        merged_df = pd.merge(df1, df2, on=merge_columns, how='outer')

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
            print("Enter the columns to merge on (e.g., 'id' 'userid'):")
            merge_columns_input = input("Enter the columns separated by space (press Enter to use auto-detection): ").strip()
            merge_columns = merge_columns_input.split() if merge_columns_input else None
            merge_csv_files(file1, file2, merge_columns)
