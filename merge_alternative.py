import os
import glob
import argparse
import pandas as pd


def merge_csv_files(directory, merge_column=None):
    """Merges two or more CSV files in a directory based on a common column.

    Args:
      directory: The directory containing the CSV files to merge.
      merge_columns: A list of possible columns to merge on. If None, the
        function will try to find a common column to merge on.

    Returns:
      A merged Pandas DataFrame.
    """

    csv_files = glob.glob(os.path.join(directory, '*.csv'))

    if not csv_files:
        print("No CSV files found in the specified directory.")
        return

    if not isinstance(csv_files, list):
        print("CSV files is not a list.")
        return

    # Create a Pandas DataFrame from the first CSV file.
    df = pd.read_csv(csv_files[0])

    # Merge the remaining CSV files with the first CSV file.
    for csv_file in csv_files[1:]:
        current_df = pd.read_csv(csv_file)
        df = df.merge(current_df, on=merge_column,
                      how='outer')

    # Save the merged DataFrame to a new CSV file.
    output_filename = os.path.join(directory, 'merged_output.csv')
    df.to_csv(output_filename, index=False)

    print(f"Merged data saved to {output_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Merge CSV files in a directory.")
    parser.add_argument(
        "directory", help="Directory containing CSV files to merge.")
    parser.add_argument(
        "--merge-columns",
        nargs='+',
        help="A list of possible columns to merge on.")
    args = parser.parse_args()

    merge_csv_files(args.directory, args.merge_columns)
