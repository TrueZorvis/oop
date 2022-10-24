class Message:
    def __init__(self, text: str):
        self.text = text
        self.fl_like = False


class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg: Message):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.messages.remove(msg)

    @staticmethod
    def set_like(msg: Message):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, n: int):
        return cls.messages.reverse()[:n]

    @classmethod
    def total_messages(cls):
        return len(cls.messages)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)