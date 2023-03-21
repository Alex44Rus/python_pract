"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


a = int(input("Введите первое число  "))
b = int(input("Введите второе число  "))
c = int(input("Введите третье число  "))


def my_func(a, b, c):
    num = [a, b, c]
    num.sort()

    return num[1] + num[2]


print(f"Решение с sort {my_func(a, b, c)}")


def my_func_2(a, b, c):
    numb = [a, b, c]
    for i in range(0, len(numb) - 1):
        for j in range(len(numb) - 1):
            if numb[j] < numb[j + 1]:
                numb[j], numb[j + 1] = numb[j + 1], numb[j]
    return numb[0] + numb[1]


print(f"Решение без функции sort {my_func_2(a, b, c)}")
