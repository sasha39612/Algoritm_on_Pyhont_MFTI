
s = input()

def brackets():
    c = 0
    for elem in s:
        if elem == '(':
            c += 1
        elif elem == ')':
            c -= 1
        if c < 0:
            return "NO"
    return "YES" if c == 0 else "NO"

print(brackets())