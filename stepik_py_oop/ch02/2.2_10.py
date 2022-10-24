class PhoneNumber:
    def __init__(self, number: int, fio: str):
        self.number = number
        self.fio = fio


class PhoneBook:
    def __init__(self):
        self.phone_book = []

    def add_phone(self, phone: PhoneNumber):
        self.phone_book.append(phone)

    def remove_phone(self, indx: int):
        self.phone_book.pop(indx)

    def get_phone_list(self):
        return self.phone_book


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print([p for p in phones])
p.remove_phone(1)
phones = p.get_phone_list()
print([p for p in phones])
