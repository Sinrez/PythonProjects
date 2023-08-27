# def greet(func):
#     def wrapper(*args, **kwargs):
#         print("Hello!")
#         return func(*args, **kwargs)
#     return wrapper

# @greet
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("John")

##########################

# def log_function(func):
#     def wrapper(*args, **kwargs):
#         print(f"Log: {func.__name__} was called")
#         return func(*args, **kwargs)
#     return wrapper


# @log_function
# def add(x, y):
#     return x + y

# add(5, 2)

###########################

# import time

# def log_execution_time(log_level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             start_time = time.perf_counter()
#             result = func(*args, **kwargs)
#             end_time = time.perf_counter()
#             execution_time = end_time - start_time
#             print(f"{log_level}: {func.__name__} took {execution_time:.6f} seconds to execute")
#             return result
#         return wrapper
#     return decorator

# @log_execution_time("INFO")
# def add(x, y):
#     time.sleep(1)
#     return x + y

# result = add(2, 3)
# print(result)

##########################

# def decorator_1(func):
#     def wrapper(*args, **kwargs):
#         # Do something before
#         print('John enters the room')
#         result = func(*args, **kwargs)
        
#         # Do something after
#         return result
#     return wrapper

# def decorator_2(func):
#     def wrapper(*args, **kwargs):
#         # Do something before
#         result = func(*args, **kwargs)
        
#         print('John leaves the room')
#         # Do something after
#         return result
#     return wrapper

# @decorator_1
# @decorator_2
# def greet(name):
#     print("Hello, " + name)


# greet('John')