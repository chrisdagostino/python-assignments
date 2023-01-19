import csv 

with open('output/vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    
print(vegetables)

import json

with open('output/vegetables.json', 'w') as f:
    json.dump(vegetables, f)