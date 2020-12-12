def remove_char(s):
    return s[1: -1]


def str_to_list(vector_str):
    return [float(x) for x in vector_str]


def quicksort(array):
    if len(array) <= 1:  # Базовый случай
        return array
    else:  # Рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  # Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  # Подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)
