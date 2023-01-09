# Известно, что на шахматной доске 8×8 можно расставить ферзей так, чтобы они не били друг друга
# (ферзь может ходить по горизонтали, вертикали и диагонали). Вам дана расстановка двух ферзей на
# доске, определите могут ли ферзи бить друг друга. Программа получает на вход две пары чисел,
# первое число в паре - координата по горизонтали, второе - координата по вертикали. Если ферзи
# не бьют друг друга, выведите слово NO, иначе выведите YES.

def check(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
        print("Yes")
    else:
        print("No")


x1 = int(input('input x1: '))
y1 = int(input('input y1: '))
x2 = int(input('input x2: '))
y2 = int(input('input y2: '))

check(x1, y1, x2, y2)
