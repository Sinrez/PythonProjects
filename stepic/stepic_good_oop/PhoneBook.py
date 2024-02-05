from string import digits

class PhoneBook:    
    def __init__(self) -> None:
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(phone)

    def get_phone_list(self):
        return self.phones

    def remove_phone(self, indx):
        self.phones.pop(indx)

class PhoneNumber:
    def __init__(self,number,fio) -> None:
        self.set_number(number)
        self.set_fio(fio)

    def set_number(self, number):
        # if len(str(number)) == 11 and set(str(number)) < set(digits):
        if len(str(number)) == 11 and type(number) == int:
            self.number = number   
    
    def set_fio(self, fio):
        if fio.isalpha():
            self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
print(p.get_phone_list())