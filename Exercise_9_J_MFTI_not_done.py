
n = int(input("Введите к-во слов в словаре: "))
a = []
b = []
a = [list(map(str, input().split())) for i in range(n)]
letters = 0
# FIXME сделать переворачивание символов
# FIXME сделать сортировку по длине символов в слове
# FIXME сделать подсчет символов в слове и вывод их распечатку.

def sortByLenght(a):

    return len(a)


column = 1
for i in range(n):
    for j in range(column):
        print(a[i][j], end=" ")
    print()



