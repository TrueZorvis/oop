class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        return type(data) == float and self._min_value <= data <= self._max_value

    def __call__(self, value):
        return self._is_valid(value)


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
print('end')
