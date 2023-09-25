import os
import glob
import argparse
import pandas as pd


def merge_csv_files(directory, merge_columns=None):
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

    merged_df = None

    if merge_columns is None:
        merge_columns = []
        for csv_file in csv_files:
            current_df = pd.read_csv(csv_file)
            merge_columns.extend(current_df.columns)
        merge_columns = set(merge_columns)

    for merge_column in merge_columns:
        if all(merge_column in df.columns for df in csv_files):
            break
    else:
        print("No common column found to merge on.")
        return

    try:
        for csv_file in csv_files:
            current_df = pd.read_csv(csv_file)

            if merged_df is None:
                merged_df = current_df
            else:
                merged_df = merged_df.merge(
                    current_df, on=merge_column, how='outer')
    except AttributeError as e:
        print(f"Error: {e}")
        return

    output_filename = os.path.join(directory, 'merged_output.csv')
    merged_df.to_csv(output_filename, index=False)

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
