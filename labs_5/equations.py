import numpy as np
import math


# Берем функцию с параметрами
def fun_with_parameters(x, a, b):
    return a * np.exp(-1 * (b * x)) - x


# Производная функции с параметрами
def fun_with_parameters_derivative(x, a, b):
    return -1 * (a * b * np.exp(-1 * (b * x))) - 1


# Выразили x = fi(x)
def fi_with_parameters(x, a, b):
    return a * np.exp(-1 * (b * x))


def fi_with_parameters_derivative(x, a, b):
    return -1 * a * b * np.exp(-1 * b * x)


# Берем функцию без параметров
def fun(x):
    return x * (2 ** x) - 1


# Производная функции без параметров
def derivative_fun(x):
    return (2 ** x) * (math.log(2) * x + 1)


# Выразили x = fi(x)
def fi(x):
    return 1 / (2 ** x)


def fi_derivative(x):
    return (-2 ** (-1 * x)) * math.log(2)


def t(x):
    return math.exp(x) - 10 * x


def td(x):
    return math.exp(x) - 10
