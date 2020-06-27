
N = int(input("Введите год: "))

def prime_year(N):
    if N < 0 or N > 100000:
        return False
    elif N % 4 == 0 and N % 100 != 0:
        return True
    elif N % 400 == 0:
        return True

    return False
print(prime_year(N))