class ItemAttrs:
    def __init__(self, x=0, y=0):
        self.coord = [x, y]

    def __getitem__(self, item):
        return self.coord[item]

    def __setitem__(self, key, value):
        self.coord[key] = value


class Point(ItemAttrs):
    pass


pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
print('end')
