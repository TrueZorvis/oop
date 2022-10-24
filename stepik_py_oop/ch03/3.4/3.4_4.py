class NewList:
    def __init__(self, lst=None):
        self._list = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._list

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError('Правый операнд должен быть типом list или объектом NewList')

        other_list = other if isinstance(other, list) else other._list

        return NewList(self.__diff_list(self._list, other_list))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError('Правый операнд должен быть типом list')
        return NewList(self.__diff_list(other, self._list))

    @staticmethod
    def __diff_list(list_1, list_2):
        if len(list_2) == 0:
            return list_1

        sub = list_2[:]
        return [x for x in list_1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print('end')

