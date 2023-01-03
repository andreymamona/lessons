# Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
# В результате ее работы на печать выводятся значения переданных переменных,
# но только если они не равны None. Получим, например, следующее сообщение:
# Переданы аргументы: var1 = 2, var3 = 10.

def three_args(var1, var2, var3):
    tmp_dict = locals()
    print('Переданы аргументы: ', end=' ')
    print(*(f'{key} = {value}' for key, value in tmp_dict.items() if value), sep=', ', end='.\n')


num1 = input('Введите var1: ')
num2 = input('Введите var2: ')
num3 = input('Введите var3: ')

three_args(num1, num2, num3)
