def find_polynomial(vector_x, vector_y, vector_xl):
    vector_yl = []
    for xl in vector_xl:
        # Полином
        L = 0
        # Вложенные циклы имеют одинаковое количество i и j т.к vector_x и vector_y имеют равную длинну
        for j in range(len(vector_x)):
            # Промежуточные значения полинома. Первоначально предполагаем, что они равны y[i]
            pl1 = vector_y[j]
            pl2 = vector_y[j]
            for i in range(len(vector_x)):
                # При одинаковых коээфициентах, значение pl2 обращается в 0. По условию i не должно совпадть с j
                if i == j:
                    continue
                '''''Находим числитель и знаменитель для нашего полинома и умножаем все на y[n]'''
                pl1 = (xl - vector_x[i]) * pl1
                pl2 = (vector_x[j] - vector_x[i]) * pl2
            #Находим значение L[i]
            L = L + (vector_y[j] * (pl1 / pl2))
        vector_yl.append(L)
    return vector_yl
