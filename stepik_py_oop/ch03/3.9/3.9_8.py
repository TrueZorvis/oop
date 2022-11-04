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
        return self.__get_obj_by_index(item).data

    def __setitem__(self, key, value):
        self.__verify_index(key)
        if key == 0:
            self.top.data = value
        else:
            tmp_obj = self.__get_obj_by_index(key)
            tmp_obj.data = value

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            tmp_obj = self.top
            while tmp_obj.next is not None:
                tmp_obj = tmp_obj.next
            tmp_obj.next = obj

    def push_front(self, obj):
        if self.top is None:
            self.top = obj
        else:
            tmp_obj = self.top
            self.top = obj
            obj.next = tmp_obj

    def __iter__(self):
        curr_obj = self.top
        if curr_obj:
            while curr_obj:
                yield curr_obj
                if curr_obj.next:
                    curr_obj = curr_obj.next
                else:
                    break


st = Stack()
st.push_front(StackObj("obj1"))
st.push_back(StackObj("obj2"))
st.push_back(StackObj("obj3"))
st[1] = "new obj2"  # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[2]  # получение данных из объекта стека по индексу
n = len(st)  # получение общего числа объектов стека

for obj in st:  # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

print('end')
