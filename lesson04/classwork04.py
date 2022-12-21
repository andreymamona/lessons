import random

r = random.randint(0,10)

if r==7:
    print("Number r equal 7")
else:
    while r != 7:
        print(r)
        r = random.randint(0,10)
    print("Number r equal 7")

