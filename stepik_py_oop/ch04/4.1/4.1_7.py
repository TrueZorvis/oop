class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


class Game(Singleton):
    name = None

    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


g1 = Game('game_1')
g2 = Game('game_2')
print(g1.__dict__)
print(g2.__dict__)
print(g1 == g2)
print(id(g1), id(g2))
print('end')
