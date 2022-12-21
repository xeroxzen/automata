# Path: change_separator.py

import sys

def change_separator(path):
    '''
    1. Write a python script that loads a csv or txt file and changes the separator to a comma.
    2. The script should check if the file uses a pipe, semicolon or tab as a separator.
    3. Change the separator to a comma and save the file as a csv file.
    '''

    # read the file
    with open(path, 'r') as f:
        lines = f.readlines()

    # check the separator
    if '|' in lines[0]:
        separator = '|'
    elif ';' in lines[0]:
        separator = ';'
    elif '\t' in lines[0]:
        separator = '\t'
    else:
        print('Unknown separator')
        return

    # change the separator
    new_lines = []
    for line in lines:
        new_lines.append(line.replace(separator, ','))

    # save the file where the original file was
    with open(path.replace('.txt', '.csv'), 'w') as f:
        f.writelines(new_lines)

def main():
    change_separator(sys.argv[1])

if __name__ == '__main__':
    main()



    