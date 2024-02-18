#39 Дан целочисленный массив. Необходимо вывести вначале его элементы с четными индексами, а затем – с нечетными.

def print_elements_by_index(arr):
    even_indices = []
    odd_indices = []

    for i in range(len(arr)):
        if i % 2 == 0:
            even_indices.append(arr[i])
        else:
            odd_indices.append(arr[i])

    print("Элементы с четными индексами:", even_indices)
    print("Элементы с нечетными индексами:", odd_indices)


size = int(input("Введите размер массива: "))
arr = []

print("Введите элементы массива:")

for i in range(size):
    element = int(input(f"Элемент {i}: "))
    arr.append(element)

print_elements_by_index(arr)


