#8 Дана строка в которой все слова записаны через пробел. Необходимо посчитать количество слов с четным количеством знаков.

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        if len(word) % 2 == 0:
            count += 1
    return count
