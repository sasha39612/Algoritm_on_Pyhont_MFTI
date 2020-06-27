
def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)


def generate_number(N:int, M:int, prefix=None):
    """Генерирует все числа (с лидирующими незачищими нулями) в N-ричной системе исчисления (N <=10)
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()

# только для двоичной системы ОС:
gen_bin(5)

# для произвольной СС:
generate_number(4, 3)


def find(number, A):
    """ ищет number в А и возвращает True, если такой есть - False, если такого нет
    """
    for x in A:
        if number == x:
            return True
    return False

def generate_permutation(N:int, M:int=-1, prefix=None):
    """Генерация всех перестановок N чисел в М позициях, с префиксом prefix
    """
    M = N if M == -1 else M  # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=", ", sep="")
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutation(N, M-1, prefix)
        prefix.pop()

generate_permutation(4)
