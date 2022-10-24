class FileAcceptor:
    def __init__(self, *args):
        self.extensions = set(args)

    def __call__(self, filename: str):
        extension = filename.split('.')[-1]
        return extension in self.extensions

    def __add__(self, other):
        if not isinstance(other, FileAcceptor):
            raise ArithmeticError("Правый операнд должен быть типом FileAcceptor")
        return FileAcceptor(*self.extensions.union(other.extensions))


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print('end')
