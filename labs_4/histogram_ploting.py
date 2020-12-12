import math


def plot_histogram(X, interval):
    a = interval[0]
    b = interval[1]
    N = len(X)
    k = int(1 + 3.2 * math.log2(N))  # число интервалов
    R = b - a  # Определяем размах выборки
    width_interval = R / k
    g = []  # Частоты
    for i in range(0, k):
        # Определяем интервал. Определяем, сколько элементов входят в него
        x_min = a + width_interval * i
        x_max = a + width_interval * (i + 1)
        count_elements = 0
        for x in X:
            if x_min < x <= x_max:
                count_elements += 1
            # Массив отсортирован и если элемент выходит из интервала, то заканчиваем подсчет
            if x > x_max:
                break
        w = count_elements / N
        data_hist = [x_min, x_max, w]
        g.append(data_hist)
    return g