class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.height+self.height)
    
    def get_square(self):
        return self.width * self.height

class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def introduce(self):
        return f'Привет, я - {self.name}'

class Student(Person):

    def __init__(self, name) -> None:
        super().__init__(name)
    #тут описал для примера, что если не добавляем новых атрибутов
    #то init можно не описывать, по умолчанию наследуется родительский

    def introduce(self):
        return f'Привет, я студент, мое имя - {self.name}'

class Teacher(Person):

    def introduce(self):
        return f'Привет, я учитель, мое имя - {self.name}'

class Circle:
    count = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.count += 1

    @classmethod
    def total_objects(cls):
        return cls.count

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def check_radius(radius):
        return True if radius > 0 else False
    
    def __get_radius(self):
        return self.radius
    
    def __str__(self) -> str:
        return f'Я круг с радиусом {self.__get_radius()}'

if __name__ == '__main__':
    rec1 = Rectangle(2,2)
    rec2 = Rectangle(3,5)
    print()
    print(f'Площадь прямогульника rec1 равна {rec1.get_square()}')
    print(f'Периметр прямогульника rec1 равен {rec1.get_perimeter()}')
    print(f'Площадь прямогульника rec2 равна {rec2.get_square()}')
    print(f'Периметр прямогульника rec2 равена {rec2.get_perimeter()}')
    print()
    student = Student('Петр')
    teacher = Teacher('Борис')
    print(student.introduce())
    print(teacher.introduce())
    print()
    circle1 =  Circle(3)
    circle2 =  Circle(5)
    c = Circle.from_diameter(10)
    print(Circle.check_radius(5))
    print(Circle.check_radius(-1))
    print(circle1)
    print(circle2)
    print(c)
    print(Circle.total_objects())




    