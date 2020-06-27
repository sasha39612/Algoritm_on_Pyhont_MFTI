
N = 10 ** 2
a = []*N
b = []*N
c = x = s = n = y = mx = k = p = m = 0
mn = 10 ** 10
d = "#"
for i in range(N):
    a.append(input("Введите число: "))
    if a[i] == d:
        break
x = a.pop()

for elem in a:
    x = int(elem)
    s += int(elem)
    mx = max(mx, x)
    mn = min(mn, x)
    n += 1
    k += int(elem)
    if n % 3 == 0:
        m = k % x
        p += m
        k = 0
if n % 3 == 0:
    x = s / n
    x = round(x, 3)
    print(x, mx, mn, p, end="")
else:
    print("Введите к-во чисел в последовательности кратно трем")

