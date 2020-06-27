N = int(input('Введите к-во чисел: '))
a = [] * N
c = b = x = d = 0
if 0 < N <= 100:
    for i in range(N):
        a.append(int(input()))
    a.sort()
    x = a[0]
    for i in range(N):
        if a[i] == x:
            c += 1
            if b < c:
                d = a[i]
            b = c
        else:
            x = a[i]
            c = 0
    print(d)
else:
    print("Введите число в диапазоне от 0 до 100!")