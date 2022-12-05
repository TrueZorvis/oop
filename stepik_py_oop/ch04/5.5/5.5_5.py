class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):
        total_weight = sum(item[1] for item in self._things)
        obj_weight = obj[1]
        if obj_weight + total_weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)

    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, lst):
        self._things = lst


class BoxDefender:
    def __init__(self, box: Box):
        self._box = box
        self.__temp = self._box.things[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box.things = self.__temp
        return False


box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))

print('end')
