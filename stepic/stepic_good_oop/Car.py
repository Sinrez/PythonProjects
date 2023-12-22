class Car:
    def __init__(self) -> None:
        pass
    
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model_in):
        if type(model_in) == str and 2<=len(model_in)<=100:
            self.__model = model_in

car = Car()
car.model = "Toyota"
print(car.model)