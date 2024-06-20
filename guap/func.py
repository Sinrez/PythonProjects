# def function():
#     x = 10
#     function()
#
# function()

# def rec_function(x):
#     if x < 10: #базовый случай - условие выхода
#         print(x)
#         rec_function(x+1)
#
#
# rec_function(5)

#Классические задачи
# Вычисление факториала 4! = 1*2*3*4  0!=1 4!=(4-1)!*4
# def fact(n):
#     if n == 0:
#         return 1
#     return fact(n - 1) * n
#
#
# print(fact(4))

# факториал с помощью цикла
# def fact(n):
#     factorial = 1
#     for i in range(2, n+1):
#         factorial *= i
#     return factorial
#
# print(fact(5))


# Числа Фибоначчи  0, 1, 1, 2, 3, 5, 8, 13, 21
# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(8))
# [print(fib(n)) for n in range(15)]

# def fib(n):
#     if n in (0, 1):
#         return n
#     previous, fib_num = 0, 1
#     for i in range(2, n+1):
#         previous, fib_num = fib_num, previous + fib_num
#     return fib_num
#
#
# print(fib(8))
# [print(fib(n)) for n in range(15)]

# Палиндром
# def is_palindrome(s):
#     if len(s) < 1:
#         return True
#     else:
#         #print(s)
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False
# a = str(input("Введите строку:"))
# if (is_palindrome(a) == True):
#     print("Это палиндром!")
# else:
#     print("Это не палиндром!")

# Замыкания
# def outer():
#     l = [1, 2, 3]
#
#     def inner():
#         return l
#
#     return inner
#
# obj = outer()
# print(obj())


# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# closure = outer_function(5)
# print(closure(3))

# распаковка
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# lst = []
# for x in range(1, 4):
#     lst.append(outer_function(x))
#
# m1, m2, m3 = lst
#
# print(m1(1))
# print(m2(2))
# print(m3(10))

# Сохранение значений между вызовами
# def mean():
#     sample = []
#     def inner_mean(number):
#         sample.append(number)
#         return sum(sample) / len(sample)
#     return inner_mean
#
# sample_mean = mean()
#
# print(sample_mean(100))
# print(sample_mean(105))
# print(sample_mean(101))


# исключение UnboundLocalError
# def running_total_multiplier_creator(n):
#     running_total = 0
#     def multiplier(number):
#         product = number * n
#         t = running_total + product #running_total = running_total + product
#
#         return t
#     return multiplier
#
# running_doubler = running_total_multiplier_creator(2)
# print(running_doubler(5))


# Ключевое слово nonlocal
# def running_total_multiplier_creator(n):
#     running_total = 0
#
#     def multiplier(number):
#         product = number * n
#         nonlocal running_total
#         running_total += product
#         return running_total
#
#     return multiplier
#
#
# func = running_total_multiplier_creator(1)
# print(func(2))
# print(func(5))
# print(func(8))

# ограниченный доступ
def password_protected(password):
    def inner():
        if password == 'secret':
            print("Access granted")
        else:
            print("Access denied")
    return inner

login = password_protected('secret')
login2 = password_protected('сбомлид')
login()
login2()
