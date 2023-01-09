# Доработать первое задание так, чтобы словарь читался из текстового CSV файла,
# где на каждой строке пары слов вида: apple,яблоко.

import csv

with open("dictionary.csv", "r") as file:
    reader = csv.reader(file)
    dictionary = {
        row[0]: row[1]
        for row in reader
    }


def eng_to_rus(word):
    return dictionary.get(word, "ERROR")


def rus_to_eng(word):
    return {
        value: key
        for key, value in dictionary.items()
    }.get(word, "ERROR")


def rus_to_eng2(word):
    for eng, rus in dictionary.items():
        if rus == word:
            return eng


print(eng_to_rus('apple'))
print(rus_to_eng('зеленый'))
print(rus_to_eng2('машина'))
