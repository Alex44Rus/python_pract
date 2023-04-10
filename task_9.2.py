class TypedMeta(type):
    """ Метакласс, создающий список __slots__, который будет содержать
    только атрибуты типа TypedProperty"""

    a = None

    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a = super().__call__(*args, **kwargs)
        return cls.a


class NClass(metaclass=TypedMeta):
    def method(self):
        pass


t = NClass()
t1 = NClass()

print(t is t1)
print(t)
print(t1)
