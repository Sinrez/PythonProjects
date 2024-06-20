class BankAccount:
    def __init__(self):
        """Класс банковский счет"""
        self.__balance = 0 #приватный атрибут для хранения текущего баланса счета
        self.__interest_rate = 0 #приватный атрибут для процентной ставки
        self.__transactions = [] #приватный атрибут для списка всех операций,совершенных посчету

    def deposit(self, amount):
        """добавляет сумму amount к балансу и регистрирует транзакцию"""
        self.__balance += amount
        self.__transactions.append(f"Deposited: {amount} total: {self.__balance} |")

    def withdraw(self, amount):
        """вычитает сумму amount из баланса и записывает транзакцию"""
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew: {amount} total: {self.__balance} |")
        else:
            self.__transactions.append("Insufficient funds")

    def add_interest(self, interest_rate):
        """добавляет проценты к счету на основе ставки interest_rate изаписывает транзакцию"""
        self.__interest_rate = interest_rate
        interest = self.__balance * (self.__interest_rate / 100)
        self.__balance += interest
        self.__transactions.append(f"Interest added: {interest} total: {self.__balance} |")

    def history(self):
        """печатает список всех операций по счету"""
        return self.__transactions


class Employee:
    def __init__(self):
        self._name = ''
        self._age = 0
        self._salary = 0
    
    @property
    def name(self):
        return self._name
 
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
 
    @age.setter
    def age(self, age):
        self._age = age 

    @property
    def salary(self):
        return self._salary
 
    @salary.setter
    def salary(self, salary):
        self._salary = salary 

if __name__ == '__main__':
    print()
    acc1 = BankAccount()
    acc1.deposit(500)
    acc1.withdraw(20)
    acc1.add_interest(5)
    print(*acc1.history())
    print()
    emp = Employee()
    emp.name = 'John'
    emp.age = 555
    emp.salary = 100500
    print(emp.name)
    print(emp.age)
    print(emp.salary)
    print()