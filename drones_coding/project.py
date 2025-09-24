import tkinter as tk
from tkinter import filedialog, messagebox
import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
import json
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from PIL import Image as PILImage, ImageTk


window = tk.Tk()
window.title("Управление дроном")
window.geometry("920x550")

# Поля ввода и лейблы
tk.Label(window, text="Высота взлета (м): ").grid(row=0, column=0, padx=20, pady=10)
entry_z = tk.Entry(window,width=10).grid(row=0,column=1)

tk.Label(window, text="Координата X (м): ").grid(row=1, column=0, padx=20, pady=10)
entry_x=tk.Entry(window, width=10).grid(row=1, column=1)

tk.Label(window, text="Координата Y (м): ").grid(row=2, column=0, padx=20, pady=10)
entry_y = tk.Entry(window, width=10).grid(row=2, column=1)

tk.Label(window, text="Широта: ").grid(row=3, column=0, padx=20, pady=10)
entry_lat = tk.Entry(window, width=10).grid(row=3, column=1)

tk.Label(window, text="Долгота: ").grid(row=4, column=0, padx=20, pady=10)
entry_lon = tk.Entry(window, width=10).grid(row=4, column=1)

tk.Label(window, text="Скорость (м/с): ").grid(row=5, column=0, padx=20, pady=10)
entry_speed = tk.Entry(window, width=10).grid(row=5, column=1)

# Кнопки
takeoff_button = tk.Button(window, text="Взлет", width=20, bg="brown3", fg="white", relief="solid").grid(row=6,column=0,padx=20, pady=5)
land_button = tk.Button(window, text="Посадка", width=20, relief="solid").grid(row=7, column=0, padx=20,pady=5)
global_coordinates_button = tk.Button(window, text="Гл. Координаты", width=20, relief="solid").grid(row=8, column=0, padx=20, pady=5)
flip_button = tk.Button(window, text="Флип", width=20, relief="solid").grid(row=9, column=0, padx=20, pady=5)
load_plan_button = tk.Button(window, text="Загрузить план", width=20, relief="solid").grid(row=10, column=0, padx=20, pady=5)
home_button = tk.Button(window, text="Домой", width=20, relief="solid").grid(row=6, column=1, padx=20, pady=5)
telemetry_button = tk.Button(window, text="Телеметрия", width=20, relief="solid").grid(row=7, column=1, padx=20, pady=5)
local_coordinates = tk.Button(window, text="Лок. Координаты", width=20, relief="solid").grid(row=8, column=1, padx=20, pady=5)
activate_plan = tk.Button(window, text="Активировать план", width=20, relief="solid").grid(row=10, column=1, padx=20, pady=5 )

status_label = tk.Label(window, text="Состояние дрона", fg="blue").grid(row=11, column=0, columnspan=2)
alt_label = tk.Label(window, text="Текущая высота", fg="blue").grid(row=10, column=3)

camera_label = tk.Label(window,bg="red").grid(row=0, column=3, rowspan=8, columnspan=4)

window.mainloop()
