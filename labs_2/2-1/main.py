import matplotlib.pyplot as plt
import numpy as np
from parser_points import *
from filter_graphs import filter_graphs as filter_gr

'''' Функция отрисовки графика
    На входе получает вектора точек
    @vectors представляет собой двумерный список точек на графике'''


def find_polynomial(vector_x, vector_y, vector_xl):
    vector_yl = []
    for xl in vector_xl:
        # Полином
        L = 0
        # Вложенные циклы имеют одинаковое количество i и j т.к vector_x и vector_y имеют равную длинну
        for j in range(len(vector_x)):
            # Промежуточные значения полинома. Первоначально предполагаем, что они равны y[i]
            pl1 = vector_y[j]
            pl2 = vector_y[j]
            for i in range(len(vector_x)):
                # При одинаковых коээфициентах, значение pl2 обращается в 0. По условию i не должно совпадть с j
                if i == j:
                    continue
                '''''Находим числитель и знаменитель для нашего полинома и умножаем все на y[n]'''
                pl1 = (xl - vector_x[i]) * pl1
                pl2 = (vector_x[j] - vector_x[i]) * pl2
            # Находим значение L[i]
            L = L + (vector_y[j] * (pl1 / pl2))
        vector_yl.append(L)
    return vector_yl


def draw_graph(vectors):
    filter_vectors = filter_gr(vectors)
    for vector in filter_vectors:
        x = np.array(vector[0], dtype=float)
        y = np.array(vector[1], dtype=float)
        xl = np.linspace(np.min(x), np.max(x))
        yl = find_polynomial(x, y, xl)
        plt.scatter(x, y)
        plt.plot(xl, yl)
    plt.show()


file = parse_file_points('points')
draw_graph(file)
