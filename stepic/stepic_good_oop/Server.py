class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    def __init__(self) -> None:
        self.buffer = []
        self.servers = {}
    
    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None
    
    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data) 
        с указанным IP-адресом получателя (пакет отправляется роутеру и 
        сохраняется в его буфере - локальном свойстве buffer);
        """
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()

    def get_data():
        """возвращает список принятых пакетов (если ничего принято не было, 
        то возвращается пустой список) и очищает входной буфер;
        """
        pass

    def get_ip():
        """возвращает свой IP-адрес.
        """
        pass


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    
    def link(server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        pass
    
    def unlink(server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        pass
    
    def send_data():
        """для отправки всех пакетов (объектов класса Data) из буфера роутера 
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        pass
    

class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """
    pass

# использование
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