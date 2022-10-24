import sys


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['Python ООП', 'Балакирев С.М.', 1024]

book = Book(*lst_in)
print(book)





