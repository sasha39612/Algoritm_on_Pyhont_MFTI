N = 10 ** 6
a = [] * N
x = 0
for i in range(N):
    a.append(int(input()))
    if a[i] == 0:
        break
a.pop()
for elem in a:
    if elem % 2 == 0:
        x = max(x, elem)

print(x)