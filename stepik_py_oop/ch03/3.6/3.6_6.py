class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name.lower()
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.price == other.price


lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

shop_items = dict()
for item in lst_in:
    name = item.split(': ')[0]
    weight, price = item.split(': ')[1].split()
    key = ShopItem(name, float(weight), float(price))
    if key not in shop_items.keys():
        shop_items[key] = [key, 1]
    else:
        shop_items[key][1] += 1

print(shop_items)

