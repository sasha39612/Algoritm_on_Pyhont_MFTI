
n = int(input("Введите трехзначное число: "))
sum = 0
digin = 1

while n > 0:
    digin = n % 10
    sum = sum + digin
    n = n // 10
print(sum)
