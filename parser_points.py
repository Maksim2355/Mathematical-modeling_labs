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
        x = utils.quicksort(x)
        if len(x) != len(y):
            continue
        list_points_parse.append([x, y])
    f.close()
    return list_points_parse



