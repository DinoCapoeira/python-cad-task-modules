import json


def draw_box(x, y, z, w, h, d):
    print(f"Box : Centered on ({x},{y},{z}), ({w}x{h}x{d}) dimensioned")

with open("scaffold.json","r") as file:
    data= json.load(file)

for box in data["scaffold"]:
    draw_box(
        box["x"],
        box["y"],
        box["z"],
        box["width"],
        box["height"],
        box["depth"]

    )