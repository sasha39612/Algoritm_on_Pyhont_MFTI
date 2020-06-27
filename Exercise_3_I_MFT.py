
#a = []
#m = 0
#for i in range(int(input())):
#    a.append(int(input()))

#for elem in a:
#    if elem != 0:
#        m = max(m, elem)
#    else:
#        break

#print(a)
#print(m)

s = '1\n7\n9\n0'
digit = []
m = 0
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digit.append(int(symbol))
for elem in digit:
    if elem != 0:
        m = max(m, elem)
    else:
        break
print(digit)
print(m)
