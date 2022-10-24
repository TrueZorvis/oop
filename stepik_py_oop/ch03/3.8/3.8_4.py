class Integer:
    def __init__(self, start_value=0):
        self._value = start_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise ValueError('должно быть целое число')
        self._value = val


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.array = [cell(0) for _ in range(max_length)]

    def __getitem__(self, item):
        if not isinstance(item, int) or item < 0 or item >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.array[item].value

    def __setitem__(self, item, value):
        if not isinstance(item, int) or item < 0 or item >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.array[item].value = value

    def __repr__(self):
        values = [str(item.value) for item in self.array]
        return " ".join(values)


ar_int = Array(5, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5  # должно генерироваться исключение ValueError
ar_int[10] = 1  # должно генерироваться исключение IndexError


