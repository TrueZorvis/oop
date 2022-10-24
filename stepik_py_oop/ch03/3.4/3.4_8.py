class Item:
    def __init__(self, name: str, money: float | int):
        self.name = name
        self.money = money

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ArithmeticError("Right operand should be type Item")
        return self.money + other.money

    def __radd__(self, other):
        if not isinstance(other, (int, float)):
            raise ArithmeticError("Right operand should be type int or float")
        return self.money + other


class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        self.items.pop(indx)

    def get_items(self):
        return self.items


it1 = Item("Name1", 10)
it2 = Item("Name2", 20.5)
it3 = Item("Name3", 30)

s = it1 + it2 + it3
print(s)

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x

print(s)
