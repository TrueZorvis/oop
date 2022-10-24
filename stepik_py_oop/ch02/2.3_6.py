class FloatValue:
    @classmethod
    def verify_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N: int, M: int):
        self.cells = [[Cell() for j in range(M)] for i in range(N)]


N = 5
M = 3
k = 1.0
table = TableSheet(N, M)
for i in range(N):
    for j in range(M):
        table.cells[i][j].value = k
        k += 1.0
print('End')


