# Дан список my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
# выведите все элементы, которые меньше 5.

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
short_list = list()

for i in range(len(my_list)):
    if my_list[i] < 5:
        short_list.append(my_list[i])
print(short_list)