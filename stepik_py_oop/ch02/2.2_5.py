class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__check_size(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__check_size(height):
            self.__height = height
            self.show()

    @staticmethod
    def __check_size(size):
        return type(size) == int and 0 <= size <= 10000


wnd = WindowDlg('Dialog', 100, 200)
wnd.show()

