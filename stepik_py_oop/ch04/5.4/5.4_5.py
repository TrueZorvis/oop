class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        self.id = id
        self.pk = pk

    def __str__(self):
        if self.id and not self.pk:
            return f"Значение первичного ключа id = {self.id} недопустимо"
        elif not self.id and self.pk:
            return f"Значение первичного ключа pk = {self.pk} недопустимо"
        else:
            return "Первичный ключ должен быть целым неотрицательным числом"


try:
    err = PrimaryKeyError(id=-10.5)
    print(err)
except PrimaryKeyError as e:
    print(e)

print('end')
