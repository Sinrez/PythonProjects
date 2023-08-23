import bisect
# from array import array

# int_array = array('i', [18, 6, 21, 20, 43, 22, 33, 60, 8, 4, 3, 6, 16, 31, 34])

# print(int_array.typecode)
# print(int_array.itemsize)

# int_array.insert(0,0)
# int_array.append(42)
# int_array.extend([35,36,37])

# print(int_array)

# for i, elem in enumerate(int_array):
#     int_array[i] = elem *2

# print(int_array)

# int_array.insert(0, 5.5)

# byte_array = array('B', [18, 6, 21, 20, 43, 22, 33, 60, 8, 4, 3, 6, 16, 31, 34])

# print(byte_array.typecode)
# print(byte_array.itemsize)

# # byte_array.append(300)

# list1 = byte_array.tolist()
# print(list1)

# print(list1.typecode)

# even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# print(bisect.bisect(even_numbers, 14))
# print(bisect.bisect_left(even_numbers, 14))
# print(bisect.bisect_right(even_numbers, 14))

# bisect.insort_right(even_numbers, 15)
# print(even_numbers)

scores = [76, 84, 65, 90, 68]

grades ='FDCBA'

breakpoints = [60, 70, 80, 90]

def calc_grade(score):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

results = [calc_grade(score) for score in scores]
print(results)