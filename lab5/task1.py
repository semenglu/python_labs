import re

def is_valid_phone_number(phone_number):
    """
    Проверяет, является ли строка допустимым телефонным номером.
    Возвращает True, если да, и False в противном случае.
    """
    # Pattern поддерживает теперь форматы: +1234567890, 1234567890,
    # с разделением пробелами или тире, а также 11-значные номера вида 79161234567
    pattern = r'^(\+\d{1,3})?[\s\-]?((\d{3})[\s\-]?){2}(\d{4})$|^(7\d{10})$'
    return re.match(pattern, phone_number) is not None

def validate_phone_number(phone_number):
    """
    Валидирует телефонный номер. Возвращает номер, если он допустим,
    либо выбрасывает исключение ValueError.
    """
    if is_valid_phone_number(phone_number):
        # Форматирование номера для читаемости, необязательно
        if len(phone_number) == 11 and phone_number.startswith('7'):
            formatted_number = f"+{phone_number[:1]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
            return formatted_number
        return phone_number
    else:
        raise ValueError("Некорректный номер телефона")

def main():
    phone_number = input("Введите номер телефона: ")
    try:
        valid_phone_number = validate_phone_number(phone_number)
        print(f"Введен корректный телефонный номер: {valid_phone_number}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
