#16 Дана строка. Необходимо найти минимальное из имеющихся в ней целых чисел.

s = input("Введите строку: ")

min_number = float('inf')

current_num = ''
for char in s:
    if char.isdigit() or char == '-':
        current_num += char
    else:
        if current_num:
            num = int(current_num)
            min_number = min(min_number, num)
            current_num = ''

if current_num:  # проверяем, было ли число в конце строки
    num = int(current_num)
    min_number = min(min_number, num)

if min_number == float('inf'):
    print("В строке нет целых чисел.")
else:
    print("Минимальное целое число в строке:", min_number)
