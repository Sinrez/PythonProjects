# lambda argument(s): expression

#Normal python function
def func(x):
    return x+x

#Lambda function
lambda x: x+x

# scalar (single) values
print((lambda x: x*2)(14))

# # list
list_1 = [1,2,3,4,5,6,7,8,9]
list_obj = (lambda x: x*2)
print(list_obj(list_1))

#string
str1 = 'AveCoder' 
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))

# using with list comprehensions:
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 15)]
 
# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())

# conditional if-else
# Example of lambda function using if-else
cond = lambda a, b : a if(a > b) else b
 
print(cond(10, 20))

#################################
# Lambda with multiple statements
List = [[12,23,56],[2, 6, 14, 72],[13, 5, 7, 22]]
 
# Sort each sublist
srt_lst = lambda x: (sorted(i) for i in x)
 
# Get the second largest element
sec_lrg = lambda x, f : [y[len(y)-2] for y in f(x)]
res = sec_lrg(List, srt_lst)
 
print(res)
