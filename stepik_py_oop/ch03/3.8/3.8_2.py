class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __get_key_by_index(self, index):
        i = 0
        for k in self.__dict__.keys():
            if index == i:
                return k
            i += 1
        return None

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0 or index > len(self.__dict__):
            raise IndexError('неверный индекс поля')
        key = self.__get_key_by_index(index)
        self.__dict__[key] = value

    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0 or index > len(self.__dict__):
            raise IndexError('неверный индекс поля')
        key = self.__get_key_by_index(index)
        return self.__dict__.get(key)


r = Record(id=1, name='Rustam', age=37)
r[2] = 38
print(r[1])
print('end')




