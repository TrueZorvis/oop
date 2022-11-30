class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request.get('method').upper() not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")

        method_request = request.get('method').lower()  # имя метода, малыми буквами
        return self.__getattribute__(method_request)(request)


class DetailView1(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


class DetailView2(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


view1 = DetailView1()
html1 = view1.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
print(html1)   # GET: https://stepik.org/course/116336/

# AttributeError: 'DetailView' object has no attribute 'put'
# html2 = view1.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})

view2 = DetailView2()
html3 = view2.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html3)  # PUT: https://stepik.org/course/116336/
print('end')
