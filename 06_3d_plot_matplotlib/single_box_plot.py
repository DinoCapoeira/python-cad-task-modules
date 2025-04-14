import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_box(ax, x, y, z, w, h, d):
    x0, x1 = x - w / 2, x + w / 2
    y0, y1 = y - h / 2, y + h / 2
    z0, z1 = z - d / 2, z + d / 2

    points = [
        [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
        [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1],
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    for edge in edges:
        p1 = points[edge[0]]
        p2 = points[edge[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='blue')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

draw_box(ax, x=0, y=0, z=0, w=10, h=10, d=10)

ax.set_xlabel('X Plane')
ax.set_ylabel('Y Plane')
ax.set_zlabel('Z Plane')
ax.set_title('Single Box')

plt.show()
