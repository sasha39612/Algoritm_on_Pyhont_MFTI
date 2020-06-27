
N = int(input("Введите к-во студентов: "))
K = 10 ** 3
a = []*K
b = []*K
d = "#"
c = b = str("")
for i in range(K):
    a.append(input("Введите число: "))
    if a[i] == d:
        break
x = a.pop()
for i in range(K):
    a[i] = int(a[i])
    print(a)
#def sorter(item):
#    student_id = 10 - item[1]
#    value = 10 - item[2]
#    print(student_id)
#    return (student_id, value)
    #a = []a.sort(key=lambda x: len(x))a[]a.sort(key=lambda x: len(x), reverse=True)[]
#    return a
#sorted_list = sorted(a, key=sorter)

print(a)
#print(b)
#print(sorted_list)