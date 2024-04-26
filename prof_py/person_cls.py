class Person:
    """Определение чела по фио"""

    def __init__(self, fname: str, mname: str = None, lname: str = None):
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def full_name(self) -> str:
        """Метод возвращает полное фио если есть"""
        full_name = self.fname
        if self.mname is not None:
            full_name = f"{full_name} {self.mname}"
        if self.lname is not None:
            full_name = f"{full_name} {self.lname}"
        return full_name


def main():
    people = [
        Person("John", "George", "Smith"),
        Person("Bill", lname="Thompson"),
        Person("Sam", mname="Watson"),
        Person("Tom"),
    ]


    for person in people:
        print(person.full_name())


if __name__ == "__main__":
    main()