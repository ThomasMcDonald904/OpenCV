import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width, height = 250, 350
points1 = np.float32([[111,219],[287,188],[154,482],[352, 440]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points1, points2)

img_output = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image", img_output)

cv2.waitKey(0)