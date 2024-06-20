 """
Класс - абстракция, шаблон, описывающий объект.
Класс описывает какими свойствами и поведением будет обладать объект этого класса."""
"""
Объект — это определённая сущность (экземпляр) с собственным состоянием этих свойств и набором доступных действий. 
"""


# # создание класса
# class MyClass():
#     pass
#
# # создание объекта класса
# obj = MyClass()

# атрибуты экземпляра класса
# class Person():
#     def __init__(self, name, surname, age, height, weight):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.height = height
#         self.weight = weight
#
# person1 = Person('Ivan', 'Ivanov', '37', '177', '65')
# person2 = Person('Nastya', 'Ivanova', '34', '163', '50')
# print(person1.name)
# print(person1.age)
#
# print(person2.name)
# print(person2.age)

# методы экземляра класса
# class ExampleClass:
#     """
#     Класс демонстрирует простой пример с двумя атрибутами
#     """
#
#     def __init__(self, a, b):
#         """
#         Инициализирует экземпляр класса с заданными значениями a b
#         """
#         self.a = a
#         self.b = b
#
#     def update_a(self, new_a):
#         """
#         Обновление значения атрибута а
#         :param new_a:
#         :return:
#         """
#         self.a = new_a
#         return self.a
#
#     def print_b(self):
#         print(f"b = {self.b}")
#
# obj = ExampleClass(4, 2)
# print(obj.update_a(10))
# obj.print_b()
# obj.b = 5
# obj.print_b()
# help(ExampleClass)
# help(obj.update_a)

# пример1 - атрибуты класса, методы класса
# class Book:
#     # Атрибут класса для подсчета количества экземпляров
#     total_books = 0
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         # Увеличение счетчика при создании нового экземпляра
#         Book.total_books += 1
#
#     @classmethod
#     def get_total_books(cls):
#         return cls.total_books
#
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}")
#
# # Создание экземпляров
# book1 = Book("Статистика и котики", "Владимир Савельев")
# book2 = Book("Мастер и Маргарита", "Михаил Булгаков")
# book3 = Book("Искусство цвета", "Иоханнес Иттен")
#
# # Использование метода класса для получения общего количества книг
# print(f"Total books: {Book.get_total_books()}")
#
# # Вывод инф
# book1.display_info()
# book2.display_info()
# book3.display_info()

# пример2 - атрибуты класса, методы класса
# class Message:
#     _id = 0
#
#     def __init__(self, data):
#         self._msg_id = Message._id
#         self._data = data
#         Message._id += 1  # Обращение к атрибуту класса внутри конструктора
#
#     def print(self):
#         print(f"{self._data}\t obj id: {self._msg_id}  /  cls id: {self._id}")
#
#     @classmethod
#     def next_free_id(self):
#         return Message._id
#
#     @staticmethod
#     def static():
#         print("Это статический метод")
#
#
# m1 = Message("First message")
# m2 = Message("Second message")
#
# m1.print()
# m2.print()
#
# print(Message.next_free_id())
# Message.static()

# # Пример с альтернативным конструктором
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     @classmethod
#     def from_string(cls, date_string):
#         year, month, day = map(int, date_string.split('-'))
#         return cls(year, month, day)
#
# # основной конструктор
# date1 = Date(2024, 5, 19)
# print(date1.year, date1.month, date1.day)
#
# # альтернативный конструктор
# date2 = Date.from_string("2024-05-19")
# print(date2.year, date2.month, date2.day)


# Наследование
# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
# class KitchenTable(Table):
#     def setPlaces(self, p):
#         self.places = p
#
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#
# t1 = KitchenTable(2, 3, 0.8)
# t2 = DeskTable(1.5, 1, 0.9)
# t1.setPlaces(4)
# print(t1.places)
# print(t2.square())
# print(issubclass(KitchenTable, Table))



# переопределения методов, super()
class Parent:
    def __init__(self, x):
        self.x = x
        print("Parent init")

    def f(self, val):
        print(f"Parent f({val})")
        return self.x * val

    def greet(self):
        return "Hello from parent"

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        print("Child init")

    def f(self, val):
        print(f"Child f({val})")
        return self.x * self.y * val

    def greet(self):
        parent_gretting = super().greet()
        return f"{parent_gretting}, Hello from Child"

parent = Parent(2)
res = parent.f(3)
print("Result:", res, "\n")

child = Child(2, 5)
res = child.f(3)
print("Result:", res)
print(child.greet())
