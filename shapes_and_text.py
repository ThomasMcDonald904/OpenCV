import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

#img[:] = 75,48,110

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (75,48,110), 5)
cv2.rectangle(img,(0,0),(250,350), ((0,255,255)), 2)
cv2.circle(img, (400,50), 30, (108, 174, 226), cv2.FILLED)
cv2.putText(img, "Some Text", (300, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (240, 40,56), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)