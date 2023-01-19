import csv 
import json

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)
    members = superheroes["members"]  
    
with open('output/superheroes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "secretIdentity", "powers", "squadName", "homeTown","formed", "secretBase", "active"])
    for element in members:
        writer.writerow([element["name"], element["age"], element["secretIdentity"], element["powers"], superheroes["squadName"], superheroes["homeTown"], superheroes["formed"], superheroes["secretBase"], superheroes["active"]])        


 
   

