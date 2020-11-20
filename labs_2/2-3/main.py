import matplotlib.pyplot as plt
from parser_points import *
from filter_graphs import filter_graphs as filter_gr
import numpy as np


'''' Функция отрисовки графика
    На входе получает вектора точек
    @vectors представляет собой двумерный список точек на графике'''


def piecewise_parabolic_interpolation(vector_x, vector_y, arg):
    for i in range(len(vector_x)):
        y0 = vector_y[i - 2]
        y1 = vector_y[i - 1]
        y2 = vector_y[i]
        x0 = vector_x[i - 2]
        x1 = vector_x[i - 1]
        x2 = vector_x[i]
        return y0 + (y1 - y0) * (arg - x0) / (x1 - x0) + (1 / (x2 - x0)) * (arg - x0) * (arg - x1) * \
               (((y2 - y1) / (x2 - x1)) - ((y1 - y0) / (x1 - x0)))


def draw_graph(vectors):
    filter_vectors = filter_gr(vectors)
    for vector in filter_vectors:
        x = np.array(vector[0], dtype=float)
        y = np.array(vector[1], dtype=float)
        xl = np.linspace(np.min(x), np.max(x))
        print(xl)
        yl = [piecewise_parabolic_interpolation(x, y, arg) for arg in xl]
        plt.scatter(x, y)
        plt.plot(xl, yl)
    plt.show()


file = parse_file_points('points')
draw_graph(file)
