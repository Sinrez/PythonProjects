from datetime import datetime

def dec_func(func):
    def wrapper(arg):
        t1 = datetime.now()
        x = func(arg)
        t2 = datetime.now()
        print("Time of completing this task:", x, end=" ")
        return x
    return wrapper

@dec_func    
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res
fact_100 = factorial(3)
print(fact_100)