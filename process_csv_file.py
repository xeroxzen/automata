import pandas as pd
import os

def deduplicate_csv_files(directory_path):
  """Deduplicates CSV files in the specified directory.

  Args:
    directory_path: The path to the directory containing the CSV files to deduplicate.
  """

  for file_name in os.listdir(directory_path):
    if file_name.endswith(".csv"):
      original_file_path = os.path.join(directory_path, file_name)
      deduplicated_file_path = os.path.join(
          directory_path, file_name.replace(".csv", "_deduplicated.csv"))

      df = pd.read_csv(original_file_path)

      df.rename(columns={"radio11": "gender"}, inplace=True)

      if "terms" in df.columns:
        df.drop("terms", axis=1, inplace=True)
      if "eett" in df.columns:
        df.drop("eett", axis=1, inplace=True)
      if "button7" in df.columns:
        df.drop("button7", axis=1, inplace=True)

      df["fullname"] = df["firstname"] + " " + df["lastname"]

      df.drop(["firstname", "lastname"], axis=1, inplace=True)

      df.to_csv(deduplicated_file_path, index=False)

if __name__ == "__main__":
  directory_path = os.getcwd()
  deduplicate_csv_files(directory_path)
