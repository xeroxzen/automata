# Write a script that deletes all files with wrong_length in the filename from the current directory.
# The script should take one argument, the directory to search, and print the names of the files it has deleted.

import os
import sys

def delete_wrong_length(directory):
    for filename in os.listdir(directory):
        if 'wrong_length' in filename:
            print(filename)
            os.remove(filename)

if __name__ == '__main__':
    delete_wrong_length(sys.argv[1])