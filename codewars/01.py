def remov_nb(n):
    tmp = []
    j = 0
    for i in range(n):
        j = (n*(n+1)/2-i)/(i+1)
        if j%1==0 and j<=n:
            tmp.append((i, j))
            tmp.append((j, i))
            return tmp
    return tmp


t = 0
for n in range(1000):
    if remov_nb(n):
        print(n, n//2, remov_nb(n))
        print(sum(range(n+1)))
        t += 1
print(t)
