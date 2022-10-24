from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
        self.init()

    def init(self):
        mines_count = 0
        while mines_count < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            mines_count += 1

        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    self.pole[x][y].around_mines = self.get_around_mines(x, y)

    def get_around_mines(self, x, y):
        around_mines = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                _x, _y = k + x, l + y
                if _x < 0 or _y < 0 or _x >= self._n or _y >= self._n:
                    continue
                if self.pole[_x][_y].mine:
                    around_mines += 1
        return around_mines

    def show(self):
        for row in self.pole:
            for cell in row:
                if cell.mine and cell.fl_open:
                    print('*', end=' ')
                elif not cell.mine and cell.fl_open:
                    print(cell.around_mines, end=' ')
                elif not cell.fl_open:
                    print('#', end=' ')
            print()


N = 10  # размер поля NxN
M = 12  # число мин на поле

pole_game = GamePole(N, M)
pole_game.show()



