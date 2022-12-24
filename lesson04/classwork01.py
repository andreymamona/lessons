# Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.

import random

my_list = []
x = random.randint(0,100)

for i in range(100):
    my_list.append(random.randint(0,100))
print(my_list)

result = 0
for elem in my_list:
    if elem > 10:
        result += elem

print(result)

# Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).

n = int(input("Input number:"))
for j in range(1,100):
    if j % n ==0:
        print(j)

###

