
c = int(input())
n = 10 ** 3
b = []
if c == 0:
    print(2)
else:
    def a(n, adict={0:0, 1:0, 2:1}):
        if n in adict:
            return adict[n]
        adict[n] = a(n - 1) + a(n - 2) + a(n - 3)
        while c < adict[n]:
            b.append(n)
            break
        return adict[n]

    #return adict[n] if n in adict else (a(n - 1) + a(n - 2) + a(n - 3))

    a(n)
    print(b[0])



