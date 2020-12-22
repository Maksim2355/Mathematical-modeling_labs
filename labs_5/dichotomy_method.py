from labs_5.equations import *


def dichotomy_method(begin, end, eps, n):
    for i in range(n):
        xo = (end + begin) / 2
        if fun(xo) == 0:
            return xo, i + 1
        if fun(begin) * fun(xo) < 0:
            end = xo
        else:
            begin = xo
        if abs(end - begin) < (2 * eps):
            return xo, i + 1
    return "Не хватило итераций"


def dichotomy_method_params(begin, end, eps, n, a, b):
    for i in range(n):
        xo = (end + begin) / 2
        if fun_with_parameters(xo, a, b) == 0:
            os = abs(str(eps).find('.') - len(str(eps))) - 1
            return round(xo, os), i + 1
        if fun_with_parameters(begin, a, b) * fun_with_parameters(xo, a, b) < 0:
            end = xo
        else:
            begin = xo
        if abs(end - begin) < 2 * eps:
            os = abs(str(eps).find('.') - len(str(eps))) - 1
            return round(xo, os), i + 1
    return "Не хватило итераций"


def find_root_dichotomy(begin, end, eps, n, has_params, a=0, b=0):
    if has_params:
        return dichotomy_method_params(begin, end, eps, n, a, b)
    else:
        return dichotomy_method(begin, end, eps, n)
