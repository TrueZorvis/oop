class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    __ip = 0

    def __init__(self):
        self.buffer: list[Data] = []
        self.ip = self.set_ip()
        self.router = None

    @classmethod
    def set_ip(cls):
        cls.__ip += 1
        return cls.__ip

    def send_data(self, data: Data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        buffer_out = self.buffer[:]
        self.buffer = []
        return buffer_out

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.links = set()

    def link(self, server: Server):
        self.links.add(server)
        server.router = self

    def unlink(self, server: Server):
        self.links.discard(server)
        server.router = None

    def send_data(self):
        for d in self.buffer:
            for l in self.links:
                if d.ip == l.ip:
                    l.buffer.append(d)
        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print("end")