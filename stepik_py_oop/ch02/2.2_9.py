from math import sqrt


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """Строковое представление - для отладки"""
        return f"{self.x}:{self.y}"


class PathLines:
    def __init__(self, *lines):
        self.lines = [line for line in lines]

    def get_path(self):
        return self.lines

    def get_length(self):
        total_length = 0
        for i, line in enumerate(self.lines):
            if i == 0:
                x0 = y0 = 0
            else:
                prev_line = self.lines[i-1]
                x0 = prev_line.x
                y0 = prev_line.y
            x1 = line.x
            y1 = line.y
            total_length += sqrt((x1-x0)**2 + (y1-y0)**2)
        return total_length

    def add_line(self, line: LineTo):
        self.lines.append(line)


# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# path_list = p.get_path()
# dist = p.get_length()
# print(dist)
# print(LineTo(10, 20))
