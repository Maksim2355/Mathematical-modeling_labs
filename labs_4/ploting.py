from labs_4.math_utils import *


def plot_histogram(X, data_hist, k, interval, title, dstr, m=0, d=0):
    a = interval[0]
    b = interval[1]
    delta = (b - a) / k
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]  # частота
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
    plt.title(title)
    plot_density_fn(X, a, b, dstr, m, d)
    plt.show()


def plot_polygon(X, data_polygon, k, interval, title, dstr, m=0, d=0):
    a = interval[0]
    b = interval[1]
    x = []
    y = []
    for i in data_polygon:
        y.append(i[0])
        x.append(i[1])
        plt.scatter(x, y)
    plt.plot(x, y)
    plt.title(title)
    plot_density_fn(X, a, b, dstr, m, d)
    plt.show()
