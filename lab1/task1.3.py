#функция 3 
#найти НОД  максимального нечетного непростого делителя числа и произведения цифр данного числа

def is_prime(num): #проверка на простоту
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_del(num): #функция нахождения делителей
    delit = []
    for i in range(3, num // 2 + 1, 2):
        if num % i == 0 and not is_prime(i):
            delit.append(i)
    return delit #возвращаем список подходящих делителей числа

def find_result_of_digits(num): #нахождение произведения числа
    product = 1
    for digit in str(num):
        if digit.isdigit():
            product *= int(digit)
    return product

def find_NOD(a, b): #вычисление НОД по алгоритму Эвклида
    while b != 0:
        a, b = b, a % b
    return a

number = int(input())

delit = find_del(number)
largest_odd_not_prime_delit = max(delit)

result = find_result_of_digits(number)

NOD_result = find_NOD(largest_odd_not_prime_delit, result)
print("НОД максимального нечетного непростого делителя числа и произведения цифр данного числа: ", NOD_result)
