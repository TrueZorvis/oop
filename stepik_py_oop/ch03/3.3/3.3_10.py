class PolyLine:
    def __init__(self, start_coord: tuple, *args):
        self.coords = [start_coord, *args]

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        if indx < len(self.coords):
            self.coords.pop(indx)

    def get_coords(self):
        return self.coords


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
print(poly.get_coords())