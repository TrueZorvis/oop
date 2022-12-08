from random import randint


class Cell:
    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, val):
        if type(val) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = val

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        if type(val) != int or not (0 <= val <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = val

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, val):
        if type(val) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = val

    def __bool__(self):
        return not self.is_open


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.__instance = None

    def __init__(self, N, M, total_mines):
        self._n = N
        self._m = M
        self._total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(M)] for _ in range(N)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        count = 0
        while count < self._total_mines:
            i, j = randint(0, self._n - 1), randint(0, self._m - 1)
            if not self.pole[i][j].is_mine:
                self.pole[i][j].is_mine = True
                count += 1

        for i in range(self._n):
            for j in range(self._m):
                if not self.pole[i][j].is_mine:
                    around_cells = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1),
                                    (i - 1, j), (i + 1, j),
                                    (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]
                    valid_cells = list(filter(lambda c: (0 <= c[0] < self._n) and (0 <= c[1] < self._m), around_cells))
                    self.pole[i][j].number = sum([self.pole[c[0]][c[1]].is_mine for c in valid_cells])

    def open_cell(self, i, j):
        if not (0 <= i < self._n) or not (0 <= j < self._m):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for i in range(self._n):
            for j in range(self._m):
                if self.pole[i][j]:
                    print('.', end=' ')
                else:
                    print('*' if self.pole[i][j].is_mine else self.pole[i][j].number, end=' ')
            print()


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
print('end')
