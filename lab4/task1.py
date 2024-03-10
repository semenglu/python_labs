def check_elements(numbers, elements, K):
    if (abs(numbers[elements[0]][0] - numbers[elements[1]][-1]) < K
        and abs(numbers[elements[0]][-1] - numbers[elements[1]][0]) < K):
            return False
    if (abs(numbers[elements[1]][0] - numbers[elements[2]][-1]) < K
        and abs(numbers[elements[1]][-1] - numbers[elements[2]][0]) < K):
            return False
    if (abs(numbers[elements[0]][0] - numbers[elements[2]][-1]) < K
        and abs(numbers[elements[0]][-1] - numbers[elements[2]][0]) < K):
            return False
    return True


def max_product(filename):
    file = open(filename, 'r')
    N, K = map(int, file.readline().split())

    numbers = dict()
    for i in range(N):
        el = int(file.readline())
        numbers.setdefault(el, []).append(i)
    keys = sorted(numbers.keys(), reverse=True)


    for i in range(N - 2):
        keys_i = keys[i: i + 3]
        if check_elements(numbers, keys_i, K):
            print(keys_i, numbers[keys_i[0]], numbers[keys_i[1]], numbers[keys_i[2]])
            el = keys_i[0] * keys_i[1] * keys_i[2]
            break
    return el % (10 ** 6 + 1)


# Пути к файлам нужно изменить на соответствующие пути к вашим файлам на вашем компьютере
print("Файл pr:", max_product('C:/Users/semen/PycharmProjects/pythonProject1/1.txt'))
print("Файл A:", max_product('C:/Users/semen/PycharmProjects/pythonProject1/27-168a.txt'))
print("Файл B:", max_product('C:/Users/semen/PycharmProjects/pythonProject1/27-168b.txt'))

