"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_func(name="Иван", last_name="Иванов", birth_year=1846,
              city_of_resid="Москва", email="jackie@gmail.com",
              phone_number="01005321456"):
    print(
        f"{name} {last_name} {birth_year} года рождения, проживает в городе"
        f" {city_of_resid}, email: {email}, телефон: {phone_number}")


user_func()

