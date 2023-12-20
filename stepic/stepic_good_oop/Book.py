class Book:
    def __init__(self, author, title, price) -> None:
        self.__author = author
        self.__title = title
        self.__price = price



book = Book('50 Cent', 'Aboba', 999)
book.set_title('Amogus')
book.set_author('NLE Choppa')
book.set_price(123)
book.get_title()
book.get_author()
book.get_price()