# Программа для добавления текста на изображение
import cv2

image = cv2.imread("output_image.jpeg")

font = cv2.FONT_HERSHEY_COMPLEX
text = "Hello World"
cv2.putText(image, text, (150, 150), font, 4, (0, 0, 0), 4,cv2.LINE_AA)
cv2.imshow("Text on Image", image)
cv2.imwrite("Text on Image.jpeg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()