class Rect:
    def __init__(self, x, y, width, height):
        if type(x) not in (int, float) or type(y) not in (int, float) or width <= 0 or height <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def is_collision(self, rect):
        pass
        # raise TypeError('прямоугольники пересекаются')


lst_rect = [
    Rect(0, 0, 5, 3),
    Rect(6, 0, 3, 5),
    Rect(3, 2, 4, 4),
    Rect(0, 8, 8, 1)
]


lst_not_collision = []
for i in range(len(lst_rect)):
    for j in range(i+1, len(lst_rect)):
        try:
            lst_rect[i].is_collision(lst_rect[j])
        except TypeError:
            pass
        else:
            lst_not_collision.append(lst_rect[i])

print(lst_not_collision)
print('end')
