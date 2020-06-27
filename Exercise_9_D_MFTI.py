N = 10
a = []
s = input()
a = s.split()
mon = 0
for i in range(len(a)):
    a[i] = int(a[i])

def money():
    mon = 0
    day = 1
    price = a[0]
    delta = a[1]
    m = a[2]
    while (day - 1) // 7 < m:
        if day >= 2:
            price = price + delta
        mon = mon + price
        day = day + 1
    return mon
print(money())