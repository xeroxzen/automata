import pandas as pd
import json
import sys


def json_extractor(json_file):
    # Load the JSON file into a Pandas DataFrame
    df = pd.read_json(json_file, lines=True)

    # Select the columns that contain useful data
    useful_data = df[['name', 'address']]

    # Save the useful data to a CSV file
    useful_data.to_csv(json_file, index=False)


def main():
    json_extractor(sys.argv[1])


if __name__ == '__main__':
    main()
