#5 Отсортировать строки В порядке увеличения квадратичного отклонения частоты встречаемости самого часто встречаемого в строке символа от частоты еговстречаемости в текстах на этом алфавите.

import numpy as np

# Русский алфавит
russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# Частоты встречаемости букв русского языка
russian_freq = [0.07998, 0.01592, 0.04533, 0.01687, 0.02977, 0.08483, 0.0094, 0.01641, 0.07367, 0.01604,
                0.03486, 0.04441, 0.03203, 0.067, 0.10983, 0.02804, 0.04746, 0.05473, 0.06264, 0.02621,
                0.00267, 0.00928, 0.00473, 0.00312, 0.02001, 0.00612, 0.00037, 0.00967, 0.00214]


# Функция для вычисления квадратичного отклонения частоты встречаемости
def calculate_freq_deviation(s):
    s = s.lower()
    char_count = [s.count(char) for char in russian_alphabet]
    most_common_freq = max(char_count)
    most_common_char = russian_alphabet[char_count.index(most_common_freq)]
    char_index = russian_alphabet.index(most_common_char)
    russian_freq_common_char = russian_freq[char_index]

    deviation = (most_common_freq - russian_freq_common_char) ** 2
    return deviation


n = int(input("Введите количество строк: "))
strings = [input("Введите строку: ") for _ in range(n)]

sorted_strings = sorted(strings, key=calculate_freq_deviation)

print("Строки, отсортированные по квадратичному отклонению частоты самого часто встречаемого символа:")
for string in sorted_strings:
    print(string)
