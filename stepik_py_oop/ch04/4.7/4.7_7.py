class Note:
    __cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self.__cyrillic_notes:
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __del__(self):
        Notes.__instance = None

    def __init__(self):
        for k, v in zip(self.__slots__, self.__cyrillic_notes):
            setattr(self, k, Note(v, 0))

    @staticmethod
    def __verify_index(indx):
        if type(indx) != int or not (0 <= indx <= 6):
            raise IndexError('недопустимый индекс')

    def __getitem__(self, item):
        self.__verify_index(item)
        return getattr(self, self.__slots__[item])


notes = Notes()

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1  # изменение тональности ноты фа
# notes[3]._name = 'xa'  # ValueError
print('end')
