class Car:
    def __init__(self, model, max_speed):
        self.model = model #модель
        self.max_speed = max_speed #максимальная cкорость

class Toyota(Car):
    pass

class Hyundai(Car):
    pass

class Lada(Car):
    pass

toyota = Toyota('Corola', 180)    # создание экземпляра дочернего класса Toyota
hyundai = Hyundai('Solaris', 160)          # создание экземпляра дочернего класса Hyundai
lada = Lada('Vesta', 140)                 # создание экземпляра дочернего класса Lada

print(f'{type(toyota).__name__} : {toyota.__dict__}')   # Toyota : {'model': 'Corola', 'max_speed': 180}
print(f'{type(hyundai).__name__} : {hyundai.__dict__}') # Hyundai : {'model': 'Solaris', 'max_speed': 160}
print(f'{type(lada).__name__} : {lada.__dict__}')      # Lada : {'model': 'Vesta', 'max_speed': 140}