import matplotlib.pyplot as plt
import numpy as np
from parser_points import *
from filter_graphs import filter_graphs as filter_gr


def piecewise_linear_interpolation(vector_x, vector_y, xl):
    res = 0
    for i in range(len(vector_x)):
        if vector_x[i - 1] <= xl <= vector_x[i]:
            x = xl - vector_x[i]
            yp = vector_y[i] - vector_y[i - 1]
            xp = vector_x[i] - vector_x[i - 1]
            res = vector_y[i] + ((yp / xp) * x)
            break
    return res


'''' Функция отрисовки графика
    На входе получает вектора точек
    @vectors представляет собой двумерный список точек на графике'''


def draw_graph(vectors):
    filter_vectors = filter_gr(vectors)
    for vector in filter_vectors:
        x = vector[0]
        y = vector[1]
        yl = [piecewise_linear_interpolation(x, y, i) for i in x]
        plt.scatter(x, y)
        plt.plot(x, yl)
    plt.show()


file = parse_file_points('points')
draw_graph(file)
