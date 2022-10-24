class RenderList:
    def __init__(self, type_list=None):
        if type_list in ('ul', 'ol'):
            self.type_list = type_list
        else:
            self.type_list = 'ul'

    def __call__(self, in_list, *args, **kwargs):
        start_tag = "<" + self.type_list + ">\n"
        end_tag = "</" + self.type_list + ">"
        body = ""
        for item in in_list:
            body += "<li>" + item + "</li>\n"
        return start_tag + body + end_tag


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
