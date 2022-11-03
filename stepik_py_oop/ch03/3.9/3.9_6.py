class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.cur_i = -1
        self.cur_j = -1
        return self

    def __next__(self):
        self.cur_j += 1
        if self.cur_j > self.cur_i:
            self.cur_i += 1
            self.cur_j = 0
        if self.cur_i < len(self.lst):
            return self.lst[self.cur_i][self.cur_j]
        else:
            raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
print('end')
