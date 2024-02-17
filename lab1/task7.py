#8 Дана строка. Необходимо найти все используемые в ней строчные символы латиницы.

s = input("Введите строку: ")

latin_lower_chars = set()
for char in s:
    if 'a' <= char <= 'z':
        latin_lower_chars.add(char)

print("Используемые строчные символы латиницы в строке:")
for char in sorted(latin_lower_chars):
    print(char, end=' ')
