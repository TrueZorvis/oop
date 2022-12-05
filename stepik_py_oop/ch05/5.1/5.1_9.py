class Triangle:
    def __init__(self, a, b, c):
        for x in (a, b, c):
            self.__check_type(x)
        self.__check_value(a, b, c)
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def __check_type(x):
        if not isinstance(x, (int, float)) or x <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')

    @staticmethod
    def __check_value(x, y, z):
        if x + y < z or y + z < x or x + z < y:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for item in input_data:
    try:
        t = Triangle(*item)
    except (TypeError, ValueError):
        continue
    lst_tr.append(t)
print('end')
