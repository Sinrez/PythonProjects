# Программа для выделения контуров с элементами управления
import cv2

image = cv2.imread("output_image.jpeg")

cv2.namedWindow('Edges')

def nothing(x):
    pass

cv2.createTrackbar("Lower", "Edges", 0, 255, nothing)
cv2.createTrackbar("Upper", "Edges", 0, 255, nothing)

while True:
    lower_tresh = cv2.getTrackbarPos("Lower", "Edges")
    upper_tresh = cv2.getTrackbarPos("Upper", "Edges")

    edges = cv2.Canny(image, lower_tresh, upper_tresh)

    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) == 27:
        break

    cv2.imwrite("Edges_Output.jpeg", edges)

cv2.destroyAllWindows()