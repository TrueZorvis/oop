class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))
        return wrapper


class RenderDigit:
    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except ValueError:
            return None


@InputValues(render=RenderDigit())
def input_dg():
    return input()


res = input_dg()
print(res)
