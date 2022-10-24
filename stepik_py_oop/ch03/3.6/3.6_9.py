class Dimensions:
    def __init__(self, a, b, c):
        if self.__verify(a, b, c):
            self.a = a
            self.b = b
            self.c = c

    @staticmethod
    def __verify(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        return True

    def __hash__(self):
        return hash((self.a, self.b, self.c))


s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'

lst_dims = []
for dims in s_inp.split('; '):
    lst = map(float, dims.split())
    lst_dims.append(Dimensions(*lst))

lst_dims = sorted(lst_dims, key=hash)

print('end')



