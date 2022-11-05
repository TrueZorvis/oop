from random import randrange


class Cell:
    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __bool__(self):
        return True if self.value == 0 else False


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    win_combinations_mask = [[[1, 1, 1], [0, 0, 0], [0, 0, 0]],
                             [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
                             [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
                             [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
                             [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
                             [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
                             [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                             [[0, 0, 1], [0, 1, 0], [1, 0, 0]]]

    win_combinations_human = [[[1, 1, 1], [0, 0, 0], [0, 0, 0]],
                              [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
                              [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
                              [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
                              [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
                              [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
                              [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                              [[0, 0, 1], [0, 1, 0], [1, 0, 0]]]

    win_combinations_comp = [[[2, 2, 2], [0, 0, 0], [0, 0, 0]],
                             [[0, 0, 0], [2, 2, 2], [0, 0, 0]],
                             [[0, 0, 0], [0, 0, 0], [2, 2, 2]],
                             [[2, 0, 0], [2, 0, 0], [2, 0, 0]],
                             [[0, 2, 0], [0, 2, 0], [0, 2, 0]],
                             [[0, 0, 2], [0, 0, 2], [0, 0, 2]],
                             [[2, 0, 0], [0, 2, 0], [0, 0, 2]],
                             [[0, 0, 2], [0, 2, 0], [2, 0, 0]]]

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    @staticmethod
    def __check_index(index):
        i, j = index
        if type(i) != int or type(j) != int or not (0 <= i <= 2) or not (0 <= j <= 2):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != int or value not in (0, 1, 2):
            raise ValueError('некорректно указанное значение ячейки')
        i, j = key
        self.pole[i][j].value = value
        bool(self)

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

    def show(self):
        for row in self.pole:
            for cell in row:
                print(cell.value, end=' ')
            print()
        print('--------------------------')

    def human_go(self):
        index = list(map(int, input('Введите две цифры через пробел от 0 до 2: ').split()))
        self.__check_index(index)
        i, j = index
        while self.pole[i][j].value != self.FREE_CELL:
            index = list(map(int, input('Ячейка уже занята. Введите две цифры через пробел от 0 до 2: ').split()))
            self.__check_index(index)
            i, j = index
        self.pole[i][j].value = self.HUMAN_X

    def computer_go(self):
        index = [randrange(0, 3) for _ in range(2)]
        i, j = index
        while self.pole[i][j].value != self.FREE_CELL:
            index = [randrange(0, 3) for _ in range(2)]
            i, j = index
        self.pole[i][j].value = self.COMPUTER_O

    @property
    def is_human_win(self):
        return self.human_win

    @property
    def is_computer_win(self):
        return self.comp_win

    @property
    def is_draw(self):
        return self.draw

    def __check_win_combination(self, current_pole, win_combinations):
        for win_mask in self.win_combinations_mask:
            check_comb = [[current_pole[i][j] * win_mask[i][j] for j in range(3)] for i in range(3)]
            if check_comb in win_combinations:
                return True
        return False

    def __bool__(self):
        current_pole = []
        for row in self.pole:
            row_pole = []
            for cell in row:
                row_pole.append(cell.value)
            current_pole.append(row_pole)

        self.human_win = self.__check_win_combination(current_pole, self.win_combinations_human)
        self.comp_win = self.__check_win_combination(current_pole, self.win_combinations_comp)
        self.draw = all([x > 0 for row in current_pole for x in row])
        return not (self.human_win or self.comp_win or self.draw)


game = TicTacToe()

game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        print("Ход компьютера:")
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

print('end')
