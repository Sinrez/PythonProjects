# functools.reduce(function, iterable[, initializer])
from functools import reduce


# The Python documentation also states that reduce() is roughly equivalent to the following Python function:
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

#######################

def ave_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

print(ave_add(2, 4))

nums = [1, 2, 3, 4, 5]

print(reduce(ave_add, nums))

############## Initializer

print(reduce(ave_add, nums, 1000))

print(reduce(lambda a, b: a + b, nums))

############################

from operator import add

print(add(2, 3))

print(reduce(add, nums))

print(sum(nums))

############### mult nums

def ave_mult(product, nums): 
    for num in nums:
        product *= num

    return product

print(ave_mult(1, nums))

##################

def ave_mult(a, b):
    return a * b

print(ave_mult(4, 5))

print(reduce(ave_mult, nums))

print(reduce(lambda a, b: a * b, nums))

########################

from operator import mul

print(mul(4, 5))

print(reduce(mul, nums))

################ reduce vs accumulate

from itertools import accumulate

print(list(accumulate(nums)))

print(reduce(add, nums))

print(list(accumulate(mul)))

print(reduce(mul, nums))

### performance vs readability

from timeit import timeit

# func

def add(a, b):
    return a + b

ave_add = reduce(add, range(100))
print(timeit(ave_add, "import functools", globals={'add': add}))

# lambda
ave_lambda = reduce(lambda x, y: x + y, range(100))
print(timeit(ave_lambda, "import functools"))

# operator.add
operator_add = reduce(add, range(100))
print(timeit(operator_add, "import functools, operator"))

# sum
print(sum(range(100)), globals={"sum":sum})