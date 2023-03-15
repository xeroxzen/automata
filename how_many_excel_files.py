'''
@Author: Google Jr
@program: How many Excel files?
'''

import os
import sys

def count_xcel_files(directory):
    '''
    A simple Python script to count the number of Excel files in a directory and subdirectories.
    '''
    count = 0
    for dire in directory:
        try:
            os.chdir(dire)
            for root, dirs, files in os.walk(dire):
                for file in files:
                    if file.endswith('.xlsx'):
                        count += 1
            return count
        except FileNotFoundError:
            print('Directory not found.')
        except PermissionError:
            print('Permission denied.')
        except OSError:
            print('OS error.')
        except:
            print('Unexpected error.')

    print('Number of Excel files: {}'.format(count))
        
def main():
    '''
    Main function.
    '''
    directory = sys.argv[1:]
    print(count_xcel_files(directory))

if __name__ == '__main__':
    main()