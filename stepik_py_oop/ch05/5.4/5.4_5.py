class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        if id and not pk:
            self.message = f"Значение первичного ключа id = {id} недопустимо"
        elif not id and pk:
            self.message = f"Значение первичного ключа pk = {pk} недопустимо"
        else:
            self.message = "Первичный ключ должен быть целым неотрицательным числом"

    def __str__(self):
        return self.message


try:
    err = PrimaryKeyError(id=-10.5)
    print(err)
except PrimaryKeyError as e:
    print(e)

print('end')
