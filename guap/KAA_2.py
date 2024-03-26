import math

def calculator(operation, num1, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль!")
    elif operation == '^':
        result = num1 ** num2
    elif operation == 'sqrt':
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            print("Ошибка: нельзя извлечь квадратный корень из отрицательного числа!")
    else:
        print("Ошибка: неподдерживаемая операция!")
    
    return result

if __name__ == '__main__':
    operation = input("Введите знак математической операции (+, -, *, /, ^, sqrt): ").strip()
    if operation not in ('+', '-', '*', '/', '^', 'sqrt'):
        print('Введен некорректный символ операции!')
    num1 = float(input("Введите первое число: "))
    
    if operation != 'sqrt':
        num2 = float(input("Введите второе число: "))
    else:
        num2 = None
    
    result = calculator(operation, num1, num2)
    
    if result is not None:
        print(f"Результат: {result}")
