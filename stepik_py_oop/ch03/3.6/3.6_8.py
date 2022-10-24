class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = []
for lst_item in lst_in:
    args = list(map(str.strip, lst_item.split(';')))
    args[-1] = int(args[-1])
    lst_bs.append(BookStudy(*args))

unique_books = len(set(map(hash, lst_bs)))
print('end')



