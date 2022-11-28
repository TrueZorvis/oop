from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = self._next = None
        self.data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, obj):
        if obj is None or isinstance(obj, StackObj):
            self._next = obj

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self._data = value


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        tmp = self._top
        if tmp is None:
            self._top = obj
        else:
            while tmp.next:
                tmp = tmp.next
            tmp.next = obj

    def pop_back(self):
        tmp = self._top
        poped = None
        if tmp.next is None:
            poped = tmp
            self._top = None
        else:
            while tmp.next:
                if tmp.next.next is None:
                    poped = tmp.next
                    tmp.next = None
                    break
                tmp = tmp.next
        return poped


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print('end')
