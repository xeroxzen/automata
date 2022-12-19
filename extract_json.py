'''
@author: Andile Mbele

'''

import pandas as pd

def extract_json():
    # Load the JSON file into a Pandas DataFrame
    df = pd.read_json('data.json')

    # Select only the columns that contain personal identifiable information
    useful_columns = ['name', 'address', 'email', 'phone', 'country', 'city', 'street', 'latitude', 'longitude']
    df = df[useful_columns]

    # Print the extracted data to the console
    print(df)
