from labs_4.create_sampling import *
from labs_4.graphs_points import create_histogram
from labs_4.ploting import plot_histogram


# 1.1 Формируем выборку случайных велечин методом обратных функций
a = int(input("Введите начальное значение интервала: "))
b = int(input("Введите конечное знаение интервала: "))

x_normal, interval_normal = create_normal_sampling(a, b)
data_hist_normal, k_normal = create_histogram(x_normal, interval_normal)

plot_histogram(x_normal, data_hist_normal, k_normal, interval_normal, "Равномерное распределение")

# 1.2 Формируем выборку велечин, распредленных по Гауссовскому закону с параметрами m и D
m_gauss = float(input("Введите мат ожидание для распределения Гаусса: "))  # Мат ожидание
d_gauss = float(input("Введите дисперсию для распределения Гаусса: "))  # Дисперсия

x_gauss, interval_gauss = create_gauss_sampling(m_gauss, d_gauss)

data_hist_gauss, k_gauss = create_histogram(x_gauss, interval_gauss)

plot_histogram(x_gauss, data_hist_gauss, k_gauss, interval_gauss, "Распределение Гаусса")

# 1.3   Осууществим выборку случайных значенй по методу Неймана
d_rayleigh = float(input("Введите дисперсию для релеевского закона: "))
n_rayleigh = int(input("Введите множитель знаение интервала Релея: "))

x_neumann, interval_neumann = create_rayleigh_sampling(d_rayleigh, n_rayleigh)
data_hist_neumann, k_neumann = create_histogram(x_neumann, interval_neumann)

plot_histogram(x_neumann, data_hist_neumann, k_neumann, interval_gauss, "Распределение Релея")

