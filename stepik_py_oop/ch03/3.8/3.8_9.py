class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []
        self.current_weight = 0

    def __check_weight(self, thing: Thing):
        if self.current_weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        return True

    def add_thing(self, thing: Thing):
        if self.__check_weight(thing):
            self.things.append(thing)
            self.current_weight += thing.weight

    def __check_index(self, index):
        if type(index) != int or index < 0 or index > len(self.things) - 1:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.things[item]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.current_weight -= self.things[key].weight
        if self.__check_weight(value):
            self.things[key] = value
            self.current_weight += self.things[key].weight
        else:
            self.current_weight += self.things[key].weight

    def __delitem__(self, key):
        self.__check_index(key)
        self.current_weight -= self.things[key].weight
        return self.things.pop(key)


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300))  # генерируется исключение ValueError
print(bag[2].name)  # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name)  # платок
del bag[0]
print(bag[0].name)  # платок
# t = bag[4]  # генерируется исключение IndexError
print('end')
