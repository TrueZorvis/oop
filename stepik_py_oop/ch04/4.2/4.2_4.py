class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, things=None):
        things = {} if things is None else things
        if type(things) != dict:
            raise TypeError('аргумент должен быть словарем')

        if things:
            for key in things:
                self.__check_type(key)
        super().__init__(things)

    @staticmethod
    def __check_type(obj):
        if type(obj) != Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')

    def __setitem__(self, key, value):
        self.__check_type(key)
        super().__setitem__(key, value)


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

# dict_things[1] = th_1  # исключение TypeError
print('end')
