# Программа для добавления прямоугольника на изображение
import cv2

image = cv2.imread("output_image.jpeg")

cv2.rectangle(image, (50, 150), (400, 300), (0, 255, 0), 3)

cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()