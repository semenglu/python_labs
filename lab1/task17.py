#27 Дан целочисленный массив. Необходимо осуществить циклический сдвиг элементов массива влево на одну позицию.

def rotate_left(arr):
    if len(arr) <= 1:
        return arr

    first_element = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first_element

    return arr


size = int(input("Введите размер массива: "))
arr = []

print("Введите элементы массива:")

for i in range(size):
    element = int(input(f"Элемент {i}: "))
    arr.append(element)

print("Исходный массив:", arr)

# Вызов функции для циклического сдвига элементов влево
rotated_array = rotate_left(arr)
print("Массив после циклического сдвига влево:", rotated_array)
