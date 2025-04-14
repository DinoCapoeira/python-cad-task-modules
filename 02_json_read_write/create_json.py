import json

data = {
    "scaffold": [
        {
            "x": 0, "y": 0, "z": 0,
            "width": 10,
            "height": 20,
            "depth": 15
        }
    ]
}

with open("scaffold.json", "w") as file:
    json.dump(data, file, indent=4)
