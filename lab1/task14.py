#12 Отсортировать список В порядке увеличение квадратичного отклонения частоты встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке.

def most_common_char_freq(s):
    char_counts = [0] * 128  # массив для подсчета количества символов ASCII
    for char in s:
        char_code = ord(char)  # получаем ASCII-код символа
        char_counts[char_code] += 1

    most_common_char = chr(max(range(128), key=lambda x: char_counts[x]))
    most_common_char_freq = char_counts[ord(most_common_char)] / len(s)
    return most_common_char_freq
def sort_by_deviation(strings):
    sorted_strings = sorted(strings, key=lambda x: (most_common_char_freq(x) - max(x.count(char) for char in set(x))) ** 2)
    return sorted_strings

# Считываем строки из консоли
num_strings = int(input("Введите количество строк: "))
strings = []
for i in range(num_strings):
    s = input("Введите строку {}: ".format(i + 1))
    strings.append(s)

# Сортировка строк и вывод результата
sorted_strings = sort_by_deviation(strings)
print("Отсортированные строки:")
for s in sorted_strings:
    print(s)
