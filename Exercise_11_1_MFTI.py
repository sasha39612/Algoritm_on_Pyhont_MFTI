N = int(input())
def trag_number(N):
    k = [0, 1, 2] + [0] * N
    for i in range(3, N + 1):
        k[i] = k[i - 3] + k[i - 2] + k[i - 1]
    return k[N]
print(trag_number(N))