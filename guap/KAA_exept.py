from math import sqrt

#запилим пользовательское исключение
class InvalidOperationError(Exception):
    pass

#вынесен в "глобальные" константы чтобы можно было обновить в одном месте
operations = ('+', '-', '*','/')
oper_unpack = ' '.join(operations)

def calculate_square_root(num):
    try:
        return round(sqrt(num),2)
    except ValueError as ve:
        return f'Невозможно извлечь квадратный корень из отрицательного числа {ve}'
    except Exception as ex:
        return f'Что-то сломалось: {ex}'

def custom_calc(num1, num2, operation):
    if operation not in operations:
        raise InvalidOperationError(f'Передан некорректный символ операции! Вы передали {operation}. Нужно выбрать из {oper_unpack}')
    elif operation == '/' and num2 == 0:
        raise ValueError('division by zero is forbidden')
    else:
        return round((num1/num2),2)

def custom_calc_start():
    try:
        num1 = int(input('Введите первое число, числитель: ').strip())
        num2 = int(input('Введите второе число, знаменатель: ').strip())
        oper = input(f'Введите операцию из {oper_unpack}: ')
        print(f'Ваш результат: {custom_calc(num1, num2, oper)}')
    except InvalidOperationError as custom_error:
        print(custom_error)
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print('Случилась ошибка: {ex}')

def digits_into_list():
    stop_word = 'done'
    stop_flag = False
    res = []
    while not stop_flag:
        digit = input(f'Введите число или {stop_word} для выхода: ').strip()
        if digit != stop_word and not digit.isdigit():
            raise ValueError(f'Введите число или {stop_word} для завершения')
        elif digit != stop_word and digit.isdigit():
            res.append(int(digit))
        elif digit == stop_word:
            try:
                stop_flag = True
                return res  
            except IndexError as ie:
                return ie

def start_calc():
    while True:
        try:
            numbers = digits_into_list()
            print(numbers)
            if len(numbers) >= 13:  # Проверяем, что в списке есть элемент с индексом 12
                print(f'Элемент с индексом 12: {numbers[12]}')
                break
            else:
                raise KeyError('Элемент с индексом 12 отсутствует в списке.')
        except KeyError as ke:
            print(f'Ошибка: {ke}')
            break
        except ValueError as ve:
            print(f'Ошибка: {ve}')
        except Exception as ex:
            print(f'Произолшла общая ошибка: {ex}')


if __name__ == '__main__':
    ##Задание1
    # print(calculate_square_root(4))
    # print(calculate_square_root(-2))
    # print(calculate_square_root(0))      
    # print(calculate_square_root(4.0))
    # print(calculate_square_root(-2.0))

    ##Задание2
    # custom_calc_start()

    ##Задание3
    start_calc()