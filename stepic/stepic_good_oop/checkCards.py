from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        # Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)
        if type(number) != str:
            return False
        else:
            card_list = number.split('-')
            if len(card_list) != 4:
                return False
            if not all(map(lambda c: c.isdigit(), card_list)):
                return False
            if not all(len(card) == 4 for card in card_list):
                return False
        return True
            

    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            return False
        s = name.split()
        if len(s) != 2:
            return False
        set_chars = set(cls.CHARS_FOR_NAME)
        return all(map(lambda x: set(x)<set(set_chars),s))
        

string = '1244-5678-9012-0000-1234'
a = CardCheck.check_card_number(string)
b = CardCheck.check_name('SERGEI BALAKIREV')
print(a)
print(b)