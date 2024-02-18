#7 В порядке увеличения разницы между количеством сочетаний «гласная-согласная» и «согласная-гласная» в строке.

def is_vowel(c): #Проверка на гласную букву (для русских и английских букв).
    return c.lower() in 'aeiouyаеёиоуыэюя'

def is_consonant(c): #Проверка на согласную букву (для русских и английских букв).
    return c.lower() in 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'

def count_combinations(s): #Подсчитывает сочетания 'гласная-согласная' и 'согласная-гласная'.
    vc_count = 0  # Счетчик для 'гласная-согласная'
    cv_count = 0  # Счетчик для 'согласная-гласная'
    for i in range(len(s) - 1):
        if is_vowel(s[i]) and is_consonant(s[i+1]):
            vc_count += 1
        elif is_consonant(s[i]) and is_vowel(s[i+1]):
            cv_count += 1
    return vc_count, cv_count

def sort_strings_by_difference(lst): #Сортировка списка строк по увеличению разницы между кол-вом сочетаний 'гласная-согласная'и 'согласная-гласная'.
    return sorted(lst, key=lambda x: abs(count_combinations(x)[0] - count_combinations(x)[1]))

# Ввод строк с консоли
print("Введите строки для сортировки (для завершения введите пустую строку):")
input_strings = []
while True:
    string = input().strip()
    if string == "":
        break
    input_strings.append(string)

# Сортировка строк и вывод результата
sorted_strings = sort_strings_by_difference(input_strings)
print("Результат сортировки:")
for string in sorted_strings:
    print(string)
