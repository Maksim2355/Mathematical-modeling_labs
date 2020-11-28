import matplotlib.pyplot as plt
from parser_points import *
from filter_graphs import filter_graphs as filter_gr
import numpy as np

'''' Функция отрисовки графика
    На входе получает вектора точек
    @vectors представляет собой двумерный список точек на графике'''


def approximation(x, y):
    d = 3
    fp, residuals, rank, sv, rcond = np.polyfit(x, y, d, full=True)
    f = np.poly1d(fp)
    fx = np.linspace(np.min(x), np.max(x))
    plt.plot(fx, f(fx))
    plt.grid(True)


def draw_graph(vectors):
    filter_vectors = filter_gr(vectors)
    for vector in filter_vectors:
        x = vector[0]
        y = vector[1]
        fx = np.linspace(x[0], x[-1] + 1, len(x))
        approximation(x, y)
        plt.scatter(x, y)
    plt.show()


file = parse_file_points('points')
draw_graph(file)
