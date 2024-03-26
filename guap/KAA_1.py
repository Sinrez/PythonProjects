def use_variables():
    """программа выводит значения, типы данных и адреса переменных в памяти"""
    digit_1 = 5
    digit_2 = 3.14
    name = 'Alex'
    bool_val = True
    reg = '1-3*j'  # какое значение использовать для j?

    for name, val in locals().items():
        print(f'Имя переменной: {name}, значение: {val}, тип: {type(val)}, адрес в памяти: {id(val)}')

if __name__ == '__main__':
    use_variables()
