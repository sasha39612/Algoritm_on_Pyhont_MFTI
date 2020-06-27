

s = '->1->3->0->3->1->0'
digit = []
m = c = p = 0
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digit.append(int(symbol))
for elem in digit:
    if elem != 0:
        m = max(m, elem)
    else:
        break
for elem in digit:
    if elem !=0:
        if elem == m:
            c += 1
    else:
        break
print(digit)
print(m)
print(c)