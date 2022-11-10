class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            self.__check_type(i)
        super().__init__(lst)

    @staticmethod
    def __check_type(num):
        if type(num) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.__check_type(value)
        super().__setitem__(key, value)

    def append(self, num):
        self.__check_type(num)
        super().append(num)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5 # TypeError
print('end')
