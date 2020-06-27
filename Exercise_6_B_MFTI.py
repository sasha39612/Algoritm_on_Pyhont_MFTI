

x, p, y = map(int, input("Введите данные x, p, y: ").split())
c = 0
while x < y:
    x = x + x * p / 100
    x = round(x, 2)
    c += 1
    print(x)

print(c)






