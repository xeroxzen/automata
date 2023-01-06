import sys

def json_insert_comma_and_bracket(path):
    '''
    1. Write a script that will normalize a json file by adding a comma after the end of each JSON entry if a comma does not already exist. 
    2. Add a square bracket at the beginning of the first line and a closing bracket on the very last line if they do not exist already.
    '''

    # read the file
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # add a comma after the end of each JSON entry if a comma does not already exist
    new_lines = []
    for line in lines:
        if line[-2] != ',':
            line = line[:-1] + ',\r '

        new_lines.append(line)

    # add a square bracket at the beginning of the first line and a closing bracket on the very last line if they do not exist already
    if new_lines[0][0] != '[':
        new_lines[0] = '[' + new_lines[0]

    if new_lines[-1][-2] != ']':
        new_lines[-1] = new_lines[-1][:-1] + ']\r '

    # save the file where the original file was
    with open(path.replace('.txt', '.json'), 'w', encoding="utf-8") as f:
        f.writelines(new_lines)
        
def main():
    json_insert_comma_and_bracket(sys.argv[1])

if __name__ == '__main__':
    main()