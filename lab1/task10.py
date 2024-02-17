#Задание 10 Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.

n = int(input("Введите количество строк: "))
strings = []

# заполняем список строками, введенными пользователем
for i in range(n):
    string = input("Введите строку: ")
    strings.append(string)

# сортируем список строк по количеству слов в каждой строке
sorted_strings = sorted(strings, key=lambda x: len(x.split()))

# выводим отсортированные строки
print("Строки, упорядоченные по количеству слов в строке:")
for string in sorted_strings:
    print(string)
