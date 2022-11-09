class Vector:
    def __init__(self, *args):
        self.coords = args
        self.size = len(self.coords)

    def _check_size(self, other):
        if other.size != self.size:
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return self.coords

    def __add__(self, other):
        self._check_size(other)
        return Vector(*[self.coords[i] + other.coords[i] for i in range(self.size)])

    def __sub__(self, other):
        self._check_size(other)
        return Vector(*[self.coords[i] - other.coords[i] for i in range(self.size)])


class VectorInt(Vector):
    def __init__(self, *args):
        if not all([isinstance(x, int) for x in args]):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def __add__(self, other):
        if type(other) != VectorInt:
            return super().__add__(other)
        self._check_size(other)
        return VectorInt(*[self.coords[i] + other.coords[i] for i in range(self.size)])

    def __sub__(self, other):
        if type(other) != VectorInt:
            return super().__sub__(other)
        self._check_size(other)
        return VectorInt(*[self.coords[i] - other.coords[i] for i in range(self.size)])


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
print(v1.get_coords())
print(v2.get_coords())
v3 = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
v4 = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
print(v3.get_coords())
print(v4.get_coords())

v5 = VectorInt(1, 2, 3, 4)
v6 = VectorInt(5, 6, 7, 8)
# v7 = VectorInt(1, 0.2, 3, 4)  # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
v8 = Vector(1, 0.2, 3, 4)

v9 = v5 + v6  # v5 - объект класса VectorInt
v10 = v5 - v6  # v5 - объект класса VectorInt
print(type(v9))  # VectorInt
print(type(v10))  # VectorInt
v11 = v5 + v8  # v5 - объект класса VectorInt
v12 = v5 - v8  # v5 - объект класса VectorInt
print(type(v11))  # Vector
print(type(v12))  # Vector
print('end')
