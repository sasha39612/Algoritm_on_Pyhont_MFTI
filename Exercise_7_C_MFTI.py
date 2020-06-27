
N = 10 ** 6
a = [] * N
c = s = x = 0
for i in range(N):
    a.append(float(input()))
    if a[i] == 0:
        break
a.pop()
for elem in a:
    s += elem
    c += 1
x = s / c
x = round(x, 2)
print(x)


