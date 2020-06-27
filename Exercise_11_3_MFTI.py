N = int(input())
price = list(map(int, input().split()))

def calculate_min_cost(N, price):

    C = [0] * (N + 1)
    C[1] = price[1]
    for i in range(2, N + 1):
        C[i] = min(C[i - 1], C[i - 2]) + price[i]
    return C[N]
print(calculate_min_cost(N, price))