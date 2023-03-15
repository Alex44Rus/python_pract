"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно
 перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random

n = int(input("Введите количество монет  "))
coins = [i for i in range(n)]
count_tails = 0
count_heads = 0
for i in range(n):
    coins[i] = random.randint(0, 1)
    if coins[i] == 0:
        count_tails = count_tails + 1
    else:
        count_heads = count_heads + 1
if count_heads < count_tails:
    print(f" Надо перевернуть минимум {count_heads} монет")
else:
    print(f" Надо перевернуть минимум {count_tails} монет")
