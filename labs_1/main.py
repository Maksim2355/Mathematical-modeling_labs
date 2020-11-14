import matplotlib.pyplot as plt
from labs_1.parser_points import *

'''''Функция отрисовки графика
    На входе получает вектора точек
    @vectors представляет собой двумерный список точек на графике'''


def draw_graph(vectors):
    for vector in vectors:
        x = vector[0]
        y = vector[1]
        plt.plot(x, y)
    plt.show()


file = parse_file_points('points')
draw_graph(file)
