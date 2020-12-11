import math
import random as rnd
import numpy as np


def reverse_fun(ri, ai, bi):
    return (ri * (bi - ai)) - ai


def rayleigh_distribution(xl, sigma):
    return (xl / sigma ** 2) * math.exp(- ((xl ** 2) / 2 * (sigma ** 2)))


def generate_random_variables(size):
    r = []
    for i in range(size):
        r.append(rnd.random())
    return r


# 1.1 Формируем выборку случайных велечин методом обратных функций
a = int(input("Введите начальное значение интервала: "))
b = int(input("Введите конечное знаение интервала: "))

if a > b:
    print("Данные некорректны")
    raise SystemExit(1)

r_normal = generate_random_variables(1000)
x_normal = []
for i in r_normal:
    xr = reverse_fun(i, a, b)
    x_normal.append(xr)

interval_normal = [a, b]

# 1.2 Формируем выборку велечин, распредленных по Гауссовскому закону с параметрами m и D
m_gauss = float(input("Введите мат ожидание для распределения Гаусса: "))  # Мат ожидание
d_gauss = float(input("Введите дисперсию для распределения Гаусса: "))  # Дисперсия
sigma_gauss = math.sqrt(d_gauss)  # Среднеквадратичное отклонеие

n = 6

r_gauss = generate_random_variables(1000)
x_gauss = []
for i in range(len(r_gauss)):
    v = 0
    for j in range(n):
        v += r_gauss[i]
    x = (v - m_gauss) / sigma_gauss
    x_gauss.append(x)

# Интервал для построение гипсторграммы и полигона
interval_gauss = [np.min(x_gauss), np.max(x_gauss)]

# 1.3   Осууществим выборку случайных значенй по методу Неймана
d_rayleigh = float(input("Введите дисперсию для релеевского закона: "))
sigma_rayleigh = math.sqrt(d_rayleigh)
m_rayleigh = math.sqrt(math.pi / 2) * sigma_gauss  # Мат ожидание

ar = int(input("Введите начальное значение интервала Релея: "))
br = int(input("Введите конечное знаение интервала Релея: "))

ri_neumann = generate_random_variables(1000)
rj_neumann = generate_random_variables(1000)

x_neumann = []
i = 0
while len(x_neumann) <= 1000 and i < 1000:
    X = (br - ar) * ri_neumann[i]
    Y = m_rayleigh * rj_neumann[i]
    if Y <= rayleigh_distribution(X, sigma_rayleigh):
        x_neumann.append(X)
    i += 1

interval_neumann = [0, np.max(x_neumann)]
