
n = int(input("Ввведите число: "))
def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)


print(fac(n))

import sys
limit = sys.getrecursionlimit()
print(limit)
