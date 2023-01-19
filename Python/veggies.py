vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

import csv 

with open('output/vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name","color"])

    for veg in vegetables:
        # veg = {"name": "eggplant", "color": "purple"}
        writer.writerow([veg["name"], veg["color"]])
   