# Программа для записи изображения
import cv2

image = cv2.imread('1.jpeg')

cv2.imwrite('output_image.jpeg', image)