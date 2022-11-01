# Write a script that deletes all files with wrong_length in the filename from the current directory.

import os, shutil

def delete_wrong_length():
    for filename in os.listdir('.'):
        if 'wrong_length' in filename:
            shutil.move(filename, 'wrong_length_files')


if __name__ == '__main__':
    delete_wrong_length()