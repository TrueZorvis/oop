class IntegerValue:
    @classmethod
    def verify_value(cls, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows: int, cols: int, cell: CellInteger):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(self.cols)) for _ in range(self.rows))

    def __getitem__(self, item):
        x1 = item[0]
        x2 = item[1]
        return self.cells[x1][x2].value

    def __setitem__(self, key, val):
        x1 = key[0]
        x2 = key[1]
        self.cells[x1][x2].value = val


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
print('end')









