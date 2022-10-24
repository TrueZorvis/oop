class WordString:
    def __init__(self, string=''):
        self._string = string

    def __len__(self):
        return len(self._string.split())

    def __call__(self, indx, *args, **kwargs):
        if 0 <= indx <= len(self._string.split()) - 1:
            return self._string.split()[indx]
        return None

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        if type(value) is str:
            self._string = value


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")