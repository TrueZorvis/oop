class Clock:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_time(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock):
        self.__clock1 = clock1
        self.__clock2 = clock2

    def __len__(self):
        diff = self.__clock1.get_time() - self.__clock2.get_time()
        return 0 if diff < 0 else diff

    def __str__(self):
        d = self.__len__()

        h = d // 3600
        m = d % 3600 // 60
        s = d % 3600 % 60

        return f'{h:02}: {m:02}: {s:02}'


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
