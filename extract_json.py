'''
@author: Andile Mbele

'''

import pandas as pd
import json
import sys

def json_extractor(json_file):
  # Load the JSON file into a Pandas DataFrame
  df = pd.read_json(json_file)

  # Select the columns that contain useful data
  useful_data = df[['name', 'address', 'phone', 'email', 'firstname', 'lastname', 'first_name', 'last_name', 'country', 'city', 'street', 'latitude', 'longitude', 'created_date']]

  # Print the useful data to the console
  print(useful_data)

def main():
  json_extractor(sys.argv[1])

if __name__ == '__main__':
  main()

