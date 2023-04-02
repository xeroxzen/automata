# Write a script that will look across columns of a csv file, and if it finds a value that has json format data,
# split it into multiple columns.

# For example, if the csv file has a column called "meta_value" and the value in that column is {"first_name":
# "John", "last_name": "Doe", "age": 25}, then the script should split that column into three columns: "first_name",
# "last_name", and "age", and populate the values in those columns.

# The script should be able to handle any number of columns that have json format data.

import pandas as pd
import sys


def dict_col_to_multi_cols(df, column_with_dictionary):
    from ast import literal_eval
    df[column_with_dictionary] = df[column_with_dictionary].fillna('{}')
    df[column_with_dictionary] = df[column_with_dictionary].apply(literal_eval)
    df = df.join(pd.json_normalize(df.pop(column_with_dictionary)),
                 lsuffix='_left', rsuffix='_right')
    return df


df = pd.read_csv(
    r"C:\\Users\\andile.mbele\\Desktop\\prescient\\Databases\\3rd Batch\\Extracted\\20 more sql db by leakbase ["
    r"chucky]_2022-08-07\\SqlConversions\\dev01.lead-iq.comt\\dev01.lead-iq.comt - leads_old_28_01_fromsql_cleaned.csv",
    dtype='object', sep=';', low_memory=False)

col_with_dict = 'formdata'


def main():
    dict_col_to_multi_cols(df, col_with_dict)


if __name__ == "__main__":
    main()
