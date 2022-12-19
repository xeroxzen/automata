import pandas as pd
import json

def json_extractor(json_file, csv_file):
  # Load the JSON file into a Pandas DataFrame
  df = pd.read_json(json_file)

  # Select the columns that contain useful data
  useful_data = df[['name', 'address']]

  # Save the useful data to a CSV file
  useful_data.to_csv(csv_file, index=False)

def main(json_file, csv_file):
  json_extractor(json_file, csv_file)

if __name__ == '__main__':
  main("/path/to/json/file.json", "/path/to/csv/file.csv")
