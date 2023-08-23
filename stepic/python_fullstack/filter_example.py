'''
The job of filter() is to apply a decision function to each value in an input iterable and return a new iterable with those items that pass the test.
'''

nums = [-5, 0, 1, 3, -4, -6, 9, -7, 2, 4, 5]

# def filter_negatives(nums):
#     neg_nums = []
#     for num in nums:
#         if num < 0:
#             neg_nums.append(num)
#     return neg_nums

# if __name__ == '__main__':

#     print(filter_negatives(nums))


################
## filter(function, iterable)

# neg_nums = filter(lambda x : x < 0, nums)
# print(list(neg_nums))

# def is_negative(num):
#     return num < 0

# if __name__ == '__main__':
#     print(list(filter(is_negative, nums)))

#################
### filter + map
import math


def is_negative(num):
    return num < 0

neg_nums = list(filter(is_negative, nums))
print(neg_nums)

print(list(map(lambda n: math.sqrt(math.pow(n, 2)), neg_nums))) # turning negative numbers to positive

print(list(map(lambda n: math.sqrt(math.pow(n, 2)), filter(is_negative, nums))))

#################
### filter + map + reduce

from functools import reduce

def is_negative(num):
    return num < 0

neg_nums = list(filter(is_negative, nums))
print(reduce(lambda a, b: a * b, neg_nums))
print(reduce(lambda a, b: a * b, filter(is_negative, nums)))

### Filtering Iterables With filterfalse()

from itertools import filterfalse

def is_negative(num):
    return num < 0

print(list(filterfalse(is_negative, nums)))