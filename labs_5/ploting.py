from labs_5.equations import *
import matplotlib.pyplot as plt


def plotting_graph_iteration(x_min, x_max):
    dx = (x_max - x_min) / 1000
    x_arr = []
    y_arr = []
    x = x_min
    while x <= x_max:
        x_arr.append(x)
        y_arr.append(fi(x))
        x += dx
    plt.plot(x_arr, y_arr)
    plt.plot(x_arr, x_arr)
    plt.show()


def plotting_graph_iteration_params(x_min, x_max, a, b):
    dx = (x_max - x_min) / 1000
    x_arr = []
    y_arr = []
    x = x_min
    while x <= x_max:
        x_arr.append(x)
        y_arr.append(fi_with_parameters(x, a, b))
        x += dx
    plt.plot(x_arr, y_arr)
    plt.plot(x_arr, x_arr)
    plt.show()
