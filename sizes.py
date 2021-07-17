import cv2
import numpy as np

img = cv2.imread("Resources/person.png")
print(img.shape)

img_resized = cv2.resize(img, (960, 540))
img_cropped = img[0:480, 0:270]

cv2.imshow("Resized Image", img_resized)
cv2.imshow("Cropped Image", img_cropped)
cv2.waitKey(0)