class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = True

    @staticmethod
    def __check_index(num):
        if type(num) != int or not (0 <= num < 3):
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        x1 = item[0]
        x2 = item[1]
        if type(x1) == int and type(x2) == slice:
            self.__check_index(x1)
            return tuple(cell.value for cell in self.pole[x1])
        elif type(x1) == slice and type(x2) == int:
            self.__check_index(x2)
            return tuple(row[x2].value for row in self.pole)
        else:
            self.__check_index(x1)
            self.__check_index(x2)
            return self.pole[x1][x2].value

    def __setitem__(self, key, value):
        x1 = key[0]
        x2 = key[1]
        self.__check_index(x1)
        self.__check_index(x2)
        if not bool(self.pole[x1][x2]):
            raise ValueError('клетка уже занята')
        self.pole[x1][x2].value = value
        self.pole[x1][x2].is_free = False


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
print('end')










