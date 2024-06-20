def find_max_recursive(lst):
    """Напишите рекурсивную функцию для нахождения наибольшего
элемента в числовом списке. """
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max_recursive(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest

def count_down_recursive(n):
    """выводит числа от n до нуля"""
    if n < 0:
        return
    if n == 0:
        print(n, end='')
    else:
        print(n, end=',')
    count_down_recursive(n - 1)

def filter_words(lst):
    """возвращает новую функцию, которая будет фильтровать список слов и
возвращать только те слова, длина которых равна length"""
    def inner(length):
        return ','.join([l for l in lst if len(l) == length])
    return inner


def authenticate(username, password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            auth_username = 'John'
            auth_paswd = hash('Hello')
            if username.strip() == auth_username and hash(password) == auth_paswd:
                return func(*args, **kwargs)
            else:
                print("Ошибка аутентификации: Неверное имя пользователя или пароль!")
        return wrapper
    return decorator

@authenticate(username="John", password="Hello")
def some_function():
    print("Функция успешно выполнена!")

@authenticate(username="T1000", password="KillAll")
def another_function():
    print("А эта функция не выполнена!")


def validate_args(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Получаем информацию о типах аргументов функции
        expected_types = func.__annotations__

        # Проверка, что все аргументы имеют аннотации
        params = func.__code__.co_varnames[:func.__code__.co_argcount]
        if len(params) != len(expected_types):
            raise TypeError(f"Not all arguments of the function {func.__name__} are annotated")

        # Проверяем типы переданных аргументов
        for i, (arg, param) in enumerate(zip(args, params)):
            if param in expected_types and not isinstance(arg, expected_types[param]):
                raise TypeError(f"Неверный тип аргумента {param} для функции {func.__name__}, ожидается {expected_types[param].__name__}, получено {type(arg).__name__}")
        
        for key, value in kwargs.items():
            if key in expected_types and not isinstance(value, expected_types[key]):
                raise TypeError(f"Неверный тип аргумента '{key}' для функции {func.__name__}, ожидается {expected_types[key].__name__}, получено {type(value).__name__}")
        
        return func(*args, **kwargs)
    
    return wrapper

if __name__ == '__main__':
    my_list = [3, 7, 2, 10, 5]
    print("Наибольший элемент в списке:", find_max_recursive(my_list))
    print()

    count_down_recursive(5)
    print()

    filter1 = filter_words(['кот','пес','лошадь','дикобраз'])
    print(filter1(3))
    print()

    some_function()
    print()

    another_function()
    print()

    # Пример использования декоратора
    @validate_args
    def example_func(a: int, b: str):
        print(a, b)

    # Вызов функции с правильными типами аргументов
    example_func(1, 'hello')

    # Вызов функции с неправильными типами аргументов
    try:
        example_func('test', 2)
    except TypeError as e:
        print(e)



