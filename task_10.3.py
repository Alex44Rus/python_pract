"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
words = ['attribute', 'класс', 'функция', 'type']
j = 0

for i in words:
    try:
        wb = bytes(i, encoding='ascii')
        print(f'{wb} можно ')
    except UnicodeEncodeError:
        j += 1
        print(f' {words[j]} нельзя !!')
