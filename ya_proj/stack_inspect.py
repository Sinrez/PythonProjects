import inspect


def print_call_stack():
    # Функция inspect.stack() возвращает объект-генератор.
    # В каждом элементе генератора хранится именованный кортеж.
    # Из этого кортежа берём элемент с названием function: frame.function.
    # В этом элементе хранится название вызванной функции.
    print([frame.function for frame in inspect.stack()])


def inner():
    print_call_stack()  # 4, 7


def outer():
    print_call_stack()  # 3
    inner()
    print_call_stack()  # 5


# А это ответ на вопрос, который сейчас появится.
print([frame.function for frame in inspect.stack()])  # 1
print_call_stack()  # 2
outer()
print_call_stack()  # 6
inner()