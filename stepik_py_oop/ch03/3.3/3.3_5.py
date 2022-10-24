class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = ""
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj


class LinkedList:
    def __init__(self):
        self.head: ObjList = None
        self.tail: ObjList = None

    def add_obj(self, obj: ObjList):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_indx(self, indx):
        _obj = self.head
        i = 0
        while _obj and i < indx:
            _obj = _obj.next
            i += 1
        return _obj

    def remove_obj(self, indx):
        current_obj = self.__get_obj_by_indx(indx)

        if current_obj is None:
            return None

        prev_obj = current_obj.prev
        next_obj = current_obj.next

        if prev_obj:
            prev_obj.next = next_obj
        if next_obj:
            next_obj.prev = prev_obj

        if self.head == current_obj:
            self.head = next_obj
        if self.tail == current_obj:
            self.tail = prev_obj

    def __len__(self):
        i = 0
        current_obj = self.head
        while current_obj:
            i += 1
            current_obj = current_obj.next
        return i

    def __call__(self, indx, *args, **kwargs):
        current_obj = self.__get_obj_by_indx(indx)
        return current_obj.data if current_obj else None


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
print(n)
s = linked_lst(1)  # s = Balakirev
print(s)
