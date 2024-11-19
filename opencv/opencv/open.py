# pip install numpy
# pip install opencv-python
# Программа для чтения изображения

# Подключение библиотеки
import cv2

# Загрука изображения
image = cv2.imread('1.jpeg')

# Отображение изображения
cv2.imshow('Read Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()