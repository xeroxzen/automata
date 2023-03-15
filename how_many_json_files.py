'''
@Author: Google Jr
@program: How many Excel files?
'''

import os
import sys

def count_json_files(directory):
    '''
    A simple Python script to count the number of Json files in a directory and subdirectories.
    '''
    count = 0
    for dire in directory:
        try:
            os.chdir(dire)
            for root, dirs, files in os.walk(dire):
                for file in files:
                    if file.endswith('.json'):
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

    print('Number of Json files: {}'.format(count))
        
def main():
    '''
    Main function.
    '''
    directory = sys.argv[1:]
    print(count_json_files(directory))

if __name__ == '__main__':
    main()