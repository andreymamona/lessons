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

###

n = int(input("Input number:"))
for j in range(1,100):
    if j % n ==0:
        print(j)

###

