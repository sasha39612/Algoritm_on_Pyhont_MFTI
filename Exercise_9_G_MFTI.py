
s = input()
    #""" Введите: qwe Rty5, yu! Mama."""
a = b = c = []
y = s.find('.')
x = s.count('.')
a = s[0 : y]
b = s[y :]
a = sorted(a)
a = ''.join(a)
c = a + b
print(c)