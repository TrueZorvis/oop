class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head: ObjList = None
        self.tail: ObjList = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            tail_obj = self.tail
            tail_obj.set_next(obj)
            self.tail = obj
            self.tail.set_prev(tail_obj)

    def remove_obj(self):
        if self.head.get_next() is None:
            self.head = None
            self.tail = None
        else:
            prev_obj = self.tail.get_prev()
            prev_obj.set_next(None)
            self.tail = prev_obj

    def get_data(self):
        data = list()
        if self.head is None:
            pass
        else:
            _obj = self.head
            while _obj is not None:
                data.append(_obj.get_data())
                _obj = _obj.get_next()
        return data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)
print("End")
