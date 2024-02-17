#3 Дана строка. Необходимо найти общее количество русских символов. 

s = input()
russian_chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
count = sum(s.count(c) for c in russian_chars)
print(count)
