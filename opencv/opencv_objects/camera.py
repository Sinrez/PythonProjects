# Программа для машин по видео
# Подключение библиотеки opencv
import cv2

# Загрузка каскада
cascade_src = "cascades/haarcascade_frontalface_default.xml"
# cascade_src = "cascades/haarcascade_frontalface_alt.xml"
# cascade_src = "cascades/haarcascade_frontalface_alt2.xml"
# cascade_src = "cascades/haarcascade_frontalface_alt_tree.xml"
# cascade_src = "cascades/cars.xml"
car_cascade = cv2.CascadeClassifier(cascade_src)

# Вывод с камеры 0 или 1 или 2
cap = cv2.VideoCapture(0)

while True:
    ret = cap.read()
    if ret[0]:
        img = ret[1]
    else:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=2
    )

    for x, y, w, h in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow('video', img)

    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()