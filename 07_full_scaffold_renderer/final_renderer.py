import sys
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_box(ax, x, y, z, w, h, d, color='blue'):
    x0, x1 = x - w / 2, x + w / 2
    y0, y1 = y - h / 2, y + h / 2
    z0, z1 = z - d / 2, z + d / 2

    points = [
        [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
        [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    for edge in edges:
        p1, p2 = points[edge[0]], points[edge[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color=color)


def apply_offset_to_box(box, ox, oy, oz):
    box["x"] += ox
    box["y"] += oy
    box["z"] += oz
    return box


try:
    ox = float(sys.argv[1])
    oy = float(sys.argv[2])
    oz = float(sys.argv[3])
except (IndexError, ValueError):
    print("Usage: python final_renderer.py OX OY OZ")
    sys.exit(1)

with open("scaffold.json", "r") as f:
    data = json.load(f)

updated_data = {"scaffold": []}
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for box in data["scaffold"]:
    box = apply_offset_to_box(box, ox, oy, oz)
    vol = box["width"] * box["height"] * box["depth"]
    color = "green" if vol >= 1000 else "yellow"
    draw_box(ax, box["x"], box["y"], box["z"],
             box["width"], box["height"], box["depth"], color=color)
    updated_data["scaffold"].append(box)

with open("scaffold_offset.json", "w") as f:
    json.dump(updated_data, f, indent=4)

ax.set_xlabel("X Plane")
ax.set_ylabel("Y Plane")
ax.set_zlabel("Z Plane")
ax.set_title("Scaffold Boxes (with color and offset)")

plt.show()
