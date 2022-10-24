class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __get_mass(self):
        return self.ro * self.volume

    def __eq__(self, other):
        if not isinstance(other, (int, float, Body)):
            raise TypeError('Правый операнд должен быть типом int, float или Body')
        mass = other if isinstance(other, (int, float)) else other.__get_mass()
        return self.__get_mass() == mass

    def __lt__(self, other):
        if not isinstance(other, (int, float, Body)):
            raise TypeError('Правый операнд должен быть типом int, float или Body')
        mass = other if isinstance(other, (int, float)) else other.__get_mass()
        return self.__get_mass() < mass

    def __le__(self, other):
        if not isinstance(other, (int, float, Body)):
            raise TypeError('Правый операнд должен быть типом int, float или Body')
        mass = other if isinstance(other, (int, float)) else other.__get_mass()
        return self.__get_mass() <= mass





