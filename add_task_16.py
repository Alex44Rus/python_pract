"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в
массиве A[1..N]. Пользователь в первой строке вводит натуральное число
N – количество элементов в массиве. В последующих  строках записаны N целых
 чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
"""
import random

n = int(input("Введите количество элементов массива - N  "))
number_list = [i for i in range(n)]
count_ra = 0
for i in range(n):
    number_list[i] = random.randint(1, 5)
print(number_list)
ra = random.randint(1, 5)
for i in range(n):
    if number_list[i] == ra:
        count_ra += 1
print(f" Кочество элементов со значением {ra}  --> {count_ra}")
