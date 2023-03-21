"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное число
N – количество элементов в массиве. В последующих  строках записаны N целых
чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random
from copy import copy

n = int(input("Введите количество элементов массива - N  "))
number_list = [i for i in range(n)]
temp_list = [i for i in range(n)]
num_count = 10
b = False
for i in range(n):
    number_list[i] = random.randint(1, 5)
print(number_list)
find_num = int(input("Какое число  будем искать?  "))
for i in range(n):
    if number_list[i] == find_num:
        b = True
    else:
        for j in range(n):
            temp_list[j] = abs((find_num - number_list[j]) / find_num)
            if temp_list[j] < num_count:
                num_count = temp_list[j]
                a = j
if b:
    print(f" Число {find_num} найдено")
else:
    print(f" Наиболее близкое к {find_num} нашлось - {number_list[a]}")

