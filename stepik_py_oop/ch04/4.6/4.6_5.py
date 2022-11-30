class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        return "".join([f"{k}: {v}\n" for k, v in self.__dict__.items()])


class ShopUserView:
    def __str__(self):
        return "".join([f"{k}: {v}\n" for k, v in self.__dict__.items() if k != "_id"])


class Book(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


class Book2(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _id: 1
# _title: Python ООП
# _author: Балакирев
# _year: 2022

book2 = Book2("Python ООП", "Балакирев", 2022)
print(book2)
# на экране увидим строчки:
# _title: Python ООП
# _author: Балакирев
# _year: 2022
print('end')
