class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


lst_in = ['Балакирев; 34; 2048',
          'Mediel; 27; 0',
          'Влад; 18; 9012',
          'Nina P; 33; 0']

players = []
for item in lst_in:
    args = item.split('; ')
    args[-1] = int(args[-1])
    args[-2] = int(args[-2])
    players.append(Player(*args))

players_filtered = list(filter(bool, players))
print('end')










