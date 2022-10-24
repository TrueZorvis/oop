class Vector:
    def __init__(self, *args):
        self.coords = tuple(args)

    @staticmethod
    def __check_type(obj):
        if not isinstance(obj, Vector):
            raise TypeError("Operand must be type Vector")

    def __validate_coords(self, obj):
        if len(self.coords) != len(obj.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __eq__(self, other):
        self.__check_type(other)
        self.__validate_coords(other)
        return self.coords == other.coords

    def __add__(self, other):
        self.__check_type(other)
        self.__validate_coords(other)
        args = tuple(map(lambda x: x[0] + x[1], list(zip(self.coords, other.coords))))
        return Vector(*args)

    def __sub__(self, other):
        self.__check_type(other)
        self.__validate_coords(other)
        args = tuple(map(lambda x: x[0] - x[1], list(zip(self.coords, other.coords))))
        return Vector(*args)

    def __mul__(self, other):
        self.__check_type(other)
        self.__validate_coords(other)
        args = tuple(map(lambda x: x[0] * x[1], list(zip(self.coords, other.coords))))
        return Vector(*args)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.__validate_coords(other)
            args = tuple(map(lambda x: x[0] + x[1], list(zip(self.coords, other.coords))))
            self.coords = args
        elif isinstance(other, int):
            args = tuple(map(lambda x: x + other, self.coords))
            self.coords = args
        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.__validate_coords(other)
            args = tuple(map(lambda x: x[0] - x[1], list(zip(self.coords, other.coords))))
            self.coords = args
        elif isinstance(other, int):
            args = tuple(map(lambda x: x - other, self.coords))
            self.coords = args
        return self


v1 = Vector(1, 2, 3, 4)
v2 = Vector(1, 2, 3, 4)
v3 = Vector(2, 3, 4)
v4 = Vector(2, 1, 4, 3)

v5 = v1 + v2
print('end')








