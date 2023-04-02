import json
import sys


def load_json():
    with open(sys.argv[1], 'r', encoding='utf8') as f:
        data = json.load(f)
        # for person in data['_id']:
        #     print(person['name'], person['address'])
        print(data)


def main():
    load_json()


if __name__ == '__main__':
    main()
