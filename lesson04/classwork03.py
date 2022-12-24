# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.

ch = int(input("Input numbr ch:"))
i = 1
summ = 0
while i <= ch :
    summ += i**3
    i += 1

print(summ)