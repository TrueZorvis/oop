from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = self.__img = 0
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__check_value(value)
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__check_value(value)
        self.__img = value

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self.__real ** 2 + self.__img ** 2)


cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print('end')
