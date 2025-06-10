from dataclasses import dataclass

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

"""
谢尔宾斯基三角形

谢尔宾斯基三角形由波兰数学家瓦茨瓦夫·谢尔宾斯基于1915年提出，它的构造方法如下：
1. 从一个等边三角形开始。
2. 将三角形分成4个全等的小三角形，去掉中间的一个。
3. 对剩下的3个小三角形重复步骤2。
"""


@dataclass(frozen=True)
class Vertex:
    """表示二维空间中的一个顶点"""
    x: float
    y: float


@dataclass(frozen=True)
class Triangle:
    """表示一个三角形，由三个顶点组成"""
    v1: Vertex
    v2: Vertex
    v3: Vertex

    def vertices(self):
        """返回三角形的顶点坐标"""
        return np.array([(self.v1.x, self.v1.y),
                         (self.v2.x, self.v2.y),
                         (self.v3.x, self.v3.y)])


def draw_triangle(ax, triangle: Triangle,
                  face_color: str = 'white',
                  edge_color: str = 'blue',
                  line_width: float = 1.0):
    """
    在给定的坐标轴上绘制三角形

    :param ax 坐标轴区域
    :param triangle 三角形对象，包含三个顶点的位置信息
    :param face_color 三角形区域的填充颜色
    :param edge_color 三角形的边的颜色
    :param line_width 三角形边的线宽
    """
    # 创建一个多边形对象
    polygon = Polygon(triangle.vertices(),
                      closed=True,
                      facecolor=face_color,
                      edgecolor=edge_color,
                      linewidth=line_width)
    # 将多边形添加到坐标轴
    ax.add_patch(polygon)


def mid_vertex(v1: Vertex, v2: Vertex) -> Vertex:
    """返回两个顶点的中点"""
    return Vertex((v1.x + v2.x) / 2, (v1.y + v2.y) / 2)


def sierpinski(ax, triangle: Triangle, depth: int):
    """
    递归绘制Sierpinski三角形

    :param ax 坐标轴区域
    :param triangle 三角形对象，包含三个顶点的位置信息
    :param depth 至少为1，表示将三角形分成4个全等的小三角形的次数
    """
    if depth >= 0:
        # 绘制三角形
        draw_triangle(ax, triangle)

        # 计算新的顶点: 两个顶点的中点
        mid1 = mid_vertex(triangle.v1, triangle.v2)
        mid2 = mid_vertex(triangle.v2, triangle.v3)
        mid3 = mid_vertex(triangle.v3, triangle.v1)

        # 递归绘制三个小三角形
        sierpinski(ax, Triangle(triangle.v1, mid1, mid3), depth - 1)
        sierpinski(ax, Triangle(mid1, triangle.v2, mid2), depth - 1)
        sierpinski(ax, Triangle(mid3, mid2, triangle.v3), depth - 1)


if __name__ == '__main__':
    # n表示等边三角形的边长
    n = 12
    # 初始化一个三角形
    triangle = Triangle(Vertex(n / 2, n * 3 ** 0.5 / 2), Vertex(0, 0), Vertex(n, 0))
    # 在外部创建统一的绘图窗口
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, n + 0.1)  # 设置x轴范围
    ax.set_ylim(0, n * 3 ** 0.5 / 2 + 0.1)  # 设置y轴范围
    ax.set_aspect('equal')  # 确保图形比例一致
    ax.axis('off')  # 不显示坐标轴
    # 绘制
    sierpinski(ax, triangle, 5)
    # 显示图形
    plt.show()
