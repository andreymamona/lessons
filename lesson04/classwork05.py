n = int(input("Input n"))
m = int(input("Input m"))
sum = 0
if n > m :
    print("!!! m > n")
else:
    for n in range(n,m+1):
        sum += n**3
print(sum)