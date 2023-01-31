# Count the number of CSV files in a directory and subdirectories.

import os
import sys

def count_csv_files(directory):
    # Count the number of CSV files in the computer.
    count = 0
    for dire in directory:
        try:
            os.chdir(dire)
            for root, dirs, files in os.walk(dire):
                for file in files:
                    if file.endswith('.csv'):
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

    print('Number of CSV files: {}'.format(count))

def main():
    '''
    Main function.
    '''
    directory = sys.argv[1:]
    print(count_csv_files(directory))

if __name__ == '__main__':
    main()