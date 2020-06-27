a = []
s = list(bin(int(input("Введите число: "))))
c = 0
for i in filter(str.isdigit, s) : a.append(int(i))
for elem in a:
    if elem == 1:
        c += 1
print(c)