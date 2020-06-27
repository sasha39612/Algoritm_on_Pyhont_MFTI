N = int(input())
price = [] * (N + 1)
prev = [] * (N + 1)
C = [0] * (N + 1)
prev[1] = 0
C[1] = price[1]
for i in range(2, N + 1):
    if C[i - 1] < C[i - 2]:
        C[i] = C[i - 1] + price[i]
        prev[i] = i - 1
    else:
        C[i] = C[i - 2] + price[i]
        prev[i] = i - 2
path = []
i = N
while i > 0:
    path.append(i)
    i = prev[i]
path.append(0)
path = path[::-1]
print(path)
