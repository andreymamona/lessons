
my_list = ["P", "y", "t", "h", "o", "n"]

my_str = str()  # создаем пустую строку

for i in range(len(my_list)) :
    my_str = my_str + my_list[i]    # добавляем к строке по одному символу из списка

test_str = "".join(my_list) # right version
print(test_str)

inv_str = my_str [::-1]     # инвертирование строки

print("Оригинальный список:")
print(my_list)
print("Строка из списка")
print(my_str)
print("Инвертированная строка")
print(inv_str)
