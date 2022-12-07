from random import randint, choice


class Ship:
    def __init__(self, length: int, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(length)]
        self._has_coords = True if x is not None and y is not None else False

    @property
    def has_coords(self):
        return self._has_coords

    def set_start_coords(self, x: int, y: int):
        self._x = x
        self._y = y
        self._has_coords = True if x is not None and y is not None else False

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            elif self._tp == 2:
                self._y += go

    @staticmethod
    def __get_full_coords(length, tp, x, y):
        if tp == 1:
            return {(x + i, y) for i in range(length)}
        elif tp == 2:
            return {(x, y + i) for i in range(length)}

    def is_collide(self, ship):
        this_coords = self.__get_full_coords(self._length, self._tp, self._x, self._y)
        other_coords = ship.__get_full_coords(ship._length, ship._tp, ship._x, ship._y)
        fl_collide = False
        for item in this_coords:
            x, y = item
            temp_set = {(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)}
            if not temp_set.isdisjoint(other_coords):
                fl_collide = True
                break
        return fl_collide

    def is_out_pole(self, size: int):
        if not (0 <= self._x < size) or not (0 <= self._y < size):
            return True

        if self._tp == 1:
            if self._x + (self._length - 1) > (size - 1):
                return True
        elif self._tp == 2:
            if self._y + (self._length - 1) > (size - 1):
                return True

        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size=10):
        self._size = size if size > 0 else 10
        self._ships = []

    def init(self):
        self._ships = [
            Ship(4, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2))
        ]

        for i, ship in enumerate(self._ships):

            ship.set_start_coords(randint(0, 9), randint(0, 9))

            if i == 0:
                while ship.is_out_pole(self._size):
                    ship.set_start_coords(randint(0, 9), randint(0, 9))
            else:
                while ship.is_out_pole(self._size) or \
                        any([ship.is_collide(self._ships[j]) for j in range(len(self._ships)) if i != j and self._ships[j].has_coords]):
                    ship.set_start_coords(randint(0, 9), randint(0, 9))

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for i, ship in enumerate(self._ships):
            go = choice([-1, 1])
            prev_x, prev_y = ship.get_start_coords()

            ship.move(go)
            if ship.is_out_pole(self._size) or \
                    any([ship.is_collide(self._ships[j]) for j in range(len(self._ships)) if i != j]):
                ship.set_start_coords(prev_x, prev_y)
                ship.move(-go)
                if ship.is_out_pole(self._size) or \
                        any([ship.is_collide(self._ships[j]) for j in range(len(self._ships)) if i != j]):
                    ship.set_start_coords(prev_x, prev_y)

    def show(self):
        for row in self.get_pole():
            print(*row)

    def get_pole(self):
        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self.get_ships():
            x, y = ship.get_start_coords()
            tp = ship._tp

            for i in range(ship._length):
                if tp == 1:
                    _x = x + i
                    _y = y
                elif tp == 2:
                    _x = x
                    _y = y + i

                pole[_x][_y] = ship._cells[i]

        return tuple(tuple(row) for row in pole)


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
