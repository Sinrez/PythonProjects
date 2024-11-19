# Программа для создания черно-белого изображения
import cv2

image = cv2.imread("output_image.jpeg")
image = cv2.imread("2.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray_image)
cv2.imwrite("Gray Image.jpg", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()