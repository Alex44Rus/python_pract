"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и
возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""
try:
    a = int(input("Введите число "))
    b = int(input("В какую степень будем возводить? "))
except ValueError:
    print("Введено не число")
except Exception:
    print("Ошибка")


def math_power(x, y):
    if y == 1:
        return x
    elif y == 0:
        x = 1
        return x
    else:
        return (x * math_power(x, y - 1))


try:
    print(f"A = {a}; B = {b} - > {math_power(a, b)}")
except NameError:
    print("Ошибка")

