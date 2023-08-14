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

        # Read the CSV file into a Pandas DataFrame.
        df = pd.read_csv(original_file_path)

        # Change the column name "radio11" to "gender".
        df.rename(columns={"radio11": "gender"}, inplace=True)

        # Check if the columns exist.
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

        # Combine the "firstname" and "lastname" columns into a new column called "fullname".
        try:
            if "firstname" in df.columns and "lastname" in df.columns:
                df["fullname"] = df["firstname"] + " " + df["lastname"]
        except KeyError as err:
            print(
                f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")

        # Convert age to integer.
        # try:
        #     if "age" in df.columns:
        #         df["age"] = df["age"].astype(int)
        # except KeyError as err:
        #     print(
        #         f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")
        # Drop the "firstname" and "lastname" columns.
        try:
            df.drop(["firstname", "lastname"], axis=1, inplace=True)
        except KeyError as err:
            print(
                f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")

        # Delete rows with duplicate emails
        try:
            df.drop_duplicates(subset="email", keep="first", inplace=True)
        except KeyError as err:
            print(
                f"Column '{err.args[0]}' does not exist in CSV file '{csv_file_path}'.")

        # Write the deduplicated DataFrame to a new CSV file.
        df.to_csv(deduplicated_file_path, index=False)

        # Move the original CSV file(s) to a new directory within this directory, named cleaned. Put code inside try-except block
        try:
            os.mkdir(os.path.join(directory_path, "cleaned"))
        except FileExistsError:
            pass
        os.rename(original_file_path, os.path.join(
            directory_path, "cleaned", os.path.basename(original_file_path)))

        print(
            f"CSV file '{original_file_path}' has been deduplicated and saved at '{deduplicated_file_path}'.")


if __name__ == "__main__":
    directory_path = sys.argv[1]
    deduplicate_csv_files(directory_path)
