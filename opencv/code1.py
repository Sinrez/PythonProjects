import threading
import time
from tkinter import messagebox
import cv2
from PIL import Image as PILImage, ImageTk
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
from clover import srv

# Инициализация ROS
rospy.init_node('flight_control_gui')
bridge = CvBridge()

# Параметры для видеозаписи и потока
video_writer = None
latest_image = None
lock = threading.Lock()

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

# Запуск видеозаписи
def start_video_recording():
    global video_writer

    if video_writer is not None:
        messagebox.showinfo("Запись", "Видео уже записывается")
        return
    
    time_str = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{time_str}.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video_writer = cv2.VideoWriter(filename, fourcc, 30.0, (640, 480))

    def record_video():
        global latest_image
        while video_writer is not None:
            with lock:
                if latest_image is None:
                    continue
                video_writer.write(latest_image)
            rospy.sleep(0.03)

    threading.Thread(target=record_video, daemon=True).start()

# Остановка видеозаписи
def stop_video_recording():
    global video_writer
    if video_writer is not None:
        video_writer.release()
        video_writer = None
        messagebox.showinfo("Запись", "Видео успешно сохранено!")

# Функция для демонстрации работы с интерфейсом
def start_gui():
    global window
    window = tk.Tk()
    window.title("Управление дроном")
    window.geometry("1080x550")
    
    # Камера
    camera_label = tk.Label(window)
    camera_label.grid(row=0, column=2, rowspan=5)
    
    # Кнопки для управления видеозаписью
    tk.Button(window, text="Записать видео", width=20, bg="green", fg="white", command=start_video_recording).grid(row=6, column=3, padx=20, pady=10)
    tk.Button(window, text="Остановить видео", width=20, bg="red", fg="white", command=stop_video_recording).grid(row=7, column=3, padx=20, pady=10)
    
    # Обновление интерфейса
    window.after(100, update_image)
    window.mainloop()

# Запуск графического интерфейса
if __name__ == "__main__":
    start_gui()
