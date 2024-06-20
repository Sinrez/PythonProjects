class Juice:
    def __init__(self, name, val) -> None:
        self.name = name
        self.val = val
    
    def __str__(self) -> str:
        return f'{self.name} | {self.val}'
    
    def __add__(self, obj):
        return Juice(self.name+'&'+obj.name, self.val+obj.val)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)