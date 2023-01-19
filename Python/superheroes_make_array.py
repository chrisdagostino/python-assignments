import json

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

powers_list = []

members = superheroes["members"]

for member in members:
    powers_list.append(member["powers"])

print(powers_list)