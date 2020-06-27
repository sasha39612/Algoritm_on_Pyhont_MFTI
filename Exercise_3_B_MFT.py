
x1 = int(input(""))
y1 = int(input(""))
x2 = int(input(""))
y2 = int(input(""))
z = 0
def ferz(z):
    if y1 == y2:
        return True
    elif x1 == x2:
        return True
    elif x2 / x1 == y2 / y1:
        return True
    return False

print(ferz(z))