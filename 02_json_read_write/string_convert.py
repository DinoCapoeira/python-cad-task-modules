import json

data = {"name": "Dino", "job": "CAD Developer"}
json_string = json.dumps(data)

print("JSON Format as String:")
print(json_string)

data = json.loads(json_string)
print("Converted back to Python Dict:")
print(data)
