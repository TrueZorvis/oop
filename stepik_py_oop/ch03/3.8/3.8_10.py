class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.st = dict()

    def __update_rows_cols(self):
        self.rows = max([key[0] for key in self.st.keys()]) + 1
        self.cols = max([key[1] for key in self.st.keys()]) + 1

    def add_data(self, row, col, data):
        self.st[(row, col)] = data
        self.__update_rows_cols()

    def remove_data(self, row, col):
        if (row, col) not in self.st.keys():
            raise IndexError('ячейка с указанными индексами не существует')
        self.st.pop((row, col))
        self.__update_rows_cols()

    def __getitem__(self, item):
        if item not in self.st.keys():
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.st.get(item).value

    def __setitem__(self, key, value):
        self.st[key] = Cell(value)
        self.__update_rows_cols()


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25  # изменение значения существующей ячейки
st[11, 7] = 'cell_117'  # создание новой ячейки
print(st[0, 0])  # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5]  # ValueError
# st.remove_data(12, 3)  # IndexError
print('end')
