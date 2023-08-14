import pandas as pd
import os

def process_csv_file(file_path):
    """Processes a CSV file in the specified directory.

    Args:
        file_path: The path to the CSV file to process.

    Returns:
        None.
    """

    df = pd.read_csv(file_path)

    # Change the column name "radio11" to "gender".
    df.rename(columns={"radio11": "gender"}, inplace=True)

    # Delete the columns "terms", "eett" and "button7".
    df = df.drop(["terms", "eett", "button7"], axis=1)

    # Combine the "firstname" and "lastname" columns into a single column named "fullname".
    df["fullname"] = df["firstname"] + " " + df["lastname"]

    # Save the processed CSV file.
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Get the directory of the CSV files to process.
    csv_dir_path = os.getcwd()

    # Iterate through all the CSV files in the directory.
    for file in os.listdir(csv_dir_path):
        if file.endswith(".csv"):
            file_path = os.path.join(csv_dir_path, file)
            process_csv_file(file_path)

