class Clock:
    def __init__(self,tm) -> None:
        self.__time = 0
        self.__time =self.set_time(tm)
    
    @classmethod
    def __check_time(cls,tm):
        return type(tm) == int and 0 <= tm < 100_000
            
    def set_time(self,tm):
        if self.__check_time(tm):
            self._time = tm
    
    def get_time(self):
        return self._time

clock = Clock(4530)
print(clock.get_time())