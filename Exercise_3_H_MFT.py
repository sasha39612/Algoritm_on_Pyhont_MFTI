
a = []
c = 0
for i in range(int(input())):
    a.append(int(input()))

for elem in a:
    if elem != 0:
        if elem % 2 == 0:
            c += 1
    else:
        break

print(a)
print(c)