### generator start

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

### example with a large file reader

file_name = ('huge_csv.csv')

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

### generator expressions
import math

squared_list_comp = [math.pow(num, 2) for num in range(5)]
print(squared_list_comp)

squared_gen_comp = (math.pow(num, 2) for num in range(5))
print(squared_gen_comp)
print(list(squared_gen_comp))

## profiling
import cProfile

cProfile.run('[math.pow(num, 2) for num in range(1000000)]')

cProfile.run('(math.pow(num, 2) for num in range(1000000))')


# exhausting the generator

def print_strings():
    yield_str = 'aaaaaaaaaaaaaaaaaaaaa'
    yield yield_str
    yield_str = 'bbbbbbbbbbbbbbbbbbbbb'
    yield yield_str
    yield_str = 'ccccccccccccccccccccc'
    yield yield_str

iter_print_strings = print_strings()

print(next(iter_print_strings))
print(next(iter_print_strings))
print(next(iter_print_strings))
#print(next(iter_print_strings))

############## stop iteration

chars = ['a', 'b', 'c', 'd', 'e']

it = iter(chars)

while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)

