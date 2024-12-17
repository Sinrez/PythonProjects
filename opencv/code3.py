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

# Создание файла csv
def create_telemetry_csv():
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"telemetry_{time}.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Time", "X", "Y", "Z", "Lat", "Lon"])
    return filename

# Запись телеметрии
def record_telemetry_to_csv(filename):
    try:
        telem = get_telemetry()
        with open(filename, mode="a", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [
                    datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
                    telem.x,
                    telem.y,
                    telem.z,
                    telem.lat,
                    telem.lon
                ]
            )
    except Exception as e:
        status_label.config(text=f"Ошибка записи телеметрии {e}")

# Начало записи телеметрии
def start_telemetry_recording():
    global telemetry_filename
    telemetry_filename = create_telemetry_csv()

    def record_telemetry():
        while True:
            record_telemetry_to_csv(telemetry_filename)
            rospy.sleep(5)

    threading.Thread(target=record_telemetry, daemon=True).start()

# Функция автоматического обновления высоты 
def update_altitude():
    try:
        telem = get_telemetry()
        altitude = telem.z
        alt_label.config(text=f"Текущая высота: {altitude:.2f} м")
    except:
        alt_label.config(text="Ошибка получения высоты")
    window.after(1000, update_altitude)

def arrival_wait(tolerance=0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id="navigate_target")
        if math.sqrt(telem.x**2+telem.y**2+telem.z**2) < tolerance:
            break
        rospy.sleep(0.2)

# Взлет
def takeoff():
    global z
    global speed
    try:
        if entry_z.get():
            z = float(entry_z.get())
        else:
            z = float(3)
        if entry_speed.get():
            speed = float(entry_speed.get())
        else:
            speed = float(1)
        status_label.config(text=f"Взлет на высоту {z} м")
        threading.Thread(target=navigate, args=(0, 0, z, 1, 0, "body", True)).start()
        
    except:
        status_label.config(text="Ошибка: введите числовое значение для высоты и скорости")

# Посадка
def land_drone():
    threading.Thread(target=land).start()
    status_label.config(text="Дрон приземлился")

# Полет по локальным координатам
def fly_to_local_coordinates():
    global z
    global speed
    try:
        if entry_x.get():
            x = float(entry_x.get())
        else:
            x = 0
        if entry_y.get():
            y = float(entry_y.get())
        else:
            y = 0
        if entry_z.get():
            z = float(entry_z.get())
        else:
            if z != 0:
                z = float(0)
        if entry_speed.get():
            speed = float(entry_speed.get())
        else:
            speed = float(1.0)
        threading.Thread(target=navigate, args=(x, y, z, speed, 0, "body", False)).start()
        arrival_wait()
        status_label.config(text=f"Дрон достиг точки Х: {x}, Y: {y} с высотой Z: {z} и скоростью {speed}")
    except Exception as e:
        status_label.config(text=f"{e}")

# Полет по глобальным координатам
def fly_to_global_coordinates():
    try:
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
        z = float(entry_z.get())
        if entry_z.get():
            z = float(entry_z.get())
        else:
            z = 3
        if entry_speed.get():
            speed = float(entry_speed.get())
        else:
            speed = 1.0
        threading.Thread(target=navigate_global, args=(lat, lon, z, speed, 0, "map", False)).start()
        status_label.config(text=f"Дрон достиг точки широта: {lat}, долгота: {lon} с высотой Z: {z} и скоростью {speed}")
    except:
        status_label.config(text="Ошибка: введите числовое значение для широты, долготы, скорости, высоты")

# Возврат домой
def fly_home():
    if home_position[0] is None or home_position[1] is None:
        status_label.config(text="Ошибка: точка взлета не определена")
        return
    
    lat, lon = home_position[0], home_position[1]
    if entry_z.get():
        z = float(entry_z.get())
    else:
        z = 3.0
    threading.Thread(target=navigate_global, args=(lat, lon, z, 0, 1, "map", False)).start()
    status_label.config(text="Возвращаемся домой")

