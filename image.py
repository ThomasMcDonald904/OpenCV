import cv2

img = cv2.imread("Resources/person.png")

cv2.imshow("Image", img)

cv2.waitKey(0)