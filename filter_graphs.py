def filter_graphs(vectors):
    filter_vectors = []
    print(f"Количество графиков в исходно выражении {len(vectors)} Выберите нужный диапазон или определнный график\n"
          f"Пример: 1-3 или 5. Для выбора всех графиков введите 0")
    command = input("").split('-')
    # Если пользователь ввел одно число
    if len(command) == 1:
        # Если командра 0, то добавляем весь список
        if int(command[0]) == 0:
            filter_vectors = vectors
        filter_vectors.append(vectors[int(command[0]) - 1])
    # Если пользователь ввел диапазон
    elif len(command) == 2:
        min_value = int(command[0]) - 1
        if min_value < 0:
            return []
        max_value = int(command[1])
        if max_value > len(vectors):
            return []
        for i in range(min_value, max_value):
            filter_vectors.append(vectors[i])
    else:
        return []
    return filter_vectors
