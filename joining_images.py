import cv2
import numpy as np

img = cv2.imread('Resources/person.png')

img_resized = cv2.resize(img, (480, 270))

img_horizontal = np.hstack((img_resized,img_resized))
img_vertical = np.vstack((img_resized, img_resized))

cv2.imshow("Horizontal", img_horizontal)
cv2.imshow("Vertical", img_vertical)
cv2.waitKey(0)