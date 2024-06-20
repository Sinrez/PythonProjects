def null_decorator(func):
    return func

def greet():
    return 'Hello!'

greet2 = null_decorator(greet)
print(greet2())

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def example_func(a: int, b: str):
        print(a, b)

expected_types = example_func.__annotations__
print(expected_types)

params = example_func.__code__.co_varnames[:example_func.__code__.co_argcount]
print(params)
print(example_func.__code__.co_argcount)
print()
