import numpy as np
import math


# Берем функцию с параметрами
def fun_with_parameters(x, a, b):
    return a * np.exp(-1 * (b * x)) - x


def derivative_fun_with_parameters(x, a, b):
    return -1 * (a * b * np.exp(-1 * (b * x))) - 1


# Берем функцию без параметров
def fun(x):
    return x * (2 ** x) - 1


def derivative_fun(x):
    return (2 ** x) * (math.log(2) * x + 1)
