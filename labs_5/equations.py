import numpy as np
import math


# Берем функцию с параметрами
def fun_with_parameters(x, a, b):
    return a * np.exp(-1 * (b * x)) - x


# Производная функции с параметрами
def fun_with_parameters_derivative(x, a, b):
    return -1 * (a * b * np.exp(-1 * (b * x))) - 1


def fun_with_parameters_second_derivative(x, a, b):
    return a * (b ** 2) * np.exp(-1 * (b * x))


# Выразили x = fi(x)
def fi_with_parameters(x, a, b):
    return a * np.exp(-1 * (b * x))


def fi_with_parameters_derivative(x, a, b):
    return -1 * a * b * np.exp(-1 * b * x)


# Берем функцию без параметров
def fun(x):
    return x * (2 ** x) - 1


# Производная функции без параметров
def fun_derivative(x):
    return (2 ** x) * (math.log(2) * x + 1)


def fun_second_derivative(x):
    return (2 ** x) * (math.log(2) ** 2) * x + (2 ** (x + 1)) * math.log(2)


# Выразили x = fi(x)
def fi(x):
    return 1 / (2 ** x)


def fi_derivative(x):
    return (-2 ** (-1 * x)) * math.log(2)

