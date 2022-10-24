class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        method = request.get('method', 'GET')
        if method == 'GET':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"


# contact = HandlerGET(contact)
@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})

print(res)

