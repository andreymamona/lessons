# Написать функцию принимающая на вход неопределенным количеством аргументов
# и именованный аргумент func_type. В зависимости от func_type вернуть минимальное
# либо максимальное значение. Написать программу в виде трех функций.

def my_func (*args, func_type):
    if func_type == "min":
        return min(args)
    elif func_type == "max":
        return max(args)
    raise "Unknown func"


print(my_func(3, 4, 6, 4, 4, 7, func_type="min"))
