import pandas as pd
import sys
import os
import glob


def deduplicate_csv_files(directory_path):
    """Deduplicates CSV files in the specified directory.

    Args:
      directory_path: The path to the directory containing the CSV files to deduplicate.
    """

    csv_file_paths = glob.glob(os.path.join(directory_path, "*.csv"))
    for csv_file_path in csv_file_paths:
        original_file_path = csv_file_path
        deduplicated_file_path = os.path.join(
            directory_path, csv_file_path.replace(".csv", "_deduplicated.csv"))

        df = pd.read_csv(original_file_path)

        df.rename(columns={"radio11": "gender"}, inplace=True)

        try:
            if "terms" in df.columns:
                df.drop("terms", axis=1, inplace=True)
            if "eett" in df.columns:
                df.drop("eett", axis=1, inplace=True)
            if "button7" in df.columns:
                df.drop("button7", axis=1, inplace=True)
        except KeyError as err:
            print(
                f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")

        try:
            if "firstname" in df.columns and "lastname" in df.columns:
                df["fullname"] = df["firstname"] + " " + df["lastname"]
        except KeyError as err:
            print(
                f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")

        try:
            df.drop(["firstname", "lastname"], axis=1, inplace=True)
        except KeyError as err:
            print(
                f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")

        try:
            df.drop_duplicates(subset="email", keep="first", inplace=True)
        except KeyError as err:
            print(
                f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")

        df.to_csv(deduplicated_file_path, index=False)

        try:
            os.mkdir(os.path.join(directory_path, "not_cleansed"))
        except FileExistsError:
            pass
        os.rename(original_file_path, os.path.join(
            directory_path, "cleaned", os.path.basename(original_file_path)))

        print(
            f"CSV file '{original_file_path}' has been deduplicated and saved at '{deduplicated_file_path}'.")


if __name__ == "__main__":
    directory_path = sys.argv[1]
    deduplicate_csv_files(directory_path)
