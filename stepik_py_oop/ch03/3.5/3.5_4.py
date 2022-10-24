from typing import Union


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = 0
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __verify_value(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__verify_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__verify_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__verify_value(value):
            self.__c = value

    @property
    def volume(self):
        return self.a * self.b * self.c

    def __lt__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError("Operand must be type Dimensions")
        return self.volume < other.volume

    def __le__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError("Operand must be type Dimensions")
        return self.volume <= other.volume


class ShopItem:
    def __init__(self, name: str, price: Union[int, float], dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]


lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume)

# для отладки сортировки
for obj in lst_shop_sorted:
    print(f'{obj.name:12} {obj.dim.a * obj.dim.b * obj.dim.c}')
print('end')
