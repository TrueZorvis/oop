class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET', )):
        super().__init__(methods)

    def render_request(self, request: dict, method: str):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

        f = getattr(self, method.lower(), False)
        # или
        # f = self.__getattribute__(method.lower())

        if f:
            return f(request)

    def get(self, request: dict):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        if 'url' not in request.keys():
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"


dv = DetailView(('GET', 'POST'))
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
print(html)
post = dv.render_request({'url': 'https://site.ru/home'}, 'POST')
print('end')
