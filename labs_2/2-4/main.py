import matplotlib.pyplot as plt
from scipy import interpolate
from parser_points import *
from filter_graphs import filter_graphs as filter_gr
import numpy as np


'''' Функция отрисовки графика
    На входе получает вектора точек
    @vectors представляет собой двумерный список точек на графике'''


def draw_graph(vectors):
    filter_vectors = filter_gr(vectors)
    for vector in filter_vectors:
        x = np.array(vector[0], dtype=float)
        y = np.array(vector[1], dtype=float)
        xl = np.linspace(np.min(x), np.max(x))
        tck = interpolate.splrep(x, y, s=0)
        yl = interpolate.splev(xl, tck, der=0)
        plt.scatter(x, y)
        plt.plot(xl, yl)
    plt.show()


file = parse_file_points('points')
draw_graph(file)
