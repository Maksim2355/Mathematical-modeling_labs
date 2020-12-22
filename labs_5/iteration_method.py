from labs_5.equations import *


def iteration_method(xo, eps, n):
    if abs(fi_derivative(xo)) >= 1:
        return "Итерационный процесс расходится"
    x = fi(xo)
    for i in range(n):
        xn = fi(x)
        if abs(fi_derivative(x)) >= 1:
            return "Итерационный процесс расходится"
        if abs(xn - x) < eps:
            os = abs(str(eps).find('.') - len(str(eps))) - 1
            return round(xn, os), i + 1
        x = xn
    return "Не хватает точности"


def iteration_method_params(xo, eps, n, params_one=0, params_two=0):
    if abs(fi_with_parameters_derivative(xo, params_one, params_two)) >= 1:
        return "Итерационный процесс расходится"
    x = fi_with_parameters(xo, params_one, params_two)
    for i in range(n):
        xn = fi_with_parameters(x, params_one, params_two)
        if abs(fi_with_parameters_derivative(xo, params_one, params_two)) >= 1:
            return "Итерационный процесс расходится", i + 1
        if abs(xn - x) < eps:
            os = abs(str(eps).find('.') - len(str(eps))) - 1
            return round(xn, os), i + 1
        x = xn
    return "Не хватает точности"


def find_root_iteration(xo, eps, n, has_params, a=0, b=0):
    if has_params:
        return iteration_method_params(xo, eps, n, a, b)
    else:
        return iteration_method(xo, eps, n)
