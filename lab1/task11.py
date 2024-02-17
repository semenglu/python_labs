#3 В порядке увеличения разницы между частотой наиболее часто встречаемого символа в строке и частотой его появления в алфавите.

import string
def calculate_frequency_difference(s):
    s = s.lower()
    char_count = [s.count(char) for char in string.ascii_lowercase if char in s]
    if not char_count:
        return 0
    most_common_freq = max(char_count)
    most_common_char = string.ascii_lowercase[char_count.index(most_common_freq)]

    if most_common_char in string.ascii_lowercase:
        alphabet_position = string.ascii_lowercase.index(most_common_char)
        return most_common_freq - alphabet_position
    else:
        return 0


n = int(input("Введите количество строк: "))
strings = [input("Введите строку: ") for i in range(n)]
sorted_strings = sorted(strings, key=calculate_frequency_difference)

print("Строки, упорядоченные по разнице частоты символов:")
for string in sorted_strings:
    print(string)
