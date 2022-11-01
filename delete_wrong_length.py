'''
@author: Andile Mbele
program: delete_wrong_length.py
time: Tue 01 Nov 2022
'''

import os
import sys

def delete_wrong_length(directory):
    for filename in os.listdir(directory):
        if 'wrong_length' in filename:
            try:
                os.remove(os.path.join(directory, filename))
                print(f"Deleted {filename}")
            except Exception as e:
                print(e)

if __name__ == '__main__':
    delete_wrong_length(sys.argv[1])