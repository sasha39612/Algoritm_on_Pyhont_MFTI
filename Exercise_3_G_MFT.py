
a = []
s = 0
for i in range(int(input())):
    a.append(int(input()))

for elem in a:
    if elem != 0:
        s += elem
    else:
        break
print(a)
print(s)