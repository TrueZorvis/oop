class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    ID = 0

    @classmethod
    def set_id(cls):
        cls.ID += 1
        return cls.ID

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.set_id()

    def get_id(self):
        return self.__id


shop_items = [
    ShopItem("item1", 20, 1000),
    ShopItem("item2", 13, 2100)
]

for i in shop_items:
    print(i.get_id())
print('end')
