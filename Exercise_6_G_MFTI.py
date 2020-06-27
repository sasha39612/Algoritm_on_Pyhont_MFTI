
from math import sqrt
z = 0
x, y, r = map(int, input("Введите данные x, y, r: ").split())
def array_search():
    if r < 0:
        return ("Введите радиус окружности > 0: ")
    else:
        z = sqrt(x ** 2 + y ** 2)
        if z <= r:
            return "YES"
        return "NO"
print(array_search())