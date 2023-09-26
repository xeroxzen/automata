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
      type merge_columns: object
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

    try:
        data_frames = [pd.read_csv(csv_file) for csv_file in csv_files]

        common_column_found = False

        for merge_column in merge_columns:
            common_rows = [df for df in data_frames if merge_column in df.columns]

            if len(common_rows) >= 2 and any(len(df[df[merge_column].notna()]) > 0 for df in common_rows):
                common_column_found = True
                break

        if not common_column_found:
            print("No common column found or no similarity in rows to merge on.")
            return

        for csv_file, current_df in zip(csv_files, data_frames):
            if merge_column in current_df.columns:
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
