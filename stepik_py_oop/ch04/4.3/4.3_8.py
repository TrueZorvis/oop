class SoftList(list):

    def __getitem__(self, item):
        try:
            res = super().__getitem__(item)
        except IndexError:
            res = False
        return res


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
print('end')
