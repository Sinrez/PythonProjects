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
    elif operation in ['>', '<', '==', '>=', '<=']:
        result = f"{num1} {operation} {num2}"
    else:
        print("Ошибка: неподдерживаемая операция!")
    
    return result

if __name__ == '__main__':
    exit_flag = False
    
    while not exit_flag:
        category = input("Выберите категорию операции (1 - математические операции, 2 - операции сравнения): ")
        
        if category == '1':
            operation = input("Введите знак математической операции (+, -, *, /, ^, sqrt): ").strip()
            if operation not in ('+', '-', '*', '/', '^', 'sqrt'):
                print('Введен некорректный символ операции!')
                break
            try:
                num1 = float(input("Введите первое число: ").strip())       
                if operation != 'sqrt':
                    num2 = float(input("Введите второе число: ").strip())
                else:
                    num2 = None
            except ValueError as ve1:
                print(f'Введено не число! {ve1}')
            except Exception as ex1:
                print(f'Ошибка {ex1}') 
            
            result = calculator(operation, num1, num2)
            
            if result is not None:
                print(f"Результат: {result}")
        
        elif category == '2':
            operation = input("Введите символ сравнения (> < == >= <=): ").strip()
            if operation not in ('>', '<', '==', '>=', '<='):
                print('Недоспустимый символ сравнения!')
                break
            try:
                num1 = float(input("Введите первое число: ").strip())
                num2 = float(input("Введите второе число: ").strip())
            except ValueError as ve:
                print(f'Ошибка, введено не число! {ve}')
            except Exception as ex:
                print(f'Ошибка: {ex}')
            
            result = calculator(operation, num1, num2)
            
            if result is not None:
                print(f"Результат сравнения: {result}")
        
        else:
            print("Ошибка: неподдерживаемая категория операции!")
        
        choice = input("Хотите выйти из программы? (y/n): ").strip().lower()
        if choice.lower() == 'y':
            exit_flag = True