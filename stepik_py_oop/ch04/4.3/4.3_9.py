class StringDigit(str):
    def __init__(self, string_digit):
        self.__check_string_digit(string_digit)
        super().__init__()

    @staticmethod
    def __check_string_digit(str_digit):
        if not str_digit.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return StringDigit(str(self).__add__(other))

    def __radd__(self, other):
        return StringDigit(str(other).__add__(self))


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456"  # StringDigit: 123456
print(sd)
sd = "789" + sd  # StringDigit: 789123456
print(sd)
# sd = sd + "12f"  # ValueError
print('end')
