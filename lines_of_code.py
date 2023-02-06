'''
@author: Google Jr
program: How many lines of code?
'''

import os
import sys

def count_lines_of_code(directory):
    count = 0
    for dire in directory:
        try:
            os.chdir(dire)
            for root, dirs, files in os.walk(dire):
                for file in files:
                    if file.endswith('.py'):
                        with open(file, 'r', encoding='utf-8') as f:
                            for line in f:
                                if line.strip() and not line.startswith(('#', '"""', "'''", 'r"""')):
                                    count += 1
            return count
        except Exception as e:
            print(f'Error: {e}')

def main():
    directory = sys.argv[1:]
    print(f'\nNumber of lines of code: {count_lines_of_code(directory)}')

if __name__ == '__main__':
    main()
