from uuid import uuid4

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies #всего книг
        self.available_copies = total_copies #число доступных книг

    def borrow_book(self):
        """уменьшает количество доступных копий книги на 1, если книги доступны для выдачи"""
        if self.available_copies > 0:
            self.available_copies -= 1
            # print(f"Книга '{self.title}' выдана")
        elif self.available_copies <=0:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        """возврат книги"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1     
        else:
            print(f"Invalid operation. All copies of '{self.title}' have already been returned.") 

class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def display_info(self):
        print(f"Author: {self.name}, Born: {self.birth_year}")

class Reader:
    def __init__(self, name):
        self.name = name
        self.reader_id = hash(uuid4) 

class Librarian:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def issue_book(self, book, member):
        if book.available_copies > 0:
            book.borrow_book()
            print(f"Book '{book.title}' issued to {member.name} with id {member.reader_id} by {self.name}.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable for issuing.")

    def collect_book(self, book, member):
        if book.available_copies < book.total_copies:
            book.return_book()
            print(f"Book '{book.title}' collected from {member.name} with id {member.reader_id} by {self.name}.")
        else:
            print(f"Invalid operation. All copies of '{book.title}' have already been returned.")

if __name__ == '__main__':
    reader = Reader('Peter')
    author = Author('Хэмингуэй','1899')
    book = Book('По ком звонит колокол', author.name, 10)
    librarian = Librarian('Смит', 'Агент')
    librarian.issue_book(book, reader)
    librarian.collect_book(book, reader)