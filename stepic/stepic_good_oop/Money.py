class Money:
    def __init__(self, mn) -> None:
        if self.__check_money(mn):
            self.__money = mn
    
    @classmethod
    def __check_money(cls, money):
        return type(money) == int and money >= 0
    
    def set_money(self, mn):
        if self.__check_money(mn):
            self.__money = mn    
    
    def add_money(self, mn):
            self.__money =  self.__money +  mn.get_money()

    def get_money(self):
        return self.__money

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
print(mn_1.get_money())    # 100
print(mn_2.get_money())    # 120