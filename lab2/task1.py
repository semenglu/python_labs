#Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

result = sorted(list(set(lst1) & set(lst2)))
print(" ".join(map(str, result)))
