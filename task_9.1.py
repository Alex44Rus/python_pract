class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Number:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f' {value!r} не число')
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class MinMaxNumber:
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):

        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Введено {value!r} должно быть более {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Введено {value!r} должно бытm не более {self.maxvalue!r}'
            )
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    weigth = 25
    thickness = 0.07

    _width = NonNegative()
    #_length = Number()
    _length = MinMaxNumber(4000, 6000)

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        res = self._length * self._width * self.weigth * self.thickness
        return res


road_66 = Road(length=5000, width=20)
print(f"Масса асфальта = {road_66.mass_calc().__round__()} кг. , "
      f"{(road_66.mass_calc() / 1000).__round__()} т.")
