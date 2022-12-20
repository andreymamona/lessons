# N1. x = 2 + 2 * 2 - 2 / 2

x = 2 + 2 * (2 - 2) / 2
print("x = 2 + 2 * (2 - 2) / 2")
print(x)
y = ((2 + 2 * 2) - 2) / 2
print("y = ((2 + 2 * 2) - 2) / 2")
print(y)

# N2.

my_list = ["P", "y", "t", "h", "o", "n"]

my_str = str()

for i in range(len(my_list)) :
    my_str = my_str + my_list[i]

inv_str = my_str [::-1]

print("Оригинальный список:")
print(my_list)
print("Строка из списка")
print(my_str)
print("Инвертированная строка")
print(inv_str)

# N3.

deposit= 2130
term = 5
percent = 10
bonus = 120

result = deposit
year = 1

while year <= term:
       result = result*1.1 + 120
       year += 1

print(result)
