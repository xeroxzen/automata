'''
@author: Andile Mbele
program: move_wrong_length.py
time: Tue 8th Nov 2022
'''

# Loop through files in a directory, move all files that have wrong_length in them to Wrong Length folder if it exists, else create it and move the files there

import os
import sys

def move_wrong_length(directory):
    '''
    $ python move_wrong_length.py /path/to/directory
    Moved cabfoods.co.za - wp_followup_customers_wrong_length.txt to Wrong Length
    Moved cabfoods.co.za - tbtlclients_wrong_length_cleaned.txt to Wrong Length
    Moved cabfoods.co.za - tbtlcustomers_wrong_length.txt to Wrong Length
    Moved cabfoods.co.za - wp_dusers_wrong_length_cleaned.txt to Wrong Length
    Moved cabfoods.co.za - tbtlorders_wrong_length.txt to Wrong Length
    Moved cabfoods.co.za - wp_posts_wrong_length_cleaned.txt to Wrong Length
    Moved cabfoods.co.za - wp_posts_wrong_length.txt to Wrong Length
    Moved cabfoods.co.za - wp_comments_wrong_length_cleaned.txt to Wrong Length
    No files to move
    '''
    for filename in os.listdir(directory):
        if 'wrong_length' in filename:
            try:
                os.rename(os.path.join(directory, filename), os.path.join(directory, 'Wrong Length', filename))
                print(f"Moved {filename} to Wrong Length")
            except Exception as e:
                print(e)
    else:
        print("No files to move")