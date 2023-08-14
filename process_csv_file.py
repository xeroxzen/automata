import pandas as pd
import sys

def deduplicate_csv_files(directory_path):
  """Deduplicates CSV files in the specified directory.

  Args:
    directory_path: The path to the directory containing the CSV files to deduplicate.
  """

  for file_name in sys.argv[1:]:
    if file_name.endswith(".csv"):
      original_file_path = os.path.join(directory_path, file_name)
      deduplicated_file_path = os.path.join(
          directory_path, file_name.replace(".csv", "_deduplicated.csv"))

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
        print(f"Column '{err.args[0]}' does not exist in CSV file '{file_name}'.")

      # Combine the "firstname" and "lastname" columns into a new column called "fullname".
      df["fullname"] = df["firstname"] + " " + df["lastname"]

      # Drop the "firstname" and "lastname" columns.
      try:
        df.drop(["firstname", "lastname"], axis=1, inplace=True)
      except KeyError as err:
        print(f"Column '{err.args[0]}' does not exist in CSV file '{file_name}'.")

      # Write the deduplicated DataFrame to a new CSV file.
      df.to_csv(deduplicated_file_path, index=False)

if name == "__main__":
  directory_path = sys.argv[1]
  deduplicate_csv_files(directory_path)
