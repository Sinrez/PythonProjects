import tkinter as tk
from tkinter import messagebox, filedialog
import rospy
from clover import srv
from std_srvs.srv import Trigger
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from PIL import Image as PILImage, ImageTk
import threading
from datetime import datetime
import math
import json
import csv
import random

rospy.init_node('flight_control_gui')

get_telemetry = rospy.ServiceProxy("get_telemetry", srv.GetTelemetry)
navigate_global = rospy.ServiceProxy("navigate_global", srv.NavigateGlobal)
land = rospy.ServiceProxy("land", Trigger)
navigate = rospy.ServiceProxy("navigate", srv.Navigate)

bridge = CvBridge()
fullbody_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

latest_image = None
lock = threading.Lock()
video_writer = None
running_mode = None
flight_plan = None

start = get_telemetry()
home_position = [start.lat, start.lon]
z = float(0)
speed = float(1)

def infinity_fly():
    """Бесконечный полет дрона по случайным координатам"""
    print('Запущен режим бесконечного автономного полета')
    while True:
        x = random.uniform(-10, 10)  
        y = random.uniform(-10, 10)
        print(f"Дрон летит в точку: X={x}, Y={y}")
        navigate(x=x, y=y, z=3, frame_id='body', speed=1)
        arrival_wait()

# Функция для обновления интерфейса
def update_altitude():
    """Функция автоматического обновления высоты """
    try:
        telem = get_telemetry()
        altitude = telem.z
        alt_label.config(text=f"Текущая высота полета: {altitude:.2f} м")
    except:
        alt_label.config(text="Ошибка получения высоты")
    window.after(1000, update_altitude)

# Интерфейс
window = tk.Tk()
window.title("Управление дроном")
window.geometry("1080x600")
window.resizable(False, False)

# Поля ввода
tk.Label(window, text="Высота взлета (м): ").grid(row=0, column=0, padx=20, pady=10)
entry_z = tk.Entry(window, width=10)
entry_z.grid(row=0, column=1, pady=10)

tk.Label(window, text="Координата X (м): ").grid(row=1, column=0, padx=20, pady=10)
entry_x = tk.Entry(window, width=10)
entry_x.grid(row=1, column=1, pady=10)

tk.Label(window, text="Координата Y (м): ").grid(row=2, column=0, padx=20, pady=10)
entry_y = tk.Entry(window, width=10)
entry_y.grid(row=2, column=1, pady=10)

tk.Label(window, text="Широта: ").grid(row=3, column=0, padx=20, pady=10)
entry_lat = tk.Entry(window, width=10)
entry_lat.grid(row=3, column=1, pady=10)

tk.Label(window, text="Долгота: ").grid(row=4, column=0, padx=20, pady=10)
entry_lon = tk.Entry(window, width=10)
entry_lon.grid(row=4, column=1, pady=10)

tk.Label(window, text="Скорость (м/с): ").grid(row=5, column=0, padx=20, pady=10)
entry_speed = tk.Entry(window, width=10)
entry_speed.grid(row=5, column=1, pady=10)

# Кнопки управления полетом
takeoff_button = tk.Button(window, text="Взлет", width=20, bg="lightgreen", fg="black", relief="solid", activebackground="silver", command=takeoff)
takeoff_button.grid(row=6, column=0, padx=20, pady=10)

land_button = tk.Button(window, text="Посадка", width=20, bg="lightcoral", fg="black", relief="solid", activebackground="silver", command=land_drone)
land_button.grid(row=7, column=0, padx=20, pady=10)

local_coordinates_button = tk.Button(window, text="Лок. Координаты", width=20, relief="solid", activebackground="silver", command=fly_to_local_coordinates)
local_coordinates_button.grid(row=6, column=1, padx=20, pady=10)

global_coordinates_button = tk.Button(window, text="Гл. Координаты", width=20, relief="solid", activebackground="silver", command=fly_to_global_coordinates)
global_coordinates_button.grid(row=7, column=1, padx=20, pady=10)

home_button = tk.Button(window, text="Домой", width=20, relief="solid", activebackground="silver", command=fly_home)
home_button.grid(row=8, column=0, padx=20, pady=10)

# Кнопка для бесконечного полета
infinity_fly_button = tk.Button(window, text="Бесконечный полет", width=20, relief="solid", activebackground="silver", command=lambda: threading.Thread(target=infinity_fly, daemon=True).start())
infinity_fly_button.grid(row=8, column=1, padx=20, pady=10)

# Кнопки для записи телеметрии и других функций
telemetry_button = tk.Button(window, text="Телеметрия", width=20, relief="solid", activebackground="silver", command=show_telemetry)
telemetry_button.grid(row=9, column=0, padx=20, pady=10)

record_telemetry_button = tk.Button(window, text="Запись телеметрии", width=20, relief="solid", activebackground="silver", bg="lightblue", fg="black", command=start_telemetry_recording)
record_telemetry_button.grid(row=9, column=1, padx=20, pady=10)

load_plan_button = tk.Button(window, text="Загрузить План", width=20, relief="solid", activebackground="silver", bg="lightblue", fg="black", command=browse_files)
load_plan_button.grid(row=10, column=0, padx=20, pady=10)

run_plan_button = tk.Button(window, text="Активировать План", width=20, relief="solid", activebackground="silver", bg="lightblue", fg="black", command=fly_by_plan)
run_plan_button.grid(row=10, column=1, padx=20, pady=10)

exit_button = tk.Button(window, text="Выход", width=20, bg="lightgrey", fg="black", relief="solid", activebackground="silver", command=window.quit)
exit_button.grid(row=11, column=0, columnspan=2, padx=20, pady=7)

# Статус и высота
status_label = tk.Label(window, text="Состояние дрона", fg="blue")
status_label.grid(row=12, column=0, columnspan=2)

alt_label = tk.Label(window, text="Текущая высота", fg="blue")
alt_label.grid(row=12, column=2, columnspan=2)

# Камера
camera_label = tk.Label(window)
camera_label.grid(row=0, column=2, rowspan=5)

# Распознавание объектов
tk.Button(window, text="Распознать объекты", width=20, bg="lightgreen", fg="black", command=start_object_detection).grid(row=6, column=2, padx=20, pady=10)
tk.Button(window, text="Остановить распознание", width=20, bg="lightcoral", fg="black", command=stop_detection).grid(row=7, column=2, padx=20, pady=10)

# Запись видео
tk.Button(window, text="Записать видео", width=20, bg="lightgreen", fg="black", command=start_video_recording).grid(row=6, column=3, padx=20, pady=10)
tk.Button(window, text="Остановить видео", width=20, bg="lightcoral", fg="black", command=stop_video_recording).grid(row=7, column=3, padx=20, pady=10)

window.after(1000, update_altitude)
window.mainloop()
