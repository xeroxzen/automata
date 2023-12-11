"""
@author: xeroxzen
@program: clean nested dictionary
"""
    
import pandas as pd
import re

# Sample DataFrame
data = {'phone_column': ['a:7:{i:0;s:160:"{""VALUE_TYPE"":""MOBILE"",""ID"":""undefined_72439"",""TYPE_ID"":""PHONE"",""VALUE"":{""VALUE_TYPE"":""MOBILE"",""VALUE"":""+79777290580"",""ID"":""undefined_32026"",""TYPE_ID"":""PHONE""}}"";i:1;s:160:"{""VALUE_TYPE"":""MOBILE"",""ID"":""undefined_90075"",""TYPE_ID"":""PHONE"",""VALUE"":{""VALUE_TYPE"":""MOBILE"",""VALUE"":""+79777290580"",""ID"":""undefined_80006"",""TYPE_ID"":""PHONE""}}"";i:2;s:160:"{""VALUE_TYPE"":""MOBILE"",""ID"":""undefined_76541"",""TYPE_ID"":""PHONE"",""VALUE"":{""VALUE_TYPE"":""MOBILE"",""VALUE"":""+79777290580"",""ID"":""undefined_84110"",""TYPE_ID"":""PHONE""}}"";i:3;s:160:"{""VALUE_TYPE"":""MOBILE"",""ID"":""undefined_50360"",""TYPE_ID"":""PHONE"",""VALUE"":{""VALUE_TYPE"":""MOBILE"",""VALUE"":""+79777290580"",""ID"":""undefined_23968"",""TYPE_ID"":""PHONE""}}"";i:4;s:160:"{""VALUE_TYPE"":""MOBILE"",""ID"":""undefined_45176"",""TYPE_ID"":""PHONE"",""VALUE"":{""VALUE_TYPE"":""MOBILE"",""VALUE"":""+79777290580"",""ID"":""undefined_89721"",""TYPE_ID"":""PHONE""}}"";i:5;s:160:"{""VALUE_TYPE"":""MOBILE"",""ID"":""undefined_46739"",""TYPE_ID"":""PHONE"",""VALUE"":{""VALUE_TYPE"":""MOBILE"",""VALUE"":""+79777290580"",""ID"":""undefined_49031"",""TYPE_ID"":""PHONE""}}"";i:6;s:160:"{""VALUE_TYPE"":""MOBILE"",""ID"":""undefined_81260"",""TYPE_ID"":""PHONE"",""VALUE"":{""VALUE_TYPE"":""MOBILE"",""VALUE"":""+79777290580"",""ID"":""undefined_16272"",""TYPE_ID"":""PHONE""}}"";}']}

df = pd.DataFrame(data)

# Function to extract phone numbers using regular expressions
def extract_phone_number(text):
    phone_match = re.search(r'\+[\d]+', text)
    if phone_match:
        return phone_match.group()
    return None
    