# Показ телеметрии
def show_telemetry():
    telem = get_telemetry()
    status_label.config(text=f"Телеметрия: широта={telem.lat}, долгота {telem.lon} ")

# Загрузка плана
def load_plan_file(filename):
    with open(filename, "r") as file:
        return json.load(file)

def browse_files():
    filename = filedialog.askopenfilename(filetypes=[("Flight Plan Files", "*.plan")])
    if filename:
        if filename.endswith(".plan"):
            try:
                global flight_plan
                flight_plan = load_plan_file(filename)
                status_label.config(text=f"Файл {filename} загружен ")
            except:
                messagebox.showerror("Ошибка", "Не удалось загрузить план")
        else:
            messagebox.showerror("Неверный файл", "Выберите файл с расширение .plan")

# Полет по плану
def fly_by_plan():
    if flight_plan is None:
        messagebox.showerror("Ошибка", "План полета не загружен")
        return
    def run_flight_plan():
        coordinates = []
        home_lat = flight_plan["mission"]["plannedHomePosition"][0]
        home_lon = flight_plan["mission"]["plannedHomePosition"][1]
        for item in flight_plan["mission"]["items"]:
            command = item["command"]
            if command == 16:
                coordinates.append((item['params'][4], item['params'][5]))
        print(coordinates)
        for item in flight_plan["mission"]["items"]:
            command = item["command"]
            z = item["params"][6]
            if command == 22:
                if get_telemetry().armed:
                    navigate_global(lat=home_lat, lon=home_lon,z=3,yaw=math.inf, speed=1, frame_id="map")
                    arrival_wait()
                    land()
                    return
                else:
                    navigate_global(lat=home_lat, lon=home_lon,z=z,yaw=math.inf, speed=1, frame_id="map", auto_arm=True)
                    navigate_global(lat=home_lat, lon=home_lon,z=z,yaw=math.inf, speed=1, frame_id="map")
                    arrival_wait()
                    for lat, lon in coordinates:
                        navigate_global(lat=lat, lon=lon, z=z, yaw=math.inf, speed=1,frame_id="map")
                        print(lat,lon)
                        arrival_wait()
            elif command == 20:
                navigate_global(lat=home_lat, lon=home_lon,z=3,yaw=math.inf, speed=1, frame_id="map")
                arrival_wait()
            elif command == 21:
                land()
    threading.Thread(target=run_flight_plan).start()

# Получение изображения с камеры
def camera_image(msg):
    global latest_image
    with lock:
        latest_image = bridge.imgmsg_to_cv2(msg, 'bgr8')

image_sub = rospy.Subscriber('main_camera/image_raw', Image, camera_image, queue_size=1)

# Обновление изображения в интерфейсе
def update_image():
    if latest_image is not None:
        with lock:
            img_rgb = cv2.cvtColor(latest_image, cv2.COLOR_BGR2RGB) 
            img_pil = PILImage.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(image=img_pil)

            camera_label.config(image=img_tk)
            camera_label.image = img_tk
    
    window.after(100, update_image)

# Распознание объектов с каскадом
def detect_objects():
    global latest_image
    while running_mode == "objects":
        with lock:
            if latest_image is None:
                continue
            img = latest_image.copy()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        objects = fullbody_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(30, 30))

        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        display_image(img)

# Показ обработанного изображения
def display_image(img):
    global video_writer
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    img_pil = PILImage.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil)

    camera_label.config(image=img_tk)
    camera_label.image = img_tk

    if video_writer is not None:
        video_writer.write(img)

# Запуск режима распознавания объектов
def start_object_detection():
    stop_detection()
    global running_mode
    running_mode = "objects"
    threading.Thread(target=detect_objects, daemon=True).start()

# Остановка режима
def stop_detection():
    global running_mode
    running_mode = None

