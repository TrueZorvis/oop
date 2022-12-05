class ValidatorString:
    def __init__(self, min_length: int, max_length: int, chars: str):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if type(string) != str or not (self.min_length <= len(string) <= self.max_length):
            raise ValueError('недопустимая строка')

        if self.chars:
            if not any([char in self.chars for char in string]):
                raise ValueError('недопустимая строка')

        return string


class LoginForm:
    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = self._password = None

    def form(self, request: dict):
        if 'login' not in request.keys() or 'password' not in request.keys():
            raise TypeError('в запросе отсутствует логин или пароль')
        self._login = self.login_validator.is_valid(request.get('login'))
        self._password = self.password_validator.is_valid(request.get('password'))


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
# login, password = input().split()
login, password = "sergey balakirev!".split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)

print('end')
