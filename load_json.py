import json

with open('data.json') as f:
    data = json.load(f)

for person in data['profile_id']:
    print(person['name'], person['address'])