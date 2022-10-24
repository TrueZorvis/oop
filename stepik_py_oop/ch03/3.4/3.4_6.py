class StackObj:
    def __init__(self, data):
        self.__data = self.__next = None
        self.data = data

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
    def data(self, value):
        if type(value) == str:
            self.__data = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        tmp = self.top
        if tmp is None:
            self.top = obj
        else:
            while tmp.next:
                tmp = tmp.next
            tmp.next = obj

    def pop_back(self):
        tmp = self.top
        if tmp.next is None:
            self.top = None
        else:
            while tmp.next:
                if tmp.next.next is None:
                    tmp.next = None
                    break
                tmp = tmp.next

    def __add__(self, other):
        if not isinstance(other, StackObj):
            raise ArithmeticError("Операнд должен быть типом StackObj")
        self.push_back(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, list):
            raise ArithmeticError("Операнд должен быть списком")
        for itm in other:
            self.push_back(StackObj(itm))
        return self

    def show(self) -> None:
        tmp = self.top
        while tmp.next is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print(tmp.data)


h = StackObj('5')
print(h._StackObj__data)  # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st.show()  # 1 2 3
st.pop_back()
st.show()  # 1 2
st = st + StackObj('4')
st += StackObj('5')
st.show()  # 1 2 4 5
st = st * [str(i) for i in range(6, 9)]
st *= [str(i) for i in range(9, 12)]
st.show()  # 1 2 4 5 6 7 8 9 10 11
print('end')
