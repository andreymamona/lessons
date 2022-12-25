# Ввести с клавиатуры строку, проверить является ли строка палиндромом
# и вывести результат (yes/no) на экран. Палиндром - это слово или фраза,
# которые одинаково читаются слева направо и справа налево

str = input("Input your string:")
str = str.replace(' ', '')  # убираем пробелы из фразы
str = str.casefold()  # переводим всё в нижний регистр

my_list = list(str)
answer = "no"

for i in range(len(my_list)//2):
    # print(my_list[i])
    # print(my_list[-i-1])
    if my_list[i] != my_list[-i-1]:
        answer = "no"
        break
    else:
        answer = "yes"

print(answer)
