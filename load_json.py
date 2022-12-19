import json
import sys

def load_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        for person in data['_id']:
            print(person['name'], person['address'])

def main():
    load_json(sys.argv[1])

if __name__ == '__main__':
    main()