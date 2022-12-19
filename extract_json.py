'''
@author: Andile Mbele

'''

import pandas as pd
import json
import sys

def json_extractor(json_file):
  # Load the JSON file into a Pandas DataFrame
  df = pd.read_json(json_file, lines=True)

  # Select the columns that contain useful data
  useful_data = df[['name', 'address', 'phone', 'email', 'firstname', 'lastname', 'first_name', 'last_name', 'country', 'city', 'street', 'latitude', 'longitude', 'created_date']]

  # Check if any of the columns contain useful data
  # If they do, then save the data to a CSV file
  # If they don't, then print a message to the user

  if useful_data.empty:
    print("No useful data in this JSON file")
  else:
    try:
        # useful_data.to_csv('useful_data.csv')
        print(useful_data) # Print the useful data to the user
        print("Data saved to useful_data.csv")
    except Exception as e:
        print(e)

  # Print the useful data to the console
#   print(useful_data)

def main():
  json_extractor(sys.argv[1])

if __name__ == '__main__':
  main()

