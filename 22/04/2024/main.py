def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
m = int(input())
n = faktorial(m)
print(n)

n = int(input())
n_vuruq = 2
b = []
while n >1:
    if n % n_vuruq == 0:
        if b.count(n_vuruq) == 0:
            b.append(n_vuruq)
            print(n_vuruq)
        n = n // n_vuruq
    else:
        n_vuruq = n_vuruq + 1


