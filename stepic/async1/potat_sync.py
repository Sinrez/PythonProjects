from time import sleep

def cook_potatoes():
    print("Почистили и отправили в кастрюлю, ждем-с")
    sleep(10)
    print('Картофан готов, достаем')

def cut_bread(count: int):
    #пилим хлеб на count кусков
    for i in range(count):
        sleep(4)
        print(f'Отрезали кусок {i + 1}')
    
    print(f'Отрезали {count} кусков')

if __name__ == '__main__':
    cook_potatoes()
    cut_bread(4)
    print('Кушать подано - садитесь жрать!')