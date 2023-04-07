"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""


class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        result_m = []
        for row in self.m_list:
            result_m.append(' '.join(str(n) for n in row))
        return '\n'.join(result_m)

    def __add__(self, other):
        if len(self.m_list) == len(other.m_list):
            result_m = []
            for k, row in enumerate(self.m_list):
                new_list = list(map(lambda x, y: x + y, row, other.m_list[k]))
                result_m.append(new_list)
            return Matrix(result_m)
        else:
            return  # или это антипаттерн?


pre_matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pre_matrix_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrix1 = Matrix(pre_matrix_1)
matrix2 = Matrix(pre_matrix_2)
matrix3 = matrix1 + matrix2

print(matrix1, end='\n\n')
print(matrix2, end='\n\n')
print(matrix3)
