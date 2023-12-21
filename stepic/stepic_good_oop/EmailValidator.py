from random import randint
from string import ascii_lowercase, ascii_uppercase,digits

class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits +'_.@'
    EMAIL_RANDOM_CHARS = ascii_lowercase + ascii_uppercase + digits

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        n = randint(4,20)
        length = len(cls.EMAIL_RANDOM_CHARS)-1
        return ''.join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + '@gmail.com'

    @classmethod    
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return 
        
        if not  set(email) < set(cls.EMAIL_CHARS):
            return False
        
        s = email.split('@')
        if len(s) != 2:
            return False
        
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        
        if "." not in s[1]:
            return False
        
        if email.count('..') > 0:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


print(EmailValidator.check_email("sc_lib@list.ru")) # True
print(EmailValidator.check_email("sc_lib@list_ru")) # False