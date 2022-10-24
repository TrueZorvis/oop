class Ellipse:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        self.has_args = False
        if x1 and y1 and x2 and y2:
            self.has_args = True
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

    def __bool__(self):
        if self.has_args:
            return True
        return False

    def get_coords(self):
        if not self.has_args:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


el1 = Ellipse()
el2 = Ellipse()
el3 = Ellipse(1, 2, 3, 4)
el4 = Ellipse(5, 6, 7, 8)

lst_geom = [el1, el2, el3, el4]
for el in lst_geom:
    if el:
        print(el.get_coords())


