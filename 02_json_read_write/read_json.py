import json

with open("scaffold.json", "r") as file:
    data = json.load(file)

print("Read the data:")
print(data)
