import matplotlib.pyplot as plt
import numpy as np
from find_polynomial import find_polynomial as polynomial
from parser_points import *
from filter_graphs import filter_graphs as filter_gr

'''' Функция отрисовки графика
    На входе получает вектора точек
    @vectors представляет собой двумерный список точек на графике'''


def draw_graph(vectors):
    filter_vectors = filter_gr(vectors)
    for vector in filter_vectors:
        x = np.array(vector[0], dtype=float)
        y = np.array(vector[1], dtype=float)
        xl = np.linspace(np.min(x), np.max(y))
        yl = polynomial(x, y, xl)
        plt.scatter(x, y)
        plt.plot(xl, yl)
    plt.show()


file = parse_file_points('points')
draw_graph(file)
