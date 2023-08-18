numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#### for loop #####

squares = []
for number in numbers:
    squares.append(number**2)
print(squares)  

#### list comp ####

squares = [number**2 for number in numbers]
print(squares) 

###### list comp cond ########

evens = [number for number in numbers if number % 2 == 0]
print('evens', evens) 

####### list comp pairs ##############

numbers1 = [0, 1, 2, 3]
numbers2 = [4, 5, 6, 7]

pairs = [(number1, number2) for number1 in numbers1 if number1 % 2 == 0 for number2 in numbers2 if number2 % 2 == 1]
print(pairs)

###### list comp range ###########

lists = [[i for i in range(j)] for j in range(5)]
print('lists', lists)  