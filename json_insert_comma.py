import sys

def json_insert_comma_add_bracket(path):
    '''
    Write a script that will normalize a json file by adding a comma after the end of each json entry if a comma does not already exist. 
    Add a square bracket at the beginning of the first line and a closing bracket on the last line if they do not exist already.
    '''

    # read the file
    with open(path, 'r', encoding='latin-1') as f:
        lines = f.readlines()

    # add a comma after the end of each line if a comma does not already exist
    new_lines = []
    for line in lines:
        if line[-2] != ',':
            new_lines.append(line[:-1] + ',\r ')
        else:
            new_lines.append(line)

    # add a square bracket at the beginning of the first line and a closing bracket on the last line if they do not exist already
    if new_lines[0][0] != '[':
        new_lines[0] = '[' + new_lines[0]
        # print number of lines altered
        print('Number of lines altered: ' + str(len(new_lines)))
    if new_lines[-1][-2] != ']':
        new_lines[-1] = new_lines[-1][:-1] + ']\r '
        print('Number of lines altered: ' + str(len(new_lines)))

    # save the file where the original file was 
    with open(path.replace('.txt', '.json'), 'w', encoding="utf-8") as f:
        f.writelines(new_lines)
        # print a message to the user
        print('File saved as: ' + path.replace('.txt', '.json'))

def main():
    json_insert_comma_add_bracket(sys.argv[1])

if __name__ == '__main__':
    main()