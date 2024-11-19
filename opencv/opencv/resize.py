# Программа для изменения размеров изображения
# Начальные размеры 1000 х 800
import cv2

image = cv2.imread("output_image.jpeg")

width = int(input("Введите новую ширину: "))
height = int(input("Введите новую высоту: "))

# Изменение размера
resize_image = cv2.resize(image, (width, height))
cv2.imshow("Resize Image", resize_image)
cv2.imwrite('Resized Image.jpeg', resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
