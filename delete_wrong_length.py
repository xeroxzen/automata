'''
@author: Andile Mbele
program: delete_wrong_length.py
time: Tue 01 Nov 2022
'''

import os
import sys

def delete_wrong_length(directory):
    '''
    $ python delete_wrong_length.py /path/to/directory
    Deleted cabfoods.co.za - wp_followup_customers_wrong_length.txt
    Deleted cabfoods.co.za - tbtlclients_wrong_length_cleaned.txt
    Deleted cabfoods.co.za - tbtlcustomers_wrong_length.txt
    Deleted cabfoods.co.za - wp_dusers_wrong_length_cleaned.txt
    Deleted cabfoods.co.za - tbtlorders_wrong_length.txt
    Deleted cabfoods.co.za - wp_posts_wrong_length_cleaned.txt
    Deleted cabfoods.co.za - wp_posts_wrong_length.txt
    Deleted cabfoods.co.za - wp_comments_wrong_length_cleaned.txt
    No files to delete

    $ python delete_wrong_length.py /path/to/directory
    No files to delete
    '''
    for filename in os.listdir(directory):
        if 'wrong_length' in filename:
            try:
                os.remove(os.path.join(directory, filename))
                print(f"Deleted {filename}")
            except Exception as e:
                print(e)
    else:
        print("No files to delete")

if __name__ == '__main__':
    delete_wrong_length(sys.argv[1])