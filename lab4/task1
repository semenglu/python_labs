def max_product(filename):
    with open(filename, 'r') as file:
        N, K = map(int, file.readline().split())
        values = [int(file.readline()) for _ in range(N)]

    # Включаем только значимые элементы для оптимизации
    significant_values = [0] * N
    max_product = 0

    for i in range(N):
        significant_values[i] = values[i]
        for j in range(i + K + 1, N):
            for k in range(j + K + 1, N):
                current_product = significant_values[i] * values[j] * values[k]
                if current_product > max_product:
                    max_product = current_product

    return max_product % (10 ** 6 + 1)


# Использование функции для вычисления ответов для заданных файлов
print("Файл A:", max_product('27-168a.txt'))
print("Файл B:", max_product('27-168.txt'))
