import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import random
from telemetry_logger import save_telemetry

rospy.init_node('flight_control')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
land = rospy.ServiceProxy('land', Trigger)

def arrival_wait(tolerance=0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

def log_telemetry():
    """Логируем текущие данные о полете"""
    telem = get_telemetry()
    print(f"Текущая телеметрия: Широта={telem.lat}, Долгота={telem.lon}, Высота={telem.z}, Скорость по x{telem.vx}, по y{telem.vy}, по z{telem.vz}")
    print(f"Рабочее напряжение: {telem.voltage}, полетный режим: {telem.mode}, тангаж: {telem.pitch} крен: {telem.roll} рыскание: {telem.yaw}")
    save_telemetry(telem)

def takeoff():
    """Функция взлета дрона"""
    z = float(input("Введите высоту полета в метрах: ").strip())
    navigate(x=0, y=0, z=z, frame_id='body', auto_arm=True)
    arrival_wait()
    
    # Логируем состояние полета после взлета
    log_telemetry()
    
    home_position = (get_telemetry().lat, get_telemetry().lon)
    print(f"Коптер взлетел на {z} метров")
    return home_position

def land_drone():
    """Функция посадки дрона"""
    print('Приземляемся...')
    land()
    rospy.sleep(3)  # Даем время для приземления
    log_telemetry()  # Логируем телеметрию после посадки
    print("Дрон приземлился.")

def fly_to_coordinates():
    """Полет по локальным координатам"""
    x = float(input("Введите координату X (метры): "))
    y = float(input("Введите координату Y (метры): "))
    print(f"Полет в точку X={x}, Y={y}")
    
    navigate(x=x, y=y, z=3, frame_id='body', speed=1)
    arrival_wait()
    
    # Логируем состояние полета после достижения точки
    log_telemetry()
    print(f"Дрон достиг точки X={x}, Y={y}")

def fly_to_global_coordinates():
    """Полет по глобальным координатам"""
    lat = float(input("Введите широту: "))
    lon = float(input("Введите долготу: "))
    print(f"Полет в точку: Широта={lat}, Долгота={lon}")
    
    navigate_global(lat=lat, lon=lon, z=3, yaw=math.inf, speed=1)
    arrival_wait()
    
    # Логируем состояние полета после достижения точки
    log_telemetry()
    print(f"Дрон достиг точки: Широта={lat}, Долгота={lon}")

def fly_home(home_position):
    """Возвращение дрона домой"""
    print(f"Возвращаемся домой в {home_position[0]}, {home_position[1]}")
    navigate_global(lat=home_position[0], lon=home_position[1], z=3, yaw=math.inf, speed=1)
    arrival_wait()
    
    # Логируем состояние полета после возвращения домой
    log_telemetry()

def infinity_fly():
    """Бесконечный полет дрона по случайным координатам"""
    print('Запущен режим бесконечного автономного полета')
    while True:
        x = random.uniform(-10, 10)  
        y = random.uniform(-10, 10)
        print(f"Дрон летит в точку: X={x}, Y={y}")
        navigate(x=x, y=y, z=3, frame_id='body', speed=1)
        arrival_wait()

        # Логируем состояние полета
        log_telemetry()

        # Ожидаем от пользователя команду для выхода из бесконечного полета
        print("Для продолжения полета нажмите любую клавишу, для выхода и возврата в основное меню введие 8")
        print("Для корректировки маршрута и ввода локальных координат введите 9")
        command = input('Введите команду: ').strip()
        if command == '8':
            print("Завершаем бесконечный полет.")
            break
        elif command == '9':
            fly_to_coordinates()


def main():
    home_position = None

    while True:
        print("\nВыберите действие: ")
        print("1 Взлет")
        print("2 Полет по локальным координатам")
        print("3 Полет по глобальным координатам")
        print("4 Возвращение домой")
        print("5 Посадка")
        print("6 Показать телеметрию")
        print("7 Бесконечный автономный полет с возможностью корректировки")
        print("0 Выход")

        choise = input("Введите номер действия: ").strip()
        
        if choise == '1':
            home_position = takeoff()
        elif choise == '2':
            fly_to_coordinates()
        elif choise == '3':
            fly_to_global_coordinates()
        elif choise == '4':
            if home_position is not None:
                fly_home(home_position)
            else:
                print("Ошибка: нельзя вернуться домой, так как дрон еще не взлетел.")
        elif choise == '5':
            land_drone()
        elif choise == '6':
            log_telemetry() 
        elif choise == '7':
            infinity_fly()
        elif choise == '0':
            print("Выход из программы...")
            land_drone()  # Приземляем дрон перед выходом
            print("Дрон приземлился. Завершаем работу программы.")
            break
        else:
            print("Такой команды нет. Попробуйте снова.")

if __name__ == '__main__':
    main()
