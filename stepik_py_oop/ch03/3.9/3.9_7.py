class IterColumn:
    def __init__(self, lst, column=0):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for row in self.lst:
            yield row[self.column]


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)

for x in it:  # последовательный перебор всех элементов столбца списка: x01, x11, x21, x31
    print(x)

it_iter = iter(it)
x = next(it_iter)
print('end')
