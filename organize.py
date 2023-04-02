import os
import sys
import shutil


def categorise(path):
    # get the list of files in the directory
    files = os.listdir(path)
    # loop through the files
    for file in files:
        # get the file extension
        file_extension = file.split('.')[-1]
        # create the subdirectory if it does not exist
        if not os.path.exists(path + '/' + file_extension + '_files'):
            os.mkdir(path + '/' + file_extension + '_files')
        # move the file to the subdirectory
        shutil.move(path + '/' + file, path + '/' + file_extension + '_files')


def main():
    categorise(sys.argv[1])


if __name__ == '__main__':
    main()
