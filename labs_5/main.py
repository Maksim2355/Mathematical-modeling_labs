from labs_5.equations import *
from labs_5.iteration_method import find_root_iteration
from labs_5.newton_method import find_root_newton
from labs_5.dichotomy_method import find_root_dichotomy
from labs_5.ploting import *

# xo = float(input("Введите начальное приближение: "))
# n = int(input("Введите максимальное число итераций: "))
# eps = float(input("Введите точность: "))
#
print("Уравнение с параметрами вида math.tan(a * x) - b * x")
print("Параметр a = 1, b = 2")
print("Уравнение без параметров вида 3 * x + cos(x) + 1")
# params_one = float(input("Введите первый параметр m для уравнения: "))
# params_two = float(input("Введите второй параметр k для уравнения: "))

n = 5
print("Число итераций", n)
eps = 0.001
print("eps ", eps)
params_one = 1
params_two = 2

xo_iter = 0.4
print("Начальное приближение метода итераций", xo_iter)

plotting_graph_iteration(-1, 2)
plotting_graph_iteration_params(-1, 1, params_one, params_two)

print("Решения уравнения без параметров методом итерации: ", find_root_iteration(xo_iter, eps, n, False))
print("Решения уравнения c параметрами методом итерации: ",
      find_root_iteration(xo_iter, eps, n, True, params_one, params_two))

print("____________________________________________________________________________")

xo_newton = 0.1
print("Начальное приближение метода Ньютона", xo_newton)
print("Решения уравнения без параметров методом Ньютона: ", find_root_newton(xo_newton, eps, n, False))
print("Решения уравнения c параметрами методом Ньютона: ",
      find_root_newton(xo_newton, eps, n, True, params_one, params_two))

print("______________________________________________________________________________")

a = float(input("Введите интервал a: "))
b = float(input("Введите интервал b: "))

print("Решения уравнения без параметров методом дихотомии: ", find_root_dichotomy(a, b, eps, n, False))
print("Решения уравнения c параметрами методом дихотомии: ",
      find_root_dichotomy(a, b, eps, n, True, params_one, params_two))
