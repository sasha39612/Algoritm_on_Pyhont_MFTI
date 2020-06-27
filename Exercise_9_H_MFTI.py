
N = int(input())
s = input()
a = [] * N
b = [] * N
c = 0
a = s.split()
for i in range(N): # переводим в int для проведения сортировки
    a[i] = int(a[i])
    i += 1
a = sorted(a)
for i in range(N): # переводим в str для возможности работы с len()
    a[i] = str(a[i])
    i += 1
b.append(a[0])
for i in range(N-1): # сравниваем к-во цифр в числе и при отличии на 1 - добавляем в список "b"
    if len(a[i]) < len(a[i + 1]):
        b.append(a[i + 1])
        c += 1
b = ' '.join(b)
print(b)
