#2 Дана строка в которой слова написаны через пробел. Перемешать слова в строке в случайном порядке.

import random
def shuffle_words(sentence):
    words = sentence.split() #разделение по пробелам
    random.shuffle(words)
    shuffled_sentence = ' '.join(words)
    return shuffled_sentence

sentence = "Квадрат гипотенузы равен сумме квадратов катетов"
print(shuffle_words(sentence))
