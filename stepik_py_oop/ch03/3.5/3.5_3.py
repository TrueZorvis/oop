class TrackLine:
    def __init__(self, to_x, to_y, max_speed=None):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x=0, start_y=0):
        self.track = [TrackLine(start_x, start_y, None)]

    def add_track(self, tr: TrackLine):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __len__(self):
        distance = 0
        if len(self.track) > 0:
            start = self.track[0]
            x1, y1 = start.to_x, start.to_y
            for obj in self.track[1:]:
                x2, y2 = obj.to_x, obj.to_y
                distance += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                x1, y1 = x2, y2
        return int(distance)


track1 = Track()
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
print(res_eq)

print(track1 == track2)  # маршруты равны, если равны их длины
print(track1 != track2)  # маршруты не равны, если не равны их длины
print(track1 > track2)  # True, если длина пути для track1 больше, чем для track2
print(track1 < track2)  # True, если длина пути для track1 меньше, чем для track2

print('end')

