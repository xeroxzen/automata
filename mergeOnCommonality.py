import pandas as pd
import os


def merge_csv_files(*args, on='userid'):
    """Merges two or more CSV files based on a common column.

    Args:
        *args: A list of CSV file paths.
        on: The common column to merge on.

    Returns:
        A merged Pandas DataFrame.
    """

    dataframes = []
    for file_path in args:
        df = pd.read_csv(file_path)
        dataframes.append(df)

    merged_df = pd.merge(*dataframes, on=on, how="inner")

    return merged_df


def main():
    csv_files = [os.path.join(os.getcwd(), f)
                 for f in os.listdir() if f.endswith('.csv')]

    merged_df = merge_csv_files(*csv_files)

    merged_df.to_csv('merged.csv', index=False)


if __name__ == main():
    main()
