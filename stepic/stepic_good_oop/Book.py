class Book:
    def __init__(self, author, title, price) -> None:
        self.__author = author
        self.__title = title
        self.__price = price
    
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
    
    def set_price(self, price):
        self.__price = price
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_price(self):
        return self.__price




book = Book('50 Cent', 'Aboba', 999)
book.set_title('Amogus')
book.set_author('NLE Choppa')
book.set_price(123)
print(book.get_title())
book.get_author()
book.get_price()