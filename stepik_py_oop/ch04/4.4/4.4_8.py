class Aircraft:
    def __init__(self, model, mass, speed, top):
        if type(model) != str or type(mass) not in (int, float) or type(speed) not in (int, float) or type(top) not in (int, float):
            raise TypeError('неверный тип аргумента')
        if mass <= 0 or speed <= 0 or top <= 0:
            raise TypeError('неверный тип аргумента')
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        if type(chairs) != int:
            raise TypeError('неверный тип аргумента')
        if chairs < 0:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


planes = [
    PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
    PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
    WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
]
print('end')
