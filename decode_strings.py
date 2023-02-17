'''
Problem: Given an encoded string found in a row of a CSV file, return its corresponding decoded string.
'''

import base64
import sys

def decode_strings(filename):
    '''
    Decode the strings in the "email" column.
    '''
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            print(line)
            for i in range(len(line)):
                if line[i].startswith('\=?utf-8?b?'):
                    line[i] = line[i].replace('\=?utf-8?b?', '')
                    line[i] = line[i].replace('?=', '')
                    line[i] = base64.b64decode(line[i])
                    line[i] = line[i].decode('utf-8')
                    print(line[i])

def main():
    '''
    Main function.
    '''
    decode_strings(sys.argv[1]) 

if __name__ == '__main__':
    main()