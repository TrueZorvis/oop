from random import randint # функция для генерации целых случайных значений в диапазоне [a; b]


class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        rnd_length = randint(self.min_length, self.max_length)
        return ''.join(self.psw_chars[randint(0, len(self.psw_chars)-1)] for _ in range(rnd_length))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)

lst_pass = [rnd() for _ in range(3)]
print(lst_pass)
