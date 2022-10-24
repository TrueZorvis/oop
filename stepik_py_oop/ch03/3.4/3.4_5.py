class ListMath:
    def __init__(self, lst=None):
        self.lst_math = [x for x in lst if type(x) in (int, float)] if lst and type(lst) == list else []

    @staticmethod
    def __check_type(value):
        if not isinstance(value, (int, float)):
            raise ArithmeticError("Правый операнд должен быть типом int или float")

    @staticmethod
    def __zero_value(value):
        if value == 0:
            raise ValueError("Делитель не может быть равен нулю")

    def __add__(self, other):
        self.__check_type(other)
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.__check_type(other)
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __sub__(self, other):
        self.__check_type(other)
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        self.__check_type(other)
        return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        self.__check_type(other)
        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __mul__(self, other):
        self.__check_type(other)
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.__check_type(other)
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __truediv__(self, other):
        self.__check_type(other)
        self.__zero_value(other)
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        self.__check_type(other)
        self.__zero_value(other)
        return ListMath([other / x for x in self.lst_math])

    def __itruediv__(self, other):
        self.__check_type(other)
        self.__zero_value(other)
        self.lst_math = [x / other for x in self.lst_math]
        return self


lst = ListMath([1, "abc", -5, 7.68, True])
print(lst.lst_math())

lst = lst + 76  # сложение каждого числа списка с определенным числом
print(lst.lst_math())

lst = 6.5 + lst  # сложение каждого числа списка с определенным числом
print(lst.lst_math())

lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst.lst_math())

lst = lst - 76  # вычитание из каждого числа списка определенного числа
print(lst.lst_math())

lst = 7.0 - lst  # вычитание из числа каждого числа списка
print(lst.lst_math())

lst -= 76.3
print(lst.lst_math())

lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.lst_math())

lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.lst_math())

lst *= 5.54
print(lst.lst_math())

lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
print(lst.lst_math())

lst = 3 / lst  # деление числа на каждый элемент списка
print(lst.lst_math())

lst /= 13.0
print(lst.lst_math())
