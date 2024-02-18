#15 Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному индексу локальным минимумом.
def is_global_maximum(arr, index):
    if index < len(arr):
        return arr[index] == min(arr)
    else:
        return False

size = int(input("Введите размер массива: "))
arr = []

print("Введите элементы массива:")

for i in range(size):
    element = int(input(f"Элемент {i}: "))
    arr.append(element)

index = int(input("Введите индекс: "))

if is_global_maximum(arr, index):
    print(f"Элемент в индексе {index} является глобальным минимумом.")
else:
    print(f"Элемент в индексе {index} не является глобальным минимумом.")
