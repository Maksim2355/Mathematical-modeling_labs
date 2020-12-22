from labs_5.equations import *


def newton_method(xo, eps, n):
    for i in range(n):
        xn = xo - (fun(xo) / fun_derivative(xo))
        # conditions_1 = (fun(xo) * fun_second_derivative(xo)) > 0
        conditions_2 = abs(xn - xo) < eps
        if conditions_2:
            os = abs(str(eps).find('.') - len(str(eps))) - 1
            return round(xn, os), i + 1
        xo = xn
    return "Слишком мало шагов итерации"


def newton_method_params(xo, eps, n, a, b):
    for i in range(n):
        xn = xo - (fun_with_parameters(xo, a, b) / fun_with_parameters_derivative(xo, a, b))
        # conditions_1 = (fun_with_parameters(xo, a, b) * fun_with_parameters_second_derivative(xo, a, b)) > 0
        conditions_2 = abs(xn - xo) < eps
        if conditions_2:
            os = abs(str(eps).find('.') - len(str(eps))) - 1
            return round(xn, os), i + 1
        xo = xn
    return "Слишком мало шагов итерации"


def find_root_newton(xo, eps, n, has_params, a=0, b=0):
    if has_params:
        return newton_method_params(xo, eps, n, a, b)
    else:
        return newton_method(xo, eps, n)
