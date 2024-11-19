# Программа для поворота изображения
import cv2

image = cv2.imread("output_image.jpeg")

angle = int(input("Укажите угол поворота изображения: "))

width = image.shape[1]
height = image.shape[0]

center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotated_image)
cv2.imwrite("Rotated Image.jpeg", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()