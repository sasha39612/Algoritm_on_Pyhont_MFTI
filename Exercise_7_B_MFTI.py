from math import sqrt
a = int(input("Введите сторону треугольника: "))
b = int(input("Введите сторону треугольника: "))
c = int(input("Введите сторону треугольника: "))
h = k = n = bbb = 0

assert a + b > c and a + c > b and b + c > a, "impossible"

if a >= b and a >= c:
    h = a
    k = b
    n = c
if b > a and b >= c:
    h = b
    k = a
    n = c
if c > b and c > a:
    h = c
    k = b
    n = a

def triangle():
    if h == sqrt(k ** 2 + n ** 2):
        return 'right'
    elif h < sqrt(k ** 2 + n ** 2):
        return 'acute'
    elif h > sqrt(k ** 2 + n ** 2):
        return 'obtuse'

print(triangle())