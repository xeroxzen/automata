# Write a script that will normalize a json file by adding a comma after the end of each line if a comma does not already exist. 
# Add a square bracket at the beginning of the first line and a closing bracket on the last line if they do not exist already.

import sys

def json_insert_comma_and_bracket(path):
    '''
    1. Write a script that will normalize a json file by adding a comma after each line and adding a square bracket at the beginning of the first line and a closing bracket on the last line.
    '''

    # read the file
    with open(path, 'r', encoding='latin-1') as f:
        lines = f.readlines()

    # add a comma after each line
    new_lines = []
    for line in lines:
        new_lines.append(line.strip() + ',')
    new_lines[-1] = new_lines[-1].replace(',', '')

    # add a square bracket at the beginning of the first line and a closing bracket on the last line
    new_lines[0] = '[' + new_lines[0]
    new_lines[-1] = new_lines[-1] + ']'

    # save the file where the original file was
    with open(path.replace('.txt', '.json'), 'w', encoding="utf-8") as f:
        f.writelines(new_lines)

def main():
    json_insert_comma_and_bracket(sys.argv[1])

if __name__ == '__main__':
    main()