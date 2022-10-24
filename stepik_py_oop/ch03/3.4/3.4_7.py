class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        if not isinstance(other, Book):
            raise ArithmeticError("Правый операнд должен быть объектом типа Book")
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Book)):
            raise ArithmeticError("Правый операнд должен быть типом int или Book")
        if type(other) == int:
            if 0 <= other < len(self.book_list):
                self.book_list.pop(other)
        if type(other) == Book:
            self.book_list.remove(other)
        return self
