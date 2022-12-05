class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        raise NotImplementedError("Метод call не переопределен в дочернем классе")


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def __call__(self, value):
        if type(value) != float or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')
        return value


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def __call__(self, value):
        if type(value) != int or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')
        return value


def is_valid(lst, validators):
    result = []
    for data in lst:
        for validator in validators:
            try:
                result.append(validator(data))
            except ValueError:
                pass
    return result


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print('end')
