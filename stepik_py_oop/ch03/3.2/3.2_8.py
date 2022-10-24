class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request):
            method = request.get('method', 'GET')
            if method in self.methods:
                method = method.lower()
                return self.__getattribute__(method)(func, request)
            return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})

print(res)

res = contact({"method": "GET", "url": "contact.html"})

print(res)
