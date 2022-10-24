class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_coord(x):
            self.__x = x
        if self.__check_coord(y):
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check_coord(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check_coord(y):
            self.__y = y

    @classmethod
    def __check_coord(cls, value):
        if type(value) in (int, float):
            return cls.MIN_COORD <= value <= cls.MAX_COORD
        return False

    @staticmethod
    def norm2(vector):
        if isinstance(vector, RadiusVector2D):
            return vector.__x * vector.__x + vector.__y * vector.__y
        return None



v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)

