
N = int(input("Введите к-во студентов: "))
a = []
a = [list(map(float, input().split())) for i in range(N)]
a = sorted(a.items(), key=lambda item: item[1]) # FIXME Сделать сортировку по второй колонке (весу студентов)
# FIXME сделать первую колонкуб 2 знака после запятой, вторую колонку, три знака после запятой
column = 2
for i in range(N):
    for j in range(column):
        print(a[i][j], end=" ")
    print()
