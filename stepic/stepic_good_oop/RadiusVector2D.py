class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self,x=0,y=0) -> None:
        self.__x = self.__y = 0
        self.x = x
        self.y = y
    
    @classmethod
    def __is_verify(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if self.__is_verify(value):
            self.__x = value
        # else:
        #     self.__x = 0

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if self.__is_verify(value):
            self.__y = value
        # else:
        #     self.__y = 0    
    
    @staticmethod
    def norm2(vector):
        return vector.x**2+vector.y**2
    
v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)

print(f'{v1.x} {v1.y}')
print(f'{v2.x} {v2.y}')
print(f'{v3.x} {v3.y}')

