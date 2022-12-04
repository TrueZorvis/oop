class Test:
    MIN_LENGTH = 10
    MAX_LENGTH = 10000

    def __init__(self, descr: str):
        if not (self.MIN_LENGTH <= len(descr) <= self.MAX_LENGTH):
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit-self.max_error_digit <= ans <= self.ans_digit+self.max_error_digit


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

try:
    test_d = TestAnsDigit(descr, ans)
except ValueError as e:
    print(e)
else:
    print(test_d.run())

print('end')
