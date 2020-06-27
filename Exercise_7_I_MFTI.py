
N = 10 ** 6
a = [] * N
x = 0
for i in range(N):
    a.append(float(input()))
    if a[i] == 0:
        break
a.pop()
x = a[i-6]
print(a)
print(x)