import random


class Line:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

    def set_coords(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

    def set_coords(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

    def set_coords(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
count = 0
while count < 217:
    count += 1
    class_type = random.randint(1, 3)
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)

    if class_type == 1:
        elements.append(Line(a, b, c, d))
    elif class_type == 2:
        elements.append(Rect(a, b, c, d))
    else:
        elements.append(Ellipse(a, b, c, d))

for item in elements:
    if isinstance(item, Line):
        item.set_coords(0, 0, 0, 0)
