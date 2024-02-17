#Задание 9 Прочитать список строк с клавиатуры. Упорядочить по длине строки.

n = int(input("Введите количество строк: "))  
strings = []

# заполняем список строками, введенными пользователем
for i in range(n):
    string = input("Введите строку: ")
    strings.append(string)

# сортируем список строк по их длине
sorted_strings = sorted(strings, key=len)

# выводим отсортированные строки
print("Строки, упорядоченные по длине:")
for string in sorted_strings:
    print(string)
