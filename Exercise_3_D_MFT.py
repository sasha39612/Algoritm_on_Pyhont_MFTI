
N = int(input('Введите число: '))
x = m = 1

for i in range(N):
    if N > 10000:
        print("Введите число менее 10000")
        break
    m = x ** 2
    x += 1
    if m < N:
        print(m, " ", end=" ")
    else:
        break


