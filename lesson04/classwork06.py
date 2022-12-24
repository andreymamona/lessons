# Вывести в порядке возрастания все простые числа, расположенные между n и m
# (включая сами числа n и m), а также количество x этих чисел.

n = int(input("Input n:"))
m = int(input("Input m:"))
l = m-n+1
for i in range(l):
    for j in range(n+1):
