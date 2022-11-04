class Cell:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = tuple(tuple(Cell() for _ in range(self.cols)) for _ in range(self.rows))

    def __verify_index(self, index):
        if type(index[0]) != int or type(index[1]) != int \
                or not (0 <= index[0] < self.rows) or not (0 <= index[1] < self.cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__verify_index(item)
        x1 = item[0]
        x2 = item[1]
        return self.cells[x1][x2].data

    def __setitem__(self, key, val):
        if type(val) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.__verify_index(key)
        x1 = key[0]
        x2 = key[1]
        self.cells[x1][x2].data = val

    def __iter__(self):
        for row in self.cells:
            yield (cell.data for cell in row)


table = TableValues(2, 3, int)

# table[0, 0] = 1.45  # генерируется исключение TypeError
# table[1, 3] = 2  # генерируется исключение IndexError

table[1, 1] = 5  # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[1, 1]  # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row:  # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()

print('end')
