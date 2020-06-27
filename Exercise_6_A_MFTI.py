

s = str(input("Введите символы строки: "))
k = int(input("Введите степень: "))
a = [0]*k
b = [0]*100
x = z = w = str("")
y = c = 0
if k > 0:
    for i in range(k):
        a.append(s)
        x += a[k]
elif k < 0:
    for i in s:
        y += 1
    y = int(y / (k * -1))
    a = list(s)
    for elem in a:
        if c == y:
            break
        else:
            x += elem
            c += 1
    z = x * (k * -1)
    if s == z:
        x = x
    else:
        x = "NO SOLUTION!"
print(x)


