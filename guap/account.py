class BankAccount:
    def __init__(self):
        """Класс банковский счет"""
        self.__balance = 0 #приватный атрибут для хранения текущего баланса счета
        self.__interest_rate = 0 #приватный атрибут для процентной ставки
        self.__transactions = [] #приватный атрибут для списка всех операций,совершенных посчету

    def deposit(self, amount):
        """добавляет сумму amount к балансу и регистрирует транзакцию"""
        self.__balance += amount
        self.__transactions.append(f"Счет пополнен на: {amount} Всего: {self.__balance} |")

    def withdraw(self, amount):
        """вычитает сумму amount из баланса и записывает транзакцию"""
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"Сумма снятия средств со счета: {amount} Всего: {self.__balance} |")
        else:
            self.__transactions.append("Недостаточно средств")

    def add_interest(self, interest_rate):
        """добавляет проценты к счету на основе ставки interest_rate изаписывает транзакцию"""
        self.__interest_rate = interest_rate
        interest = self.__balance * (self.__interest_rate / 100)
        self.__balance += interest
        self.__transactions.append(f"Начислено процентов: {interest} Всего: {self.__balance} |")

    def history(self):
        """печатает список всех операций по счету"""
        return self.__transactions

if __name__ == '__main__':
    print()
    acc1 = BankAccount()
    acc1.deposit(500)
    acc1.withdraw(20)
    acc1.add_interest(5)
    print(*acc1.history())
    print()