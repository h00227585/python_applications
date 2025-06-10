import matplotlib.pyplot as plt
import random

"""
谢尔宾斯基三角形
"""


def sierpinski(points, iterations):
    x, y = random.uniform(-200, 200), random.uniform(-100, 200)
    xs, ys = [], []
    for _ in range(iterations):
        vertex = random.choice(points)
        x = (x + vertex[0]) / 2
        y = (y + vertex[1]) / 2
        xs.append(x)
        ys.append(y)
    return xs, ys


if __name__ == '__main__':
    points = [[-200, -100], [0, 200], [200, -100]]
    xs, ys = sierpinski(points, 10000)
    plt.scatter(xs, ys, s=0.1, color='blue')
    plt.axis('equal')
    plt.show()
