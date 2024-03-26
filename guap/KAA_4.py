def coordinates(num_points, x, y, i):
        if x > 0 and y > 0:
            print(f"Точка {i+1} с координатами ({x}, {y}) принадлежит к первой четверти.")
        elif x < 0 and y > 0:
            print(f"Точка {i+1} с координатами ({x}, {y}) принадлежит ко второй четверти.")
        elif x < 0 and y < 0:
            print(f"Точка {i+1} с координатами ({x}, {y}) принадлежит к третьей четверти.")
        elif x > 0 and y < 0:
            print(f"Точка {i+1} с координатами ({x}, {y}) принадлежит к четвёртой четверти.")
        else:
            print(f"Точка {i+1} с координатами ({x}, {y}) лежит на одной из осей.")
        

if __name__ == '__main__':
    stop_flag = False
    while not stop_flag:
        try:
            num_points = int(input("Введите количество точек: ").strip())
            for i in range(num_points):
                x = float(input(f"Введите значение X для точки {i+1}: ").strip())
                y = float(input(f"Введите значение Y для точки {i+1}: ").strip())
                coordinates(num_points, x, y, i)
        except ValueError as ve:
            print(f'Введено некорректное значение: {ve}')
        except Exception as ex:
            print(f'Произошла ошибка: {ex}')
        choice = input("Хотите выйти из программы? (y/n): ").strip().lower()
        if choice.lower() == 'y':
            print("Программа завершена.")
            stop_flag = True        