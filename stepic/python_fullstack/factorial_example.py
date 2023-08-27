### add some slides as well

# iterative approach to factorial problem:
def factorial(num):
    return_value = 1
    for i in range(2, num + 1):
        return_value *= i
    return return_value

######################
# recursive approach:
def factorial(num):
    return 1 if num <= 1 else num * factorial(num-1)

####################
# next iteration

def factorial(num):
    print(f'call factorial() with num == {num}')
    return_val = 1 if num <= 1 else num * factorial(num-1)
    print(f'factorial({num}) returned {return_val}')
    return return_val

####################
# use reduce()

from functools import reduce

def factorial(num):
    return reduce(lambda a, b: a * b, range(1, num + 1) or [1])

###################
# use math factorial
# 

from math import factorial

factorial(5) # or in if name main

if __name__ == '__main__':
    factorial(5)
    # or here: math.factorial(5)