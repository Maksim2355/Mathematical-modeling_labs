import utils


def parse_file_points(filename):
    list_points_parse = []
    f = open(filename, 'r')
    for p in f.read().splitlines():
        vectors = p.split(';')
        x_str = utils.remove_char(vectors[0]).split(',')
        x = utils.str_to_list(x_str)
        y_str = utils.remove_char(vectors[1]).split(',')
        y = utils.str_to_list(y_str)
        #Если вектор содержит меньше 5 элементов, или их значения не равны, то пропускаем
        x = quicksort(x)
        if len(x) != len(y):
            continue
        list_points_parse.append([x, y])
    f.close()
    return list_points_parse



def quicksort(array):
    if len(array) <= 1:  #Базовый случай
        return array
    else:  #Рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  #Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  #Подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)