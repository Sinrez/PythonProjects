class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
            return cls.__instance
        return cls.__instance    

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
for el in objs:
    print(el.name)