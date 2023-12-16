class AbstractClass:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        else:
            return "Ошибка: нельзя создавать объекты абстрактного класса"

        return cls.__instance

obj1 = AbstractClass()
obj2 = AbstractClass()
print(obj1)
print(obj2)

# class AbstractClass:
## it's a fucking current solve
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             return "Ошибка: нельзя создавать объекты абстрактного класса"