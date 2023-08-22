import itertools


num_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]

# print(itertools.groupby(num_list))

# for i, j in itertools.groupby(num_list):
#     print("i: ", i, "j: ", list(j))

###################################

# print([i for i, j in itertools.groupby(num_list)])

# print([list(j) for i, j in itertools.groupby(num_list)])

# print([(i, list(j)) for i, j in itertools.groupby(num_list)])

####################################
# print('LAMBDA')
# print([(i, list(j)) for i, j in itertools.groupby(num_list, lambda x: x * 2)])

######################################

# data = [[0, 'Egg', 10],
#         [1, 'Egg', 20],
#         [2, 'Ham', 30],
#         [3, 'Ham', 40],
#         [4, 'Ham', 50]]

# for i, j in itertools.groupby(data, lambda x: x[1]):
#     print(i, list(j))

#########################################

tpl = (1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4)

print('TUPLE')
print([(i, list(j)) for i, j in itertools.groupby(tpl)])

print(tuple((i, tuple(j)) for i, j in itertools.groupby(tpl) ))

#########################################

s = 'xxxyyyzzz'

print('STRING')

print([(i, list(j)) for i, j in itertools.groupby(s)]) 

######################
"""
Напишите функцию, которая принимает на вход строку слов и возвращает словарь, 
содержащий частоту каждого слова в строке. Словарь должен включать слова в качестве ключей и их частоты в качестве значений.
"""


# from typing import Dict
# from itertools import groupby


# def word_frequencies(string):
#     return {i:len(list(j)) for i,j in groupby(sorted(string.split()))}
#     # Поместите свой код сюда

# print(word_frequencies('hello world and hello universe'))
# print(word_frequencies('hello world'))

from itertools import groupby

def group_integers(names):
    return [[*list(j)] for i, j in groupby(sorted(names))]

print(group_integers([1, 2, 3, 4, 3, 2, 1]))
print(group_integers([-1, -2, 3, -2, 4, -1]))
print(group_integers([5, 5, 5, 5, 5]))