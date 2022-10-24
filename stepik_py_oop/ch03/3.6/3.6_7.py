class Record:
    pk = 0

    @classmethod
    def set_pk(cls):
        cls.pk += 1
        return cls.pk

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = int(old)
        self.pk = self.set_pk()

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


class DataBase:
    def __init__(self, path: str = 'default.db'):
        self.path = path
        self.dict_db = dict()

    def write(self, record: Record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]


db = DataBase()

for lst_item in lst_in:
    args = list(map(str.strip, lst_item.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))

rec = db.read(pk=2)
print(rec)
print('end')




