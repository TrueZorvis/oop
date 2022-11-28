from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    _id = 0

    @classmethod
    def set_id(cls):
        cls._id += 1
        return cls._id

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.set_id()

    def get_pk(self):
        return self._id


form1 = ModelForm("Логин", "Пароль")
form2 = ModelForm("Логин2", "Пароль2")
print(form1.get_pk())
print(form2.get_pk())
print('end')
