stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

stich = [row.replace('–', '').replace('?', '').replace('!', '').replace(',', '').replace('.', '').replace(';', '').split()
         for row in stich]


class StringText:
        def __init__(self, lst_words: list):
                self.lst_words = list(lst_words)

        def __len__(self):
                return len(self.lst_words)

        def __lt__(self, other):
                if not isinstance(other, StringText):
                        raise TypeError("Right operand must be type StringText")
                return len(self) < len(other)

        def __le__(self, other):
                if not isinstance(other, StringText):
                        raise TypeError("Right operand must be type StringText")
                return len(self) <= len(other)

        @property
        def get_words(self):
                return self.lst_words


lst_text = [StringText(lst_words) for lst_words in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(obj.get_words) for obj in lst_text_sorted]
print(lst_text_sorted)
