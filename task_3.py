"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
"""
n = int(input("Введите целое положительное число n= "))
if n > 0:
    n = str(n)
    nn = n + n
    nnn = n + n + n
else:
    print("Введенное число не является положительным")
    exit()
res = int(n) + int(nn) + int(nnn)
print(f"n + nn + nnn = {res}")
"""
n = input("Введите целое положительное число n= ")
n = str(n)
nn = n + n
nnn = n + n + n
res = int(n) + int(nn) + int(nnn)
print(f"n + nn + nnn = {res}")
