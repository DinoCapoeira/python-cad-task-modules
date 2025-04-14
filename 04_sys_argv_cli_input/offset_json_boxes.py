import sys
import json

ox = float(sys.argv[1])
oy = float(sys.argv[2])
oz = float(sys.argv[3])

with open("scaffold.json", "r") as file:
    data = json.load(file)

box = data["scaffold"]["box"]
box["x"] += ox
box["y"] += oy
box["z"] += oz

with open("scaffold_offset.json", "w") as file:
    json.dump(data, file, indent=4)

print("Offset applied JSON has been saved.")
