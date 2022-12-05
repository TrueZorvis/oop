class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"{self.__class__.__name__}: x = {self._x}, y = {self._y}"


a, b = input().split()

try:
    a, b = int(a), int(b)
    pt = Point(a, b)
except:
    try:
        a, b = float(a), float(b)
        pt = Point(a, b)
    except:
        pt = Point()
finally:
    print(pt)
