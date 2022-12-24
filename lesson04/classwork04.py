# Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.

import random

r = random.randint(0,10)

if r==7:
    print("Number r equal 7")
else:
    while r != 7:
        print(r)
        r = random.randint(0,10)
    print("Number r equal 7")

