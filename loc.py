'''
@author: Google Jr
program: How many lines of code?
'''
import os
import sys

def count_lines_of_code(directory):
    # Count the number of lines of code in a directory and subdirectories.
    count = 0
    for dire in directory:
        try:
            os.chdir(dire)
            for root, dirs, files in os.walk(dire):
                for file in files:
                    if file.endswith('.py'):
                        with open(file) as f:
                            for line in f:
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

def main():
    directory = sys.argv[1:]
    print(f'Number of lines of code: {count_lines_of_code(directory)}')

if __name__ == '__main__':
    main()