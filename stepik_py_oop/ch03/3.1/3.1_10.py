import time


class Filter:
    def __init__(self, date):
        self.__date = None
        self.date = int(date)

    @classmethod
    def __value_verify(cls, value):
        return type(value) == int and value > 0

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if self.__date is None and self.__value_verify(value):
            self.__date = value


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if slot_num in self.slots and self.slots.get(slot_num) is None:
            if slot_num == 1 and isinstance(filter, Mechanical):
                d = {1: filter}
                self.slots.update(d)
            if slot_num == 2 and isinstance(filter, Aragon):
                d = {2: filter}
                self.slots.update(d)
            if slot_num == 3 and isinstance(filter, Calcium):
                d = {3: filter}
                self.slots.update(d)

    def remove_filter(self, slot_num):
        if slot_num in self.slots:
            d = {slot_num: None}
            self.slots.update(d)

    def get_filters(self):
        return tuple(self.slots.values())

    def water_on(self):
        for value in self.slots.values():
            if value is None:
                return False
            if (time.time() - value.date) > self.MAX_DATE_FILTER:
                return False
        return True


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно


