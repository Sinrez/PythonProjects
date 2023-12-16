from string import ascii_lowercase, digits

#дублирование кода сделано умышленно по условиям задачи

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10) -> None:
        self.name = name
        self.size = size
    
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10) -> None:
        self.name = name
        self.size = size
    
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")
        return True

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)