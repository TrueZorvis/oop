class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    def __init__(self, volume=0):
        self.__cb = self.__volume = None
        self.volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value


class MoneyR(Money):
    def __init__(self, volume=0):
        super().__init__(volume)

    def __check_register(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

    @staticmethod
    def __get_rubles(other):
        if type(other) is MoneyD:
            currency = round(other.volume * other.cb.rates['rub'], 1)
        elif type(other) is MoneyE:
            currency = round(other.volume / other.cb.rates['euro'] * other.cb.rates['rub'], 1)
        else:
            currency = other.volume

        return currency

    def __eq__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        return self.volume == currency

    def __lt__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        return self.volume < currency

    def __le__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        return self.volume <= currency


class MoneyD(Money):
    def __init__(self, volume=0):
        super().__init__(volume)

    def __check_register(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

    @staticmethod
    def __get_rubles(other):
        if type(other) is MoneyR:
            currency = other.volume
        elif type(other) is MoneyE:
            currency = round(other.volume / other.cb.rates['euro'] * other.cb.rates['rub'], 1)
        else:
            currency = round(other.volume * other.cb.rates['rub'], 1)

        return currency

    def __eq__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        roubles = round(self.volume * self.cb.rates['rub'], 1)
        return roubles == currency

    def __lt__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        roubles = round(self.volume * self.cb.rates['rub'], 1)
        return roubles < currency

    def __le__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        roubles = round(self.volume * self.cb.rates['rub'], 1)
        return roubles <= currency


class MoneyE(Money):
    def __init__(self, volume=0):
        super().__init__(volume)

    def __check_register(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

    @staticmethod
    def __get_rubles(other):
        if type(other) is MoneyD:
            currency = round(other.volume * other.cb.rates['rub'], 1)
        elif type(other) is MoneyR:
            currency = other.volume
        else:
            currency = round(other.volume / other.cb.rates['euro'] * other.cb.rates['rub'], 1)

        return currency

    def __eq__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        roubles = round(other.volume / other.cb.rates['euro'] * other.cb.rates['rub'], 1)
        return roubles == currency

    def __lt__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        roubles = round(other.volume / other.cb.rates['euro'] * other.cb.rates['rub'], 1)
        return roubles < currency

    def __le__(self, other):
        self.__check_register()
        currency = self.__get_rubles(other)
        roubles = round(other.volume / other.cb.rates['euro'] * other.cb.rates['rub'], 1)
        return roubles <= currency


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
