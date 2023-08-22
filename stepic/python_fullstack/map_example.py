import math

def square(n):
    return pow(n, 2)

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squared_list = map(square, num_list)
# print(squared_list)
# print(f'squared_list: {list(squared_list)}')

############################################

# float_list = [1.23, 2.24, 3.35, 4.46, 5.57, 6.68, 7.79, 8.89, 9.99]

# rounded_list = map(round, float_list)
# ceiled_list = map(math.ceil, float_list)
# floored_list = map(math.floor, float_list)

# print(f'rounded_list: {list(rounded_list)}')
# print(f'ceiled_list: {list(ceiled_list)}')
# print(f'floored_list: {list(floored_list)}')

#############################################

# my_string = "DADADA DUDUDU DIDIDI"

# def lower_chars(s):
#     return s.lower()

# new_str_list = map(lower_chars, my_string)
# print(f'new_str_list: {list(new_str_list)}')

#############################################

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lambda_list = map(lambda x: x*10, num_list)
# print(f'lambda_list: {list(lambda_list)}')

#############################################

# list1 = [2, 2, 2, 2, 2]
# list2 = [5, 5, 5, 5, 5]

# def mult_func(list1, list2):
#     return list1 * list2

# mult_list = map(mult_func, list1, list2)
# print(f'mult_list: {list(mult_list)}')

#############################################

tuple1 = ("Room", "Room", "Room", "Room")
list1 = ["A", "B", "C", "D"] 

def tupl_list_func(tuple1, list1):
    return tuple1 + " - " + list1

room_list = map(tupl_list_func, tuple1, list1)
print(f'room_list: {list(room_list)}')