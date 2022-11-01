from typing import Union


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next: Union[StackObj, None] = None

    @property
    def next(self):
        return self.__next

    @property
    def data(self):
        return self.__data

    @next.setter
    def next(self, obj):
        if obj is None or isinstance(obj, StackObj):
            self.__next = obj

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top: Union[StackObj, None] = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            tmp_obj = self.top
            while tmp_obj.next is not None:
                tmp_obj = tmp_obj.next
            tmp_obj.next = obj

    def pop(self):
        tmp_obj = self.top
        if tmp_obj.next is None:
            popped = tmp_obj
            self.top = None
        else:
            while tmp_obj.next is not None:
                if tmp_obj.next.next is None:
                    popped = tmp_obj.next
                    tmp_obj.next = None
                    break
                tmp_obj = tmp_obj.next
        return popped

    def __verify_index(self, index):
        if type(index) != int or index < 0 or index > self.__len__() - 1:
            raise IndexError('неверный индекс')

    def __len__(self):
        if self.top is None:
            return 0
        else:
            i = 0
            tmp_obj = self.top
            while tmp_obj:
                tmp_obj = tmp_obj.next
                i += 1
            return i

    def __get_obj_by_index(self, num):
        tmp_obj = self.top
        i = 0
        while tmp_obj:
            if i == num:
                return tmp_obj
            tmp_obj = tmp_obj.next
            i += 1

    def __getitem__(self, item):
        self.__verify_index(item)
        return self.__get_obj_by_index(item)

    def __setitem__(self, key, value):
        self.__verify_index(key)
        if key == 0:
            value.next = self.top.next
            self.top = value
        else:
            prev_obj = self.__get_obj_by_index(key-1)
            tmp_obj = self.__get_obj_by_index(key)
            value.next = tmp_obj.next
            prev_obj.next = value


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data)  # obj3
print(st[1].data)  # new obj2
# res = st[3]  # исключение IndexError
print('end')







