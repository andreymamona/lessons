# Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой
# строчный символ, из этих чисел составляется первый список. Далее таким
# же образом вводятся второй и третий списки. Вывести на экран список,
# элементы которого есть в первых двух списках, но отсутствуют в третьем.


list_number = int(0)
first_list = list()
second_list = list()
third_list = list()

while True:
    num = input("Input number: ")
    if num.isdigit() == True:
        if list_number == 0:
            first_list.append(num)
        elif list_number == 1:
            second_list.append(num)
        else:
            third_list.append(num)
    else:
        list_number += 1
        if list_number > 2:
            break

print(first_list)
print(second_list)
print(third_list)

check = False
result_list = list()

for item1 in first_list:
    for item2 in second_list:
        if item1 == item2:
            check = False
            for item3 in third_list:
                if item1 == item3:
                    check = False
                    break
                else:
                    check = True
            if check == True:
                result_list.append(item1)
            break

print(result_list)