# Запись видео
def start_video_recording():
    global video_writer

    if video_writer is not None:
        messagebox.showinfo("Запись", "Видео уже записывается")
        return
    
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{time}.avi"

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video_writer = cv2.VideoWriter(filename, fourcc, 30.0, (320, 240))

    def record():
        global latest_image
        while video_writer is not None:
            with lock:
                if latest_image is None:
                    continue
                video_writer.write(latest_image)
            rospy.sleep(0.03)

    threading.Thread(target=record, daemon=True).start()

# Остановка записи видео
def stop_video_recording():
    global video_writer
    if video_writer is not None:
        video_writer = None
        messagebox.showinfo("Запись", "Видео успешно сохранено!")

# Интерфейс
window = tk.Tk()
window.title("Управление дроном")
window.geometry("1080x550")
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

# Кнопки
takeoff_button = tk.Button(window, text="Взлет", width=20, bg="lightgreen", fg="black", relief="solid", activebackground="silver", command=takeoff).grid(row=6, column=0, padx=20, pady=10)
land_button = tk.Button(window, text="Посадка", width=20, bg="lightcoral", fg="black", relief="solid", activebackground="silver", command=land_drone).grid(row=7, column=0, padx=20, pady=10)
global_coordinates_button = tk.Button(window, text="Гл. Координаты", width=20, relief="solid", activebackground="silver", command=fly_to_global_coordinates).grid(row=8, column=0, padx=20, pady=10)
home_button = tk.Button(window, text="Домой", width=20, relief="solid", activebackground="silver", command=fly_home).grid(row=9, column=0, padx=20, pady=10)
local_coordinates_button = tk.Button(window, text="Лок. Координаты", width=20, relief="solid", activebackground="silver", command=fly_to_local_coordinates).grid(row=8, column=1, padx=20, pady=10)
telemetry_button = tk.Button(window, text="Телеметрия", width=20, relief="solid", activebackground="silver",command=show_telemetry).grid(row=9, column=1, padx=20, pady=10)
load_plan_button = tk.Button(window, text="Загрузить План", width=20, relief="solid", activebackground="silver", bg="lightblue", fg="black", command=browse_files).grid(row=8, column=2, padx=20, pady=10)
run_plan_button = tk.Button(window, text="Активировать План", width=20, relief="solid", activebackground="silver", bg="lightblue", fg="black", command=fly_by_plan).grid(row=8, column=3, padx=20, pady=10)

# Кнопка выхода
exit_button = tk.Button(window, text="Выход", width=20, bg="lightgrey", fg="black", relief="solid", activebackground="silver", command=window.quit).grid(row=10, column=3, padx=20, pady=10)

status_label = tk.Label(window, text="Состояние дрона", fg="blue")
status_label.grid(row=10, column=0, columnspan=2)

# Переносим alt_label до использования
alt_label = tk.Label(window, text="Текущая высота", fg="blue")
alt_label.grid(row=10, column=2, columnspan=2)

# Камера
camera_label = tk.Label(window)
camera_label.grid(row=0, column=2, rowspan=5)
tk.Button(window, text="Распознать объекты", width=20, bg="lightgreen", fg="black", command=start_object_detection).grid(row=6, column=2, padx=20, pady=10)
tk.Button(window, text="Остановить распознание", width=20, bg="lightcoral", fg="black", command=stop_detection).grid(row=7, column=2, padx=20, pady=10)
tk.Button(window, text="Записать видео", width=20, bg="lightgreen", fg="black", command=start_video_recording).grid(row=6, column=3, padx=20, pady=10)
tk.Button(window, text="Остановить видео", width=20, bg="lightcoral", fg="black", command=stop_video_recording).grid(row=7, column=3, padx=20, pady=10)

# Остальные кнопки
record_telemetry_button = tk.Button(window, text="Запись телеметрии", width=20, relief="solid", activebackground="silver", bg="lightblue", fg="black", command=start_telemetry_recording).grid(row=6, column=1, padx=20, pady=10)

window.after(1000, update_altitude)
window.mainloop()
