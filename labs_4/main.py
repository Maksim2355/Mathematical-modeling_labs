import math
import random as rnd


def reverse_fun(ri):
    return (ri * (b - a)) - a


def g(xl):
    return (xl / d) * math.exp(- (xl ** 2) / 2 * (d ** 2))


def generate_random_variables(size):
    r = []
    while size != 0:
        r.append(rnd.random())
        size -= size
    return r


a = int(input("Введите начальное значение интервала: "))
b = int(input("Введите конечное знаение интервала: "))

m = float(input("Введите мат ожидание: "))  # Мат ожидание
d = float(input("Введите дисперсию: "))  # Дисперсия
sigma = math.sqrt(d)  # Среднеквадратичное отклонеие

if a > b:
    print("Данные некорректны")
    raise SystemExit(1)

# 1.1 Формируем выборку случайных велечин методом обратных функций

r_reverse_function = generate_random_variables(1000)
x_reverse = []
for i in r_reverse_function:
    xr = reverse_fun(i)
    x_reverse.append(xr)

# 1.2 Формируем выборку велечин, распредленных по Гауссовскому закону с параметрами m и D

n = 6

# if n != 6 or n != 12:
#     n = 12

r_gauss = generate_random_variables(1000)
x_gauss = []
for i in range(len(r_gauss)):
    v = 0
    for j in range(n):
        v += r_gauss[i]
    x = (v - m) / sigma
    x_gauss.append(x)

# 1.3   Осууществим выборку случайных значенй по методу Неймана

ri_neumann = generate_random_variables(1000)
rj_neumann = generate_random_variables(1000)
x_neumann = []
i = 0
while len(x_neumann) <= 1000 and i <= 1000:
    X = (b - a) * ri_neumann[i]
    Y = m * rj_neumann[i]
    if Y <= g(X):
        x_neumann.append(X)
    i += 1
