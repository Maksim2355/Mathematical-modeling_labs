from labs_5.equations import *


def get_segments(a, b, has_equations_params, params_one=0, params_two=0):
    n = 1
    begin = a
    end = a
    segments = []
    while end <= b:
        dx = (b - a) / n
        end = begin + dx
        if has_equations_params:
            has_root = fun_with_parameters(begin, params_one, params_two) \
                       * fun_with_parameters(end, params_one, params_two) < 0
        else:
            has_root = t(begin) * t(end) < 0
        # Необходимое условие
        if has_root:
            # Если корень единственный, то добавляем интервал в сегменты, если нет, то разбиваем интервал
            if check_monotony(begin, end, has_equations_params):
                segments.append([begin, end])
            else:
                n += 1
                end = a
                continue
        else:
            n += 1
            end = a
            continue
        begin = end
    return segments


''''Надо проверить функцию на монотонность. 
Получим равномерную распредленную велечину на min-max и проверяем значение производной. '''


def check_monotony(min, max, has_equations_params, params_one=0, params_two=0):
    k = 1000
    ln = (max - min) / k
    min_value_fn = min
    list_derivative_values = []
    for i in range(k):
        r = min_value_fn
        if has_equations_params:
            params = fun_with_parameters_derivative(r, params_one, params_two)
        else:
            params = td(r)
        list_derivative_values.append(params)
        min_value_fn += ln
    return is_monotonic(list_derivative_values)


# Проверка, является ли массив монотонным
def is_monotonic(arr):
    return (all(
        arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all(arr[i] >= arr[i + 1] for i in
                range(len(arr) - 1)))
