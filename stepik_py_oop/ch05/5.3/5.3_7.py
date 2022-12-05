class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return str(self)


digits = list(map(float, input().split()))


try:
    t = TupleLimit(digits, 5)
except ValueError as e:
    print(e)
else:
    print(t)

print('end')
