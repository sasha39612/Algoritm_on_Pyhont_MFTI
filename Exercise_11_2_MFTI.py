N = int(input())
def trag_number(N):
    x = 0
    k = [0, 1, 2] + [0] * N
    for i in range(3, N + 1):
        if i % 3 == 0:
            x += k[i]
        k[i] = x + k[i - 2] + k[i - 1]
        x = 0
    return k[N]
print(trag_number(N))