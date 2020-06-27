
x = y = c = 0
s = input("Введите числа в шестнадцатиричной системе исчисления: ")
a = s.split()
for i in range(len(a)):
    a[i] = int(a[i], base=16)
x = a[0]
y = a[1]
c = x ^ y
c = hex(c)
print(c)


