from typing import Union


class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next: Union[StackObj, None] = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if obj is None or isinstance(obj, StackObj):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


class Stack:
    def __init__(self):
        self.top: Union[StackObj, None] = None

    def push(self, obj: StackObj):
        if self.top is None:
            self.top = obj
        else:
            _obj = self.top
            while _obj.next is not None:
                _obj = _obj.next
            _obj.next = obj

    def pop(self):
        _obj = self.top
        if _obj.next is None:
            popped = _obj
            self.top = None
        else:
            while _obj.next is not None:
                if _obj.next.next is None:
                    popped = _obj.next
                    _obj.next = None
                    break
                _obj = _obj.next
        return popped

    def get_data(self):
        data = list()
        _obj = self.top
        while _obj:
            data.append(_obj.data)
            _obj = _obj.next
        return data


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st.pop())
print(st.pop())
print(st.pop())
res = st.get_data()    # ['obj1', 'obj2']
print(res)















