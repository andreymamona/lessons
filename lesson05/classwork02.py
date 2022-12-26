# Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.

def sum_and_max(*args):
    my_sum = 0
    my_min = args[0]
    if len(args):
        for elem in args:
            my_sum += elem
            if elem < my_min:
                my_min = elem
    return my_sum, my_min


#my_list = [1, 2, 3, 4, 34, 323, 553, 34, 35, 65, 66, 554]
print(sum_and_max(1, 2, 3, 4, 34, 323, 553, 34, 35, 65, 66, 554))
