class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            r, c, v = args
            if type(r) != int or type(c) != int or type(v) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.table = [[v for _ in range(c)] for _ in range(r)]
            self.rows = r
            self.cols = c
        elif len(args) == 1:
            lst2d = list(*args)
            r = len(lst2d)
            c = len(lst2d[0])
            for line in lst2d:
                if len(line) != c:
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
                for el in line:
                    if type(el) not in (int, float):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.table = lst2d
            self.rows = r
            self.cols = c

    def __check_index(self, index):
        r, c = index
        if type(r) != int or type(c) != int or not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def __check_value(value):
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.table[r][c]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__check_value(value)
        r, c = key
        self.table[r][c] = value

    def __check_size(self, mtrx):
        r1, c1 = self.rows, self.cols
        r2, c2 = mtrx.rows, mtrx.cols
        if r1 != r2 or c1 != c2:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if type(other) == Matrix:
            self.__check_size(other)
            return Matrix([[self.table[x][y] + other.table[x][y] for y in range(self.cols)] for x in range(self.rows)])
        else:
            self.__check_value(other)
            return Matrix([[x + other for x in row] for row in self.table])

    def __sub__(self, other):
        if type(other) == Matrix:
            self.__check_size(other)
            return Matrix([[self.table[x][y] - other.table[x][y] for y in range(self.cols)] for x in range(self.rows)])
        else:
            self.__check_value(other)
            return Matrix([[x - other for x in row] for row in self.table])


m1 = Matrix(3, 2, 1)
m2 = Matrix([[1, 2], [3, 4], [5, 6]])
m11 = Matrix([[1, 2], [3, 4]])

res1 = m2[1, 1]
m1[1, 1] = 10

m3 = m1 + m2  # сложение соответствующих значений элементов матриц m1 и m2
m4 = m1 + 10  # прибавление числа ко всем элементам матрицы m1
m5 = m1 - m2  # вычитание соответствующих значений элементов матриц m1 и m2
m6 = m1 - 10  # вычитание числа из всех элементов матрицы m1

# m7 = Matrix(3, 2, '1')  # TypeError
# m8 = Matrix([[1, '2'], [3, 4], [5, 6]])  # TypeError
# m9 = Matrix([[1, 2], [3, ], [5, 6]])  # TypeError
# res2 = m2[2, 2]  # IndexError
# m2[1, 1] = '10'  # TypeError
# m10 = m1 + '10'  # TypeError
# m12 = m2 + m11  # ValueError

print('end')
