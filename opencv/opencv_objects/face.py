# Программа для распознавания лиц
# Подключение библиотеки opencv
import cv2

# Загрузка каскада
# cascade_src = "cascades/haarcascade_frontalface_default.xml"
# cascade_src = "cascades/haarcascade_frontalface_alt.xml"
cascade_src = "cascades/haarcascade_frontalface_alt2.xml"
# cascade_src = "cascades/haarcascade_frontalface_alt_tree.xml"
face_cascade = cv2.CascadeClassifier(cascade_src)

# Загрузка изображений
image = cv2.imread("src/2.jpg")

# Перевод в градации серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Обнаружения лиц на изображении
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.01, minNeighbors=2, minSize=(80, 80)
)

# Выделение распознанных областей
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Уменьшение изображения
image = cv2.resize(image, (400, 400))
# Отображение результатов
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
