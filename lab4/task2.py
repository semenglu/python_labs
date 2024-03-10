import random

def generate_numbers(filename, N):
    #Генерирует N случайных целых чисел и записывает их в файл
    with open(filename, 'w') as file:
        for _ in range(N):
            # Генерируем случайное число от -100 до 100
            number = random.randint(-100, 100)
            file.write(f"{number}\n")


def count_opposite_pairs(filename):
    #Считывает числа из файла и подсчитывает количество пар противоположных чисел
    with open(filename, 'r') as file:
        numbers = file.readlines()

    # Преобразование строк в целые числа
    numbers = [int(number.strip()) for number in numbers]

    # Создаем словарь для подсчета вхождений каждого числа
    count_dict = {}
    for number in numbers:
        if number not in count_dict:
            count_dict[number] = 1
        else:
            count_dict[number] += 1

    # Подсчитываем количество пар противоположных чисел
    opposite_pairs = 0
    for number, count in count_dict.items():
        if -number in count_dict:
            opposite_pairs += min(count, count_dict[-number])

    # Делим на 2, т.к. каждая пара была подсчитана дважды
    opposite_pairs //= 2
    return opposite_pairs


# Настройка
filename = "random_numbers.txt"
N = 100  # Количество случайных чисел

# Генерация чисел и их запись в файл
generate_numbers(filename, N)

# Подсчет и вывод количества пар противоположных чисел
print(f"Количество пар противоположных чисел: {count_opposite_pairs(filename)}")

