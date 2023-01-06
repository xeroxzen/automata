# Write a python script that will take a csv file as an argument and clean it up. The script should do the following:
# look for any columns that have json/dictionary data in them.
# If the column has json/dictionary data in it, then the script should convert the json/dictionary data into a string.
# look for PII(firstname, lastname, email, created_at,  middle_name, password etc) in the specified columns and created a new column for each of the PII columns and populate the new column with the PII data.
# Correspond the PII data with the customer_id column.
# Write the cleaned csv file to the same directory as the original csv file.
# Print out the number of rows that were deleted.

# Path: clean_json.py

import pandas as pd
import os
import sys
import json
import re

def clean_json():
    """"
    Clean up the info column in the file
    """

    