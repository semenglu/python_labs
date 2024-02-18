#51 Для введенного списка построить два списка L1 и L2, где элементы L1 это неповторяющиеся элементы исходного списка, а элемент списка L2 с
#номером i показывает, сколько раз элемент списка L1 с таким номером
#повторяется в исходном.

input_str = input("Введите элементы списка через пробел: ")  
input_elements = input_str.split() 

input_list = []  #список для хранения преобразованных элементов

for item in input_elements:
    input_list.append(item)

L1 = []
L2 = []

# Цикл для обработки элементов исходного списка
for element in input_list:
    if element not in L1:
        L1.append(element)
        L2.append(1)
    else:
        index = L1.index(element)
        L2[index] += 1

print("Список L1 (неповторяющиеся элементы):", L1)
print("Список L2 (количество повторений для каждого элемента):", L2)
