# Вывести в порядке возрастания все простые числа, расположенные между n и m
# (включая сами числа n и m), а также количество x этих чисел.

n1 = int(input("Input n:"))
m1 = int(input("Input m:"))
x = int(0)  # quantity of simple numbers
list_of_simple = list()

for i in range(n1, m1+1):
    if i == 1:if n1 == 1:
    test = int(1)
else:
        test = int(1)
    else:
        test = int(0)
    for j in range(1, i):
        if i % j == 0:
            test +=1
    if test == 1:
        x += 1
        list_of_simple.append(i)

print("First number: ", n1)
print("Last number: ", m1)
print("Quantity of simple numbers in range: ", x)
print(list_of_simple)
