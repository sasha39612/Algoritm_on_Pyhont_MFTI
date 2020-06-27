
x = int(input("Введите число: "))
a = input("Введите ответы жителей: ")
b = [] * x
s = c = 0
if 1 < x <= 255:
    a = a.split()
    for i in filter(str.isdigit, a) : b.append(int(i))
    for elem in b:
        s += elem
        c += 1

    print("К-во рыцарей:", s)
    if c != x:
        print("К-во жителей и к-во полученных ответов от жителей не совпадают. Ищите ошибку")

else:
    print("Введите число между 1 и 255")