class IteratorAttrs:
    def __iter__(self):
        # return iter(self.__dict__.items())
        # или
        self.index = -1
        return self
        # + __next__()

    def __next__(self):
        self.index += 1
        if self.index < len(self.__dict__) - 1:
            return list(self.__dict__.items())[self.index]
        raise StopIteration


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('nokia', (50, 120), 5)
for attr, value in phone:
    print(attr, value)
print('end')
