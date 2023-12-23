from string import ascii_lowercase, digits

class PhoneBook:    
    def remove_phone(self,indx):
        pass

    def get_phone_list(self):
        pass

    def remove_phone(self, indx):
        pass

class PhoneNumber:
    def __init__(self,number,fio) -> None:
        self.set_number(number)
        self.fio = fio

    def set_number(self, number):
        if len(number) == 11 and set(number) < set(digits):
            self.number = number   
    
    def set_fio(self, fio):
        pass

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
print(p.get_phone_list())