from utils import quicksort
from labs_4.math_utils import *


# Возвращаем выборку и интервал
def create_normal_sampling(a, b):
    if a > b:
        print("Данные некорректны")
        raise SystemExit(1)
    r = generate_random_variables(1000)
    x = []
    for i in r:
        xr = reverse_fun(i, a, b)
        x.append(xr)
    x = quicksort(x)
    interval = [a, b]
    return x, interval


def create_gauss_sampling(m, d):
    sigma = math.sqrt(d)
    r = generate_random_variables(1000)
    n = 6
    x = []
    for i in range(len(r)):
        v = 0
        for j in range(n):
            v += r[i]
        x = (v - m) / sigma
        x.append(x)
    x = quicksort(x)
    # Интервал от минимального до максимального x
    interval = [x[0], x[-1]]
    return x, interval


def create_rayleigh_sampling(d, n):
    sigma = math.sqrt(d)
    m = math.sqrt(math.pi / 2) * sigma  # Мат ожидание
    br = sigma * n
    ri = generate_random_variables(1000)
    rj = generate_random_variables(1000)
    x = []
    i = 0
    while len(x) <= 1000 and i < 1000:
        X = br * ri[i]
        Y = m * rj[i]
        if Y <= rayleigh_distribution(X, sigma):
            x.append(X)
        i += 1
    x = quicksort(x)
    # Интервал от 0 до максимального X
    interval = [0, x[-1]]
    return x, interval
