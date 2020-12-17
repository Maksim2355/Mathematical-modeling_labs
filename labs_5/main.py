from labs_5.equations import *
from labs_5.iteration_method import *
from labs_5.ploting import *




xo = float(input("Введите начальное приближение: "))
n = int(input("Введите максимальное число итераций: "))
eps = float(input("Введите точность: "))

print("Уравнения вида m * np.exp(-1 * (k * x)) - x")
params_one = float(input("Введите первый параметр m для уравнения: "))
params_two = float(input("Введите второй параметр k для уравнения: "))


plotting_graph_iteration(-1, 2)
plotting_graph_iteration_params(-1, 1, params_one, params_two)

print(iteration_method(xo, eps, n))
print(iteration_method_params(xo, eps, n, params_one, params_two))



