class Product:
    __id = 0

    @classmethod
    def set_id(cls):
        cls.__id += 1
        return cls.__id

    def __init__(self, name, weight, price):
        self.id = self.set_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")

        if key in ('weight', 'price') and (type(value) not in (int, float) or value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")

        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
