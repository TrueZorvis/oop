from math import sqrt


class InputValue:
    @classmethod
    def verify_value(cls, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Triangle:
    a = InputValue()
    b = InputValue()
    c = InputValue()

    def __init__(self, a, b, c):
        self.__verify_triangle(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __verify_triangle(a, b, c):
        if a > b + c or b > a + c or c > a + b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self)/2
        return sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))





