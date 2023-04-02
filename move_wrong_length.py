"""
@author: Andile Mbele
program: move_wrong_length.py
time: Tue 8th Nov 2022
"""

import os
import sys


def move_wrong_length(directory):
    """
    Loop through files in a directory, move all files that have wrong_length in them to Wrong Length folder if it exists, else create it and move the files there
    """

    if not os.path.exists(directory + '/Wrong Length'):
        os.makedirs(directory + '/Wrong Length')

    for filename in os.listdir(directory):
        if 'wrong_length' in filename:
            try:
                # move files to Wrong Length folder 
                os.rename(directory + '/' + filename, directory + '/Wrong Length/' + filename)
                print(f"Moved {filename} to Wrong Length")
            except Exception as e:
                print(e)
    else:
        print("No files to move")


def main():
    move_wrong_length(sys.argv[1])


if __name__ == '__main__':
    main()
