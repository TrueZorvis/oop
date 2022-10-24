class Morph:
    def __init__(self, *args):
        self.words = list(args)

    def add_word(self, word):
        w = word.lower()
        if w not in self.words:
            self.words.append(w)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        if not isinstance(other, str):
            raise TypeError('Operand must be type str')
        return other.lower() in self.words


s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]

text = 'Мы будем устанавливать связь завтра днем.'

total = 0
for word in text.split():
    total += len(list(filter(lambda obj: word.strip('–?!,.;').lower() == obj, dict_words)))

print(total)
print('end')
