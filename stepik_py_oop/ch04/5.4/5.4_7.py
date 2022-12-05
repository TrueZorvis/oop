class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class Cell:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, '_' + k, v)
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = self._check_value(val)

    def _check_value(self, val):
        raise NotImplementedError("метод должен быть переопределен в дочернем классе")


class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _check_value(self, val):
        if not (self._min_value <= val <= self._max_value):
            raise CellIntegerException("значение выходит за допустимый диапазон")
        return val


class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _check_value(self, val):
        if not (self._min_value <= val <= self._max_value):
            raise CellFloatException("значение выходит за допустимый диапазон")
        return val


class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    def _check_value(self, val):
        if not (self._min_length <= len(val) <= self._max_length):
            raise CellStringException("длина строки выходит за допустимый диапазон")
        return val


class TupleData:
    def __init__(self, *args):
        self.cells = list(args)
        self._length = len(self.cells)

    def __check_index(self, indx):
        if not (0 <= indx < self._length):
            raise IndexError

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item].value

    def __setitem__(self, key, val):
        self.__check_index(key)
        self.cells[key].value = val

    def __len__(self):
        return self._length

    def __iter__(self):
        for item in self.cells:
            yield item.value


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

value = ld[1]  # считывание значения из ячейке с индексом 1
res = len(ld)  # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)

print('end')
