"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        gfn = self.name + ' ' + self.surname
        return gfn

    def get_total_income(self):
        gti = sum(self._income.values())
        return gti

    def __str__(self):
        total_info = f" {self.surname} {self.name} " \
                     f"оклад {self._income['wage']} " \
                     f"премия {self._income.get('bonus')} " \
                     f"Итого {self.get_total_income()}"

        return total_info


w1 = Position('Иван', 'Петров', 'босс', 350000, 250000)
w2 = Position('Светалана', 'И', 'мега-босс', 700000, 250000)
print(w1.get_full_name())
print(w1.get_total_income())
print(w2.get_full_name())
print(w2.get_total_income())
print(w1)
