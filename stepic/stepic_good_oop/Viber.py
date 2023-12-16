from typing import Any


class Viber:
    msgs = {}

    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений;
        """
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        """удаление сообщения из списка;
        """
        key = id(msg)
        if key in cls.msgs:
            cls.msgs.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        """поставить/убрать лайк для сообщения msg 
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, number):
        """отображение последних сообщений;
        """
        for m in tuple(cls.msgs.values())[-number:]:
            print(m)

    @classmethod
    def total_messages(cls):
        """звращает общее число сообщений.
        """
        return len(cls.msgs)


class Message:
    """позволяет создавать объекты-сообщения со следующим 
    набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения 
    (булево значение True - если лайк есть и False - в противном 
    случае, изначально False);
    P.S. Как хранить список сообщений, решите самостоятельно.
    """
    def __init__(self, text) -> None:
        self.text = text
        self.fl_like = False

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)