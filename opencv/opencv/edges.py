# Программа для выделения контуров изображения
import cv2

image = cv2.imread("output_image.jpeg")

edges_image = cv2.Canny(image, 200, 100)

cv2.imshow("Edges", edges_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
