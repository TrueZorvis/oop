class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self, goods=[]):
        self.goods = goods

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        _ = self.goods.pop(indx)

    def get_list(self):
        return [f'{gd.name}:{gd.price}' for gd in self.goods]


cart = Cart()
cart.add(TV('LG', 1500))
cart.add(TV('Sony', 1800))
cart.add(Table('Ikea', 50))
cart.add(Notebook('Asus', 2000))
cart.add(Notebook('Apple', 2700))
cart.add(Cup('Ikea', 5))

print(cart.get_list())
