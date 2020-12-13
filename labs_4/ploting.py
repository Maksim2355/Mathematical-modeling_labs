import matplotlib.pyplot as plt
from labs_4.math_utils import *


def plot_histogram(X, data_hist, k, interval, title):
    delta = ((interval[1] - interval[0]) / k)
    i = 0
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]  # частота
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
        i += 1
    plt.title(title)
    plt.show()
