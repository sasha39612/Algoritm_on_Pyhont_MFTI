


N = int(input("Введите длину массива: "))
a = []
c = 0
for i in range(N):
    a.append(int(input()))

for i in range(N):
    if a[i] == a[i-1]:
        c += 1
print(c